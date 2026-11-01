"""Reference solution: Warehouse Demand Forecasting.

Run from the folder holding the data files and future_actuals.csv.gz (kept with the answer key).
Needs pandas, numpy, and scikit-learn. Prints every figure in the answer key and writes answers.json.
"""
import json
import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor

O = "./"
D = pd.read_csv(O + "daily_sales.csv.gz", parse_dates=["date"])
SK = pd.read_csv(O + "skus.csv.gz", parse_dates=["launch_date", "discontinue_date"])
PR = pd.read_csv(O + "promotions.csv.gz", parse_dates=["start_date", "end_date"])
ACT = pd.read_csv(O + "future_actuals.csv.gz", parse_dates=["week_start"])
A = {"rows": len(D)}
ORIGIN = pd.Timestamp("2025-06-30")                       # first forecast week
FWEEKS = pd.date_range(ORIGIN, periods=8, freq="7D")

# stockouts: the day sold everything it started with, so demand is at least what was sold
D["stockout"] = (D.units_sold >= D.units_on_hand_start) & (D.units_on_hand_start >= 0)
A["stockout_days_pct"] = round(100 * D.stockout.mean(), 1)
dow_w = D[~D.stockout].groupby(D.date.dt.dayofweek).units_sold.mean(); dow_w = dow_w / dow_w.mean()
D["w"] = D.date.dt.dayofweek.map(dow_w)
D["week"] = D.date - pd.to_timedelta(D.date.dt.dayofweek, "D")
g = D.groupby(["week", "warehouse_id", "sku"])
Wk = pd.DataFrame({"sold": g.units_sold.sum(), "days": g.size(),
                   "instock_sold": g.apply(lambda x: x.loc[~x.stockout, "units_sold"].sum(), include_groups=False),
                   "instock_w": g.apply(lambda x: x.loc[~x.stockout, "w"].sum(), include_groups=False),
                   "all_w": g.w.sum()}).reset_index()
# estimated demand: scale in-stock days up to the full week by weekday weights
Wk["demand"] = np.where(Wk.instock_w > 0, Wk.instock_sold / Wk.instock_w * Wk.all_w * 7 / Wk.days.clip(lower=1) * Wk.days / 7, Wk.sold)
Wk = Wk[Wk.days == 7]                                     # drop partial weeks (closures, launches)
A["weeks_dropped_partial"] = int((g.size() < 7).sum())

def promo_disc(sku, week):
    p = PR[(PR.sku == sku) & (PR.start_date <= week + pd.Timedelta(days=6)) & (PR.end_date >= week)]
    return float(p.discount_pct.max()) if len(p) else 0.0
promo = {(r.sku, wk): 0.0 for r in SK.itertuples() for wk in []}
P2 = []
for p in PR.itertuples():
    for wk in pd.date_range(p.start_date - pd.to_timedelta(p.start_date.dayofweek, "D"), p.end_date, freq="7D"):
        P2.append((p.sku, wk, p.discount_pct))
PW = pd.DataFrame(P2, columns=["sku", "week", "disc"]).groupby(["sku", "week"]).disc.max()

def features(origin, target_col):
    hist = Wk[Wk.week < origin]
    piv = hist.pivot_table(index=["warehouse_id", "sku"], columns="week", values=target_col)
    cols = sorted(piv.columns)
    f = pd.DataFrame(index=piv.index)
    for n in (4, 8, 13):
        f[f"mean{n}"] = piv[cols[-n:]].mean(axis=1)
    rows = []
    for h in range(8):
        wk = origin + pd.Timedelta(weeks=h)
        x = f.copy(); x["h"] = h; x["week"] = wk; x["woy"] = wk.isocalendar().week
        ly = wk - pd.Timedelta(weeks=52)
        x["last_year"] = piv[ly] if ly in piv.columns else np.nan
        rows.append(x.reset_index())
    X = pd.concat(rows, ignore_index=True)
    X = X.merge(SK, on="sku", how="left")
    X["disc"] = [PW.get((s, w), 0.0) for s, w in zip(X.sku, X.week)]
    X["age_w"] = (X.week - X.launch_date).dt.days / 7
    X["gone"] = (X.discontinue_date.notna() & (X.discontinue_date <= X.week)).astype(int)
    for c in ["warehouse_id", "category"]:
        X[c] = X[c].astype("category")
    return X
F = ["mean4", "mean8", "mean13", "h", "woy", "last_year", "disc", "age_w", "gone", "warehouse_id", "category"]

def train(target_col):
    parts = []
    for origin in pd.date_range("2023-07-03", "2025-04-28", freq="28D"):
        X = features(origin, target_col)
        y = Wk.set_index(["week", "warehouse_id", "sku"])[target_col]
        X["y"] = [y.get((w, a, b), np.nan) for w, a, b in zip(X.week, X.warehouse_id, X.sku)]
        parts.append(X.dropna(subset=["y"]))
    T = pd.concat(parts, ignore_index=True)
    return HistGradientBoostingRegressor(loss="poisson", max_iter=300, learning_rate=.05, random_state=42, categorical_features="from_dtype").fit(T[F], T.y)

def score(fc, name):
    m = ACT.merge(fc, on=["week_start", "warehouse_id", "sku"], how="left").fillna({"forecast": 0})
    A[name] = {"wape_pct": round(100 * (m.forecast - m.actual_units).abs().sum() / m.actual_units.sum(), 1),
               "bias_pct": round(100 * (m.forecast - m.actual_units).sum() / m.actual_units.sum(), 1)}
    return m

Xf = features(ORIGIN, "demand")
score(Xf.assign(forecast=Xf.last_year.fillna(Xf.mean8), week_start=Xf.week)[["week_start", "warehouse_id", "sku", "forecast"]], "seasonal_naive")
score(Xf.assign(forecast=Xf.mean8, week_start=Xf.week)[["week_start", "warehouse_id", "sku", "forecast"]], "moving_average_8")
Xs = features(ORIGIN, "sold")
model_raw = train("sold")
score(Xs.assign(forecast=np.where(Xs.gone == 1, 0, model_raw.predict(Xs[F])), week_start=Xs.week)[["week_start", "warehouse_id", "sku", "forecast"]], "model_on_raw_sales")
model = train("demand")
pred = model.predict(Xf[F]); pred = np.where(Xf.gone == 1, 0, pred)
m = score(Xf.assign(forecast=pred, week_start=Xf.week)[["week_start", "warehouse_id", "sku", "forecast"]], "model_on_corrected_demand")
m = m.merge(SK[["sku", "category", "launch_date"]], on="sku")
A["wape_by_category"] = (m.groupby("category").apply(lambda g: (g.forecast - g.actual_units).abs().sum() / g.actual_units.sum() * 100, include_groups=False)).round(1).to_dict()
new = m.launch_date >= "2024-09-01"
A["wape_new_skus"] = round(100 * (m[new].forecast - m[new].actual_units).abs().sum() / m[new].actual_units.sum(), 1)
A["discontinued_skus"] = int(SK.discontinue_date.notna().sum())
json.dump(A, open("answers.json", "w"), indent=1, default=str)
print(json.dumps(A, indent=1, default=str))
