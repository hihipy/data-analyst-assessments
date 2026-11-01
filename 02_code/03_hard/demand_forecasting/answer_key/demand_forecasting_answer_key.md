# Answer Key: Warehouse Demand Forecasting

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Hard, code track | 4 hours |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs. All data is synthetic.

## What This Assessment Measures

Time-series forecasting at scale: censored demand, known future events, product lifecycles, rolling-origin backtesting, and translating error into planning guidance.

## Expected Results

`reference_solution.py` and `future_actuals.csv.gz`, both kept with this key, score any `forecast.csv` against what customers actually wanted in the eight forecast weeks.

### Section A: Data Problems

- **Stockouts.** On 13.9 percent of product-warehouse days, the warehouse sold everything it had, so sales understate demand. Those days must be treated as censored.
- **Partial weeks.** 192 product-warehouse weeks have fewer than seven days of data: product launches, and warehouse W4, closed March 4 to 17, 2024.
- **Launches and discontinuations.** 25 products launched in the last year with short histories, and 10 products are discontinued and should be forecast at zero.
- **Planned promotions** in the forecast weeks are known in advance and should be used.

### Results on the Eight Forecast Weeks

| Method | WAPE | Bias |
| --- | ---: | ---: |
| Same week last year | 31.3% | +3.4% |
| 8-week moving average | 24.1% | -0.9% |
| Gradient boosting trained on raw sales | 19.8% | -8.7% |
| Gradient boosting trained on stockout-corrected demand | 19.0% | +3.9% |

The reference model is a Poisson gradient-boosting model trained on rolling origins every four weeks from July 2023 to April 2025. Its features are recent averages, the same week last year, planned discount, weeks since launch, a discontinued flag, warehouse, and category.

WAPE by category for the corrected model (percent): Beverages 19.7, Frozen 18.2, Household 19.7, Personal Care 18.6, Snacks 19.2. Products launched in the last year: 20.0 percent.

### What a Good Answer Says

- **Training on raw sales underforecasts by about 9 percent.** That bias feeds straight into more stockouts. Correcting for stockouts removes most of it, at a small cost in overprediction.
- **A strong baseline matters.** The 8-week moving average is a solid benchmark; same week last year is worse because promotions move from year to year.
- **Discontinued products must be forecast at zero,** and planned promotions must be used, or the forecast misses known changes.
- **Safety stock should be sized from the backtest error,** not from the forecast alone.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Data integrity | 20 | Detects stockouts as censored demand, handles partial weeks, launches, discontinuations, and the W4 closure. |
| Baselines | 10 | At least two sensible baselines, scored the same way as the model. |
| Model and backtest | 30 | Rolling-origin backtest, planned promotions used, WAPE near 19 percent, and bias reported. |
| Forecast file | 15 | `forecast.csv` complete for every week, warehouse, and product, with zeros for discontinued products. |
| Recommendation | 15 | Explains where the forecast is weakest and ties safety stock to backtest error. |
| Reproducibility and AI transparency | 10 | Code or notebook reruns end to end. An AI log, if used, at the Strong level. |

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
| Training on raw sales | Forecast about 9 percent low | Missed censored demand; the key trap |
| A single train-test split | Error estimate depends on one period | Weak evaluation habits |
| Ignoring planned promotions | Misses known demand spikes | Did not use available future information |
| Forecasting discontinued products | Phantom demand | Did not use the product file |
| Reporting MAPE | Blows up on low-volume series | Picked a metric that breaks on zeros |

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

1. How did you detect stockouts, and what did you do with those days?
2. How did your backtest choose its forecast dates?
3. How should planners turn your error into safety stock?
