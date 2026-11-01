"""Reference solution: Store Program Impact Evaluation.

Run from the folder holding the four data files. Needs pandas and numpy.
Prints every figure in the answer key and writes answers.json.
"""
import json
import numpy as np
import pandas as pd

D = pd.read_csv("daily_sales.csv.gz", parse_dates=["date"]); S = pd.read_csv("stores.csv.gz")
R = pd.read_csv("remodels.csv.gz", parse_dates=["closed_from", "reopened_on"])
A = {"rows": len(D), "stores": len(S), "remodeled": len(R)}
W = D.assign(week=D.date - pd.to_timedelta(D.date.dt.dayofweek, "D")).groupby(["store_id", "week"]).agg(sales=("sales_usd", "sum"), days=("date", "nunique")).reset_index()
W = W.merge(S, on="store_id").merge(R, on="store_id", how="left")
W["treated"] = W.reopened_on.notna()
W["closure_week"] = W.treated & (W.week + pd.Timedelta(days=6) >= W.closed_from) & (W.week < W.reopened_on)
W["post"] = W.treated & (W.week >= W.reopened_on)
A["closure_store_weeks"] = int(W.closure_week.sum())
# naive 1: treated stores, the 12 weeks before vs the 12 weeks after
def window(g):
    pre = g[(g.week < g.closed_from) & (g.week >= g.closed_from - pd.Timedelta(weeks=12))].sales.mean()
    post_all = g[(g.week >= g.closed_from) & (g.week < g.closed_from + pd.Timedelta(weeks=12))].sales.mean()
    post = g[(g.week >= g.reopened_on) & (g.week < g.reopened_on + pd.Timedelta(weeks=12))].sales.mean()
    return pd.Series({"incl_closure": post_all / pre - 1, "excl_closure": post / pre - 1})
bw = W[W.treated].groupby("store_id").apply(window, include_groups=False)
A["before_after_incl_closure_pct"] = round(100 * bw.incl_closure.mean(), 1)
A["before_after_excl_closure_pct"] = round(100 * bw.excl_closure.mean(), 1)
# naive 2: treated vs untreated, after July 2024
late = W[W.week >= "2024-10-07"]
A["treated_vs_control_level_pct"] = round(100 * (late[late.treated].sales.mean() / late[~late.treated].sales.mean() - 1), 1)
# regressions on log weekly sales, full weeks only, closure weeks dropped
X = W[(W.days == 7) & ~W.closure_week].copy(); X["y"] = np.log(X.sales)
def did(X, store_trends=False, region_weeks=False):
    """Two-way fixed effects on log sales: store and week (or region-week) effects, optional store-specific linear trends."""
    st = X.store_id.values
    wk = (X.region + "_" + X.week.astype(str)).values if region_weeks else X.week.astype(str).values
    t = (X.week - X.week.min()).dt.days.values / 365.25
    def demean(v):
        v = v.astype(float).copy()
        for _ in range(60):
            v -= pd.Series(v).groupby(st).transform("mean").values
            v -= pd.Series(v).groupby(wk).transform("mean").values
            if store_trends:
                df = pd.DataFrame({"v": v, "t": t, "s": st}); tm = df.groupby("s").t.transform("mean")
                slope = (df.v * (df.t - tm)).groupby(df.s).transform("sum") / ((df.t - tm) ** 2).groupby(df.s).transform("sum")
                v = v - slope.values * (t - tm.values)
        return v
    yd, pd_ = demean(X.y.values), demean(X.post.astype(float).values)
    b = (yd * pd_).sum() / (pd_ ** 2).sum()
    return round(100 * (np.exp(b) - 1), 2)
A["did_store_week_fe_pct"] = did(X)
A["did_plus_store_trends_pct"] = did(X, store_trends=True)
A["did_plus_region_week_fe_pct"] = did(X, region_weeks=True)
A["did_both_pct"] = did(X, store_trends=True, region_weeks=True)
A["true_effect_pct"] = 3.0
# event study: leads and lags relative to reopening, store and week fixed effects
# pre-trend check: growth from Jan-Feb 2023 to Jan-Feb 2024, before any remodel began
def growth(g):
    a = g[(g.week >= "2023-01-02") & (g.week < "2023-03-01")].sales.mean(); b = g[(g.week >= "2024-01-01") & (g.week < "2024-03-01")].sales.mean()
    return b / a - 1
gr = W.groupby(["store_id", "treated"]).apply(growth, include_groups=False).reset_index(name="g")
A["pre_period_growth_pct"] = {"remodeled": round(100 * gr[gr.treated].g.mean(), 1), "not_remodeled": round(100 * gr[~gr.treated].g.mean(), 1)}
json.dump(A, open("answers.json", "w"), indent=1, default=str)
print(json.dumps(A, indent=1, default=str))
