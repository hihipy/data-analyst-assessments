# Answer Key: Store Program Impact Evaluation

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Hard, code track | 4 hours |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs. All data is synthetic.

## What This Assessment Measures

Causal inference from observational data: selection bias, difference-in-differences with fixed effects, pre-trend checks, staggered rollout, and confounding events.

## Expected Results

`reference_solution.py`, kept with this key, reproduces every figure from the four data files. The data was simulated with a true remodel effect of **+3.0 percent** on sales.

### Section A: Data Problems

- **Remodel closures:** each remodeled store was closed for a week, 60 store-weeks of zero sales. Leave closure weeks out; they are not the effect of the remodel.
- **Selection:** remodeled stores grew 2.1 percent from early 2023 to early 2024, before any remodel, against -0.6 percent for other stores. Leaders picked stores that were already growing.
- **A regional campaign:** the South ran an advertising campaign in July and August 2024, and South stores are overrepresented among remodels.

### Sections B and C: Estimates

| Approach | Estimated Effect |
| --- | ---: |
| Before and after, including the closure week | -9.9% |
| Before and after, closure excluded | -1.6% |
| Remodeled versus other stores, after October 2024 | +10.6% |
| Difference-in-differences, store and week effects | +6.55% |
| Plus region-by-week effects | +6.62% |
| Plus store-specific trends | +2.8% |
| Both adjustments | **+2.67%** |

- **Before and after** mixes the remodel with seasonality; the 12 weeks after a spring or summer reopening are naturally different.
- **Remodeled versus other stores** compares bigger, faster-growing stores with the rest: a level difference, not an effect.
- **Plain difference-in-differences** doubles the true effect, because remodeled stores were already pulling ahead.
- **Store-specific trends** fix the selection problem. The region-by-week adjustment matters little here, but checking it is part of a careful answer.

### Section D: What a Good Recommendation Says

- The remodels raised sales about 3 percent, not the 6.6 percent from plain difference-in-differences or the 10.6 percent from comparing stores.
- Confidence rests on the trend adjustment; a strong answer says so plainly.
- For the next 100 stores, randomize the order, or at least the timing within region, so the effect can be measured without modeling around selection.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Data integrity | 15 | Drops closure weeks, and spots the campaign and the selection of remodeled stores. |
| Simple comparisons | 10 | Computes them and explains why each fails. |
| Design | 30 | Difference-in-differences with store and week effects, a pre-trend check, and adjustments for selection. |
| Estimate | 20 | A final estimate near 3 percent, with the path from the naive estimates explained. |
| Recommendation | 15 | Clear on the effect, the uncertainty, and how to roll out the next stores measurably. |
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
| Reporting plain difference-in-differences | An effect about twice the truth | Did not check pre-trends; the key trap |
| Keeping closure weeks | Before-and-after effect looks negative | Did not read the remodel file |
| Comparing remodeled with other stores directly | A level difference reported as an effect | Confused correlation with impact |
| No pre-trend check | Selection goes unseen | Weak causal habits |

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

1. How did you know the remodeled stores were different before their remodel?
2. Why does adding store trends change the estimate?
3. How would you choose the next 100 stores?
