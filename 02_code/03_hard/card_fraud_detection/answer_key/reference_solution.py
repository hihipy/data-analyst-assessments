"""Reference solution: Card Fraud Detection.

Run from the folder holding the three data files. Needs pandas, numpy, and scikit-learn.
Prints every figure in the answer key and writes answers.json.
"""
import json
import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import average_precision_score

T = pd.read_csv("transactions.csv.gz", parse_dates=["txn_time"]); C = pd.read_csv("cards.csv.gz"); CB = pd.read_csv("chargebacks.csv.gz", parse_dates=["reported_date"])
A = {"rows": len(T), "chargebacks": len(CB)}
T = T.merge(C[["card_id", "home_country"]], on="card_id").sort_values(["card_id", "txn_time"]).reset_index(drop=True)
T["y"] = T.txn_id.isin(CB.txn_id).astype(int)
T["month"] = T.txn_time.dt.to_period("M").astype(str)
A["reported_fraud_rate_by_month_bp"] = (T.groupby("month").y.mean() * 10000).round(1).to_dict()
# features from each card's own past only
g = T.groupby("card_id")
T["prev_gap_min"] = g.txn_time.diff().dt.total_seconds() / 60
T["card_txn_no"] = g.cumcount()
T["amt_vs_card_median"] = T.amount_usd / g.amount_usd.transform(lambda s: s.shift().expanding().median()).fillna(T.amount_usd.median())
T["foreign"] = (T.country != T.home_country).astype(int)
T["country_change"] = (T.country != g.country.shift()).astype(int) & T.card_txn_no.gt(0)
T["new_device"] = ((T.channel == "Online") & ~T.duplicated(["card_id", "device_id"])).astype(int)
small = (T.amount_usd < 5).astype(int)
roll = T.set_index("txn_time").groupby("card_id")
T["txns_last_hour"] = roll.amount_usd.rolling("60min").count().values - 1
T["small_last_hour"] = pd.Series(small.values, index=T.txn_time).groupby(T.card_id.values).rolling("60min").sum().values - small.values
T["online"] = (T.channel == "Online").astype(int)
T["cat"] = T.merchant_category.astype("category")
F = ["amount_usd", "prev_gap_min", "card_txn_no", "amt_vs_card_median", "foreign", "country_change", "new_device", "txns_last_hour", "small_last_hour", "online", "cat"]
train = T[T.txn_time < "2025-06-01"]; valid = T[(T.txn_time >= "2025-06-01") & (T.txn_time < "2025-07-01")]
m = HistGradientBoostingClassifier(random_state=42, max_iter=300, learning_rate=.06, categorical_features="from_dtype").fit(train[F], train.y)
valid = valid.assign(p=m.predict_proba(valid[F])[:, 1])
cap = 50 * valid.txn_time.dt.date.nunique()
top = valid.nlargest(cap, "p")
A["june"] = {"transactions": len(valid), "fraud": int(valid.y.sum()), "review_capacity": cap, "precision_at_capacity_pct": round(100 * top.y.mean(), 1),
             "recall_at_capacity_pct": round(100 * top.y.sum() / valid.y.sum(), 1), "pr_auc": round(average_precision_score(valid.y, valid.p), 3),
             "fraud_dollars_caught_pct": round(100 * top[top.y == 1].amount_usd.sum() / valid[valid.y == 1].amount_usd.sum(), 1)}
rule = valid[(valid.amount_usd > 1000) | ((valid.foreign == 1) & (valid.online == 1))]
A["rule_baseline"] = {"flagged": len(rule), "precision_pct": round(100 * rule.y.mean(), 1), "recall_pct": round(100 * rule.y.sum() / valid.y.sum(), 1)}
sep = T[T.month == "2025-09"].assign(p=lambda d: m.predict_proba(d[F])[:, 1])
topS = sep.nlargest(50 * sep.txn_time.dt.date.nunique(), "p")
A["september_reported_precision_pct"] = round(100 * topS.y.mean(), 1)   # chargebacks for September are mostly not in yet
json.dump(A, open("answers.json", "w"), indent=1, default=str); print(json.dumps(A, indent=1, default=str))
