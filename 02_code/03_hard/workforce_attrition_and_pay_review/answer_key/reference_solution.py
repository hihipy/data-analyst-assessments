"""Reference solution: Workforce Attrition and Pay Review.

Run from the folder holding the six data files. Needs pandas, numpy, and scikit-learn.
Prints every figure in answer_key.md and writes answers.json.
"""
import json, numpy as np, pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, average_precision_score

O = "./"  # folder holding the six data files
A = {}
SNAP = pd.Timestamp("2025-05-31")

# ---------------------------------------------------------------- employees
E = pd.read_csv(O + "employees.csv.gz", dtype=str, keep_default_na=False)
A["employees_rows_raw"] = len(E)
A["employees_exact_dups"] = int(E.duplicated().sum())
E = E.drop_duplicates()
E["employee_id"] = E.employee_id.str.upper().str.strip()
def parse_date(s):
    out = pd.to_datetime(s, format="%Y-%m-%d", errors="coerce")
    for fmt in ("%m/%d/%Y", "%d-%b-%Y"):
        out = out.fillna(pd.to_datetime(s.where(out.isna()), format=fmt, errors="coerce"))
    serial = s.str.fullmatch(r"\d{5}")
    out = out.where(~serial, pd.Timestamp("1899-12-30") + pd.to_timedelta(pd.to_numeric(s.where(serial), errors="coerce"), "D"))
    return out
E["hire_date"] = parse_date(E.hire_date)
E["termination_date"] = pd.to_datetime(E.termination_date.replace("", None), errors="coerce")
E["last_updated"] = pd.to_datetime(E.last_updated)
before = len(E)
E = E.sort_values("last_updated").drop_duplicates("employee_id", keep="last")
A["employees_after_exact_dedupe"] = before
A["employees_versions_resolved"] = before - len(E)
A["employees_unique"] = len(E)
E["education_level"] = E.education_level.replace({"HS": "High School", "BSc": "Bachelor's", "Masters": "Master's", "Ph.D.": "PhD"})
E["termination_reason"] = E.termination_reason.str.strip().str.capitalize().replace({"Termed": "Terminated"})
A["hire_unparsed"] = int(E.hire_date.isna().sum())
A["future_hires"] = int((E.hire_date > SNAP).sum())

# ---------------------------------------------------------------- locations and fx
LOC = pd.read_csv(O + "locations.csv.gz", dtype=str)
alias = {"USA": "United States of America", "U.S.": "United States of America", "United States": "United States of America",
         "UK": "United Kingdom", "U.K.": "United Kingdom", "England": "United Kingdom", "Deutschland": "Germany",
         "España": "Spain", "JAPAN": "Japan", "México": "Mexico", "Italia": "Italy"}
LOC["country"] = LOC.country.str.strip().replace(alias)
A["location_country_values_raw"] = int(pd.read_csv(O + "locations.csv.gz").country.nunique())
A["location_dup_city"] = LOC[LOC.duplicated(["city", "country"], keep=False)].location_id.tolist()
FX = pd.read_csv(O + "fx_rates.csv.gz")
FX["usd_per_unit"] = np.where(FX.quote_basis == "UNIT_PER_USD", 1 / FX.rate, FX.rate)
fx = FX.set_index(["month", "currency"]).usd_per_unit
def usd(amount, currency, month):
    r = pd.Series(list(zip([month] * len(currency), currency))).map(lambda k: 1.0 if k[1] == "USD" else fx.get(k, np.nan))
    return amount * r.values

# ---------------------------------------------------------------- job history
JH = pd.read_csv(O + "job_history.csv.gz", dtype=str, keep_default_na=False)
A["history_rows_raw"] = len(JH)
known = set(E.employee_id)
A["history_unknown_employee_rows"] = int((~JH.employee_id.isin(known)).sum())
JH = JH[JH.employee_id.isin(known)]
def parse_sal(s):
    k = s.str.endswith("k")
    v = pd.to_numeric(s.str.replace(",", "").str.rstrip("k"), errors="coerce")
    return np.where(k, v * 1000, v)
