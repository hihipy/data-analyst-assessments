# Answer Key: Card Fraud Detection

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Hard, code track | 4 hours |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs. All data is synthetic.

## What This Assessment Measures

Rare-event detection with delayed labels: label maturity, point-in-time features from each card's history, capacity-based evaluation, and honest monitoring.

## Expected Results

`reference_solution.py`, kept with this key, reproduces every figure from the three data files.

### Section A: Labels

Chargebacks arrive a median of about three weeks after the transaction and can take two months. Reported fraud per 10,000 transactions holds between about 38 and 52 through August, then falls to 15.8 in September. September fraud has not been reported yet. Training or testing on it treats unreported fraud as legitimate.

A safe design trains on January to May and tests on June, whose chargebacks have had three months to arrive.

### Section B: Features

The reference features use only each card's own earlier transactions: amount against the card's median, minutes since its last transaction, transactions in the last hour, small test charges in the last hour, a new device, a foreign country, and a change of country. Anything from the chargeback file other than the label leaks the answer.

### Section C: Results (June 2025)

| Approach | Reviewed | Precision | Recall |
| --- | ---: | ---: | ---: |
| Rule: amount over $1,000, or foreign and online | 3,604 | 5.2% | 32.1% |
| Reference model, top 50 a day | 1,500 | 36.2% | 93.3% |

The model's PR-AUC is 0.842, and the top 50 a day catch 92.8 percent of June's fraud dollars. Scoring September the same way shows only 13.9 percent precision against chargebacks reported so far; the true figure, once labels mature, is close to June's. That gap is the label delay, not a model failure.

### Section D: What a Good Recommendation Says

- The score finds most fraud within the review capacity. Fraud in this data arrives in bursts of online purchases, often from a new device or after small test charges, which the card-history features capture.
- It misses fraud that looks like the cardholder's normal spending.
- Monitor it on labels at least 60 days old, and watch the alert mix weekly in the meantime.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Labels | 20 | Shows the chargeback delay, and tests only on months with mature labels. |
| Features | 25 | Uses only each card's past, with no leakage from the chargeback file. |
| Model and evaluation | 25 | Beats the rule, and reports precision, recall, and dollars caught at 50 a day. |
| Recommendation | 20 | Explains what the model catches and misses, and how to monitor with delayed labels. |
| Reproducibility and AI transparency | 10 | Code or notebook reruns. An AI log, if used, at the Strong level. |

## Score Bands

| Score | Reading |
| ---: | --- |
| 85 to 100 | Strong. Catches the traps, gets the numbers right, and explains the reasoning clearly. |
| 70 to 84 | Solid. Most numbers right, with one trap missed or one section thin. |
| 50 to 69 | Mixed. The mechanics work, but the judgment calls are weak or a major trap is missed. |
| Below 50 | Below the bar for this level. |

Weigh any single failure that would mislead a decision-maker more heavily than its points suggest. Reporting the inflated growth figure as real is one example.

## Common Mistakes

| Mistake | Effect | What It Usually Means |
| --- | --- | --- |
| Testing on September | Precision looks like 14 percent instead of about 36 | Ignored label delay; the key trap |
| Random train-test split | Future transactions leak into training | Ignored time order |
| Reporting accuracy or ROC-AUC only | Hides performance on rare fraud | Wrong metric for the decision |
| Features computed over the whole card history | Uses the future | Leakage |

## Evaluating AI Use

Candidates may use AI tools and must log them. Using AI is not penalized. Score the AI criterion on transparency and verification, not on whether AI was used.

| Level | What It Looks Like |
| --- | --- |
| Strong | Names each tool and the parts it touched. Shows real prompts, not summaries of them. Shows how the numbers were confirmed, for example a recomputed total, a row-count check, or a hand-checked case. Notes at least one AI suggestion that was wrong or rejected, and why. |
| Adequate | Lists tools and some prompts, but the verification is thin or generic ("I reviewed the output"). |
| Weak | No log despite clear signs of AI output, or reported numbers that cannot be traced to the submitted work. |

A candidate who used no AI scores this criterion on reproducibility alone: can a reviewer rerun or follow the work and get the same numbers?

Signs of unverified AI output:

- Figures that do not match the data, especially round or plausible-looking numbers with no calculation behind them.
- Code that references columns, sheets, or files that do not exist.
- Industry benchmarks or statistics cited with no source.
- Recommendations that would fit any company and are not tied to a number from this data.

## Follow-Up Interview Questions

1. Why can't you trust September's labels?
2. How did you make sure each feature used only the past?
3. What would you monitor weekly before labels arrive?
