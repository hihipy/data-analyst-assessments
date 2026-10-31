"""Reference solution: Inpatient Deterioration Early Warning.

Run from the folder holding the four data files. Needs pandas, numpy, and scikit-learn.
Prints every figure in answer_key.md and writes answers.json.
"""
import json
import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import average_precision_score, roc_auc_score

O = "./"
A = {}
E = pd.read_csv(O + "encounters.csv.gz", parse_dates=["admit_time", "discharge_time"])
V = pd.read_csv(O + "vitals.csv.gz", parse_dates=["recorded_time", "entered_time"])
L = pd.read_csv(O + "labs.csv.gz", parse_dates=["collected_time", "resulted_time"])
T = pd.read_csv(O + "icu_transfers.csv.gz", parse_dates=["transfer_time"])
A["rows"] = {"encounters": len(E), "vitals": len(V), "labs": len(L), "icu_transfers": len(T)}

# ---- clean vitals
A["vitals_dups"] = int(V.duplicated().sum()); V = V.drop_duplicates()
f = V.temperature > 45                       # recorded in Fahrenheit
A["temp_fahrenheit"] = int(f.sum()); V.loc[f, "temperature"] = ((V.loc[f, "temperature"] - 32) * 5 / 9).round(1)
bad = ~V.heart_rate.between(20, 250)
A["hr_implausible"] = int(bad.sum()); V.loc[bad, "heart_rate"] = np.nan
A["vitals_after_transfer"] = int(V.merge(T, on="encounter_id").pipe(lambda m: (m.recorded_time > m.transfer_time).sum()))
# ---- clean labs
mg = (L.test == "Lactate") & (L.units == "mg/dL")
A["lactate_mg_dl"] = int(mg.sum()); L.loc[mg, "value"] = (L.loc[mg, "value"] / 9.01).round(2)

# ---- checkpoints every 4 hours on the clock, from admission to discharge or ICU transfer
E = E.merge(T, on="encounter_id", how="left")
E["stop"] = E[["discharge_time", "transfer_time"]].min(axis=1)
rows = []
for r in E.itertuples():
    ts = pd.date_range(r.admit_time.ceil("4h"), r.stop, freq="4h", inclusive="left")
    rows.append(pd.DataFrame({"encounter_id": r.encounter_id, "t": ts}))
C = pd.concat(rows, ignore_index=True).merge(E[["encounter_id", "admit_time", "transfer_time", "age_band", "unit", "admission_source"]], on="encounter_id")
C["y"] = ((C.transfer_time > C.t) & (C.transfer_time <= C.t + pd.Timedelta(hours=12))).astype(int)
C["hours_in"] = (C.t - C.admit_time).dt.total_seconds() / 3600

VIT = ["heart_rate", "resp_rate", "systolic_bp", "temperature", "spo2"]
def build(C, vkey, lkey):
    """Attach the latest vitals and labs available at each checkpoint, by the given time columns."""
    C = C.sort_values("t")
    v = V.sort_values(vkey)[["encounter_id", vkey] + VIT]
    D = pd.merge_asof(C, v, left_on="t", right_on=vkey, by="encounter_id", direction="backward")
    prev = V.sort_values(vkey)[["encounter_id", vkey] + VIT].copy(); prev[vkey] = prev[vkey] + pd.Timedelta(hours=8)
    D = pd.merge_asof(D.sort_values("t"), prev.rename(columns={c: c + "_8h" for c in VIT}), left_on="t", right_on=vkey, by="encounter_id",
                      direction="backward", suffixes=("", "_p"))
    for c in VIT:
        D[c + "_chg"] = D[c] - D[c + "_8h"]
    for test in ("Lactate", "WBC"):
        l = L[L.test == test].sort_values(lkey)[["encounter_id", lkey, "value"]].rename(columns={"value": test.lower(), lkey: lkey + "_" + test})
        D = pd.merge_asof(D.sort_values("t"), l, left_on="t", right_on=lkey + "_" + test, by="encounter_id", direction="backward")
    for c in ["age_band", "unit", "admission_source"]:
        D[c] = D[c].astype("category")
    return D
F = ["hours_in", "age_band", "unit", "admission_source", "lactate", "wbc"] + VIT + [c + "_chg" for c in VIT]
def ews(D):
    """Points-based early warning score in the style of NEWS, from the latest vitals."""
    s = np.zeros(len(D))
    s += np.select([D.resp_rate >= 25, D.resp_rate >= 21, D.resp_rate <= 8], [3, 2, 3], 0)
    s += np.select([D.spo2 <= 91, D.spo2 <= 93, D.spo2 <= 95], [3, 2, 1], 0)
    s += np.select([D.systolic_bp <= 90, D.systolic_bp <= 100, D.systolic_bp <= 110, D.systolic_bp >= 220], [3, 2, 1, 3], 0)
    s += np.select([D.heart_rate >= 131, D.heart_rate >= 111, D.heart_rate >= 91, D.heart_rate <= 40], [3, 2, 1, 3], 0)
    s += np.select([D.temperature >= 39.1, D.temperature >= 38.1, D.temperature <= 35.0], [2, 1, 3], 0)
    return s

def fit_eval(D, label):
    tr, te = D[D.t < "2025-01-01"], D[D.t >= "2025-01-01"]
    m = HistGradientBoostingClassifier(random_state=42, categorical_features="from_dtype", max_iter=250, learning_rate=.06).fit(tr[F], tr.y)
    p = m.predict_proba(te[F])[:, 1]
    A[label] = {"auc": round(roc_auc_score(te.y, p), 3), "prauc": round(average_precision_score(te.y, p), 3)}
    return te.assign(p=p)

D = build(C, "entered_time", "resulted_time")
A["checkpoints"] = len(D); A["positive_rate_pct"] = round(100 * D.y.mean(), 2)
A["train_n"], A["test_n"] = int((D.t < "2025-01-01").sum()), int((D.t >= "2025-01-01").sum())
te = fit_eval(D, "model")
e = ews(te); A["ews_baseline"] = {"auc": round(roc_auc_score(te.y, e), 3), "prauc": round(average_precision_score(te.y, e), 3)}
# operating point: the threshold that flags half of the checkpoints that precede a transfer
thr = np.quantile(te.p[te.y == 1], .5)
alerts = te.p >= thr
pdays = len(te) * 4 / 24
A["alerts_per_100_patient_days"] = round(100 * alerts.sum() / pdays, 1)
A["alert_precision_pct"] = round(100 * te.y[alerts].mean(), 1)
first = te[alerts & (te.y == 1)].groupby("encounter_id").t.min()
lead = (te.drop_duplicates("encounter_id").set_index("encounter_id").transfer_time.reindex(first.index) - first).dt.total_seconds() / 3600
A["median_lead_hours"] = round(lead.median(), 1)
A["auc_by_age"] = {k: round(roc_auc_score(g.y, g.p), 3) for k, g in te.groupby("age_band", observed=True) if g.y.nunique() == 2}
# leakage: time stamps of when things happened rather than when they were known
te_leak = fit_eval(build(C, "recorded_time", "collected_time"), "leaky_model")
json.dump(A, open("answers.json", "w"), indent=1, default=str)
print(json.dumps(A, indent=1, default=str))