A["history_salary_text"] = int((~JH.base_salary.str.fullmatch(r"\d+(\.\d+)?")).sum())
JH["base_salary"] = parse_sal(JH.base_salary)
dmap = {"Human Resources": "HR", "R & D": "R&D", "Information Technology": "IT", "FIN": "Finance", "sales": "Sales", "Mktg": "Marketing", "Ops": "Operations"}
A["history_department_variants"] = int(JH.department.isin(dmap).sum())
JH["department"] = JH.department.replace(dmap)
JH["effective_date"] = pd.to_datetime(JH.effective_date)
JH["recorded_at"] = pd.to_datetime(JH.recorded_at)
n0 = len(JH)
JH = JH.sort_values("recorded_at").drop_duplicates(["employee_id", "effective_date"], keep="last")
A["history_same_day_resolved"] = n0 - len(JH)
orph = (JH.manager_id != "") & ~JH.manager_id.isin(known)
A["history_orphan_manager_rows"] = int(orph.sum())
JH.loc[orph, "manager_id"] = ""
JH["job_level"] = JH.job_level.astype(int)
JH = JH.sort_values(["employee_id", "effective_date"])

def state_asof(d):
    """Last job-history row on or before d for employees active on d."""
    act = E[(E.hire_date <= d) & (E.termination_date.isna() | (E.termination_date > d))]
    h = JH[(JH.effective_date <= d) & JH.employee_id.isin(act.employee_id)]
    st = h.groupby("employee_id").tail(1).merge(act, on="employee_id").merge(LOC[["location_id", "country"]], on="location_id")
    st["salary_usd"] = usd(st.base_salary.values, st.currency.values, d.strftime("%Y-%m"))
    return st

# ---------------------------------------------------------------- reviews and surveys
PR = pd.read_csv(O + "performance_reviews.csv.gz", dtype=str, keep_default_na=False)
A["reviews_rows_raw"] = len(PR)
PR["employee_id"] = PR.employee_id.str.upper()
PR["rating_n"] = pd.to_numeric(PR.rating, errors="coerce")
A["reviews_invalid_rating"] = int((~PR.rating_n.between(1, 5)).sum())
PR = PR[PR.rating_n.between(1, 5)]
PR["review_date"] = pd.to_datetime(PR.review_date)
n0 = len(PR)
PR = PR.sort_values("review_date").drop_duplicates(["employee_id", "review_year"], keep="last")
A["reviews_revisions_resolved"] = n0 - len(PR)
SV = pd.read_csv(O + "engagement_surveys.csv.gz", dtype=str)
A["surveys_rows_raw"] = len(SV)
A["surveys_exact_dups"] = int(SV.duplicated().sum())
SV = SV.drop_duplicates()
SV["score"] = pd.to_numeric(SV.engagement_score, errors="coerce")
A["surveys_sentinel"] = int((SV.score > 100).sum())
SV = SV[SV.score.between(0, 100)]
SV["survey_date"] = pd.to_datetime(SV.survey_date)

# ---------------------------------------------------------------- snapshot, metrics, pay
st = state_asof(SNAP)
A["active_headcount_snapshot"] = len(st)
A["headcount_by_country"] = st.country.value_counts().to_dict()
t12 = E[(E.termination_date > SNAP - pd.DateOffset(years=1)) & (E.termination_date <= SNAP)]
start_hc = len(state_asof(SNAP - pd.DateOffset(years=1)))
A["terminations_12m"] = len(t12); A["headcount_start_12m"] = start_hc
A["attrition_12m_pct"] = round(100 * len(t12) / start_hc, 1)
A["attrition_by_reason"] = t12.termination_reason.value_counts().to_dict()
A["median_salary_usd_by_country"] = st.groupby("country").salary_usd.median().round(0).to_dict()
g = st.groupby(["department", "job_title", "country"]).salary_usd
q1, q3 = g.transform(lambda x: x.quantile(.25)), g.transform(lambda x: x.quantile(.75))
st["hi_out"] = st.salary_usd > q3 + 1.5 * (q3 - q1)
A["salary_high_outliers"] = int(st.hi_out.sum())
A["top10_outliers"] = st[st.hi_out].nlargest(10, "salary_usd")[["employee_id", "department", "job_title", "country", "salary_usd"]].round(0).to_dict("records")
# naive: no currency conversion
st["naive"] = st.base_salary
A["naive_top_country_by_median_unconverted"] = st.groupby("country").naive.median().idxmax()

# hiring trend
hires = JH[(JH.event == "Hire") & (JH.effective_date >= "2023-06-01") & (JH.effective_date <= SNAP)]
ht = hires.assign(m=hires.effective_date.dt.to_period("M")).groupby(["m", "department"]).size().unstack(fill_value=0)
ht = ht.reindex(pd.period_range("2023-06", "2025-05", freq="M"), fill_value=0)
roll = ht.rolling(3, min_periods=1).mean().round(1)
A["hires_total_24m"] = int(ht.values.sum())
A["hires_may2025_by_dept"] = ht.loc[pd.Period("2025-05")].to_dict()
A["rolling_may2025_by_dept"] = roll.loc[pd.Period("2025-05")].to_dict()

# ---------------------------------------------------------------- model
def features(d):
    s = state_asof(d)
    s["tenure"] = (d - s.hire_date).dt.days / 365.25
    peer = s.groupby(["job_title", "country", "job_level"]).salary_usd.transform("median")
    s["compa"] = s.salary_usd / peer
    lp = JH[(JH.event.isin(["Promotion", "Hire"])) & (JH.effective_date <= d)].groupby("employee_id").effective_date.max()
    s["yrs_since_promo"] = (d - s.employee_id.map(lp)).dt.days / 365.25
    r = PR[PR.review_date <= d].sort_values("review_date").groupby("employee_id").rating_n.last()
    s["last_rating"] = s.employee_id.map(r)
    sv = SV[(SV.survey_date <= d) & (SV.survey_date > d - pd.DateOffset(years=1))].sort_values("survey_date").groupby("employee_id").score
    s["eng_last"] = s.employee_id.map(sv.last()); s["eng_missing"] = s.eng_last.isna().astype(int)
    s["eng_change"] = s.employee_id.map(sv.last() - sv.first())
    # manager's team attrition in the prior 12 months (as of d)
    left = E[(E.termination_date > d - pd.DateOffset(years=1)) & (E.termination_date <= d)].employee_id
    lastmgr = JH[JH.effective_date <= d].groupby("employee_id").manager_id.last()
    mt = pd.DataFrame({"mgr": lastmgr}).assign(left=lambda x: x.index.isin(left))
    rate = mt[mt.mgr != ""].groupby("mgr").left.mean()
    s["mgr_team_attr"] = s.manager_id.map(rate)
    nxt = d + pd.DateOffset(years=1)
    s["y"] = ((s.termination_date > d) & (s.termination_date <= nxt)).astype(int)
    for c in ["department", "country", "work_mode"]:
        s[c] = s[c].astype("category")
    return s
F = ["tenure", "job_level", "compa", "yrs_since_promo", "last_rating", "eng_last", "eng_missing", "eng_change", "mgr_team_attr",
     "department", "country", "work_mode"]
tr, te = features(pd.Timestamp("2023-05-31")), features(pd.Timestamp("2024-05-31"))
te["country"] = te.country.cat.set_categories(tr.country.cat.categories); te["department"] = te.department.cat.set_categories(tr.department.cat.categories)
te["work_mode"] = te.work_mode.cat.set_categories(tr.work_mode.cat.categories)
m = HistGradientBoostingClassifier(random_state=42, categorical_features="from_dtype", max_iter=300, learning_rate=.06).fit(tr[F], tr.y)
p = m.predict_proba(te[F])[:, 1]
A["model_train_n"], A["model_test_n"] = len(tr), len(te)
A["model_train_rate"], A["model_test_rate"] = round(tr.y.mean(), 4), round(te.y.mean(), 4)
A["model_auc"], A["model_prauc"] = round(roc_auc_score(te.y, p), 3), round(average_precision_score(te.y, p), 3)
base = LogisticRegression(max_iter=500).fit(tr[["tenure"]], tr.y).predict_proba(te[["tenure"]])[:, 1]
A["baseline_tenure_auc"], A["baseline_prauc"] = round(roc_auc_score(te.y, base), 3), round(average_precision_score(te.y, base), 3)
# leakage demo: latest survey and review regardless of date
r_all = PR.sort_values("review_date").groupby("employee_id").rating_n.last(); s_all = SV.sort_values("survey_date").groupby("employee_id").score.last()
for df in (tr, te):
    df["last_rating"] = df.employee_id.map(r_all); df["eng_last"] = df.employee_id.map(s_all)
    df["eng_missing"] = df.eng_last.isna().astype(int)
ml = HistGradientBoostingClassifier(random_state=42, categorical_features="from_dtype", max_iter=300, learning_rate=.06).fit(tr[F], tr.y)
A["leaky_auc"] = round(roc_auc_score(te.y, ml.predict_proba(te[F])[:, 1]), 3)
json.dump(A, open("answers.json", "w"), indent=1, default=str)
print(json.dumps(A, indent=1, default=str))
