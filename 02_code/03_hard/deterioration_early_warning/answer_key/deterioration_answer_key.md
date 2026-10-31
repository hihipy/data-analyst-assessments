# Answer Key: Inpatient Deterioration Early Warning

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Hard, code track | 4 hours |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs. All data is synthetic.

## What This Assessment Measures

Point-in-time feature building on irregular time series, the difference between when something happened and when it was known, unit cleanup, honest evaluation against a clinical baseline, and judging an alarm burden.

## Expected Results

`reference_solution.py`, kept with this key, reproduces every figure from the four data files.

### Section A: Data Problems

| Problem | Rows | Correct Handling |
| --- | ---: | --- |
| Duplicate vital-sign rows | 20,000 | Remove |
| Temperature recorded in Fahrenheit | 51,208 | Convert values over 45 to Celsius |
| Heart rate of 0 or 999 | 2,500 | Treat as missing |
| Lactate in mg/dL instead of mmol/L | 21,532 | Divide by 9.01 |
| Vitals taken after the ICU transfer | 43,618 | Never use; checkpoints stop at transfer |

### Section B: Features

Vitals must be matched on `entered_time` and labs on `resulted_time`: that is when a nurse could see them. About 10 percent of vitals are entered 3 to 9 hours late, and labs take 1 to 4 hours to result.

The feature table has 1,662,995 checkpoints, 0.38 percent of them within 12 hours of a transfer: 1,121,094 in 2024 for training and 541,901 in 2025 for testing.

### Sections C and D: Results (2025 Test Checkpoints)

| Model | ROC-AUC | PR-AUC |
| --- | ---: | ---: |
| Points-based early warning score | 0.74 | 0.017 |
| Gradient boosting, point-in-time features | 0.855 | 0.105 |
| Same model with leakage (`recorded_time` and `collected_time`) | 0.88 | 0.161 |

The reference score gives points for respiratory rate, oxygen saturation, systolic pressure, heart rate, and temperature, in the style of NEWS. Candidates' thresholds will differ, and a score near 0.74 is typical.

At the threshold that flags half of the checkpoints preceding a transfer: **33.0 alerts per 100 patient days**, 3.4 percent of alerts followed by a transfer within 12 hours, and a median of 7.0 hours of warning. On a 30-bed ward that is about 10 alerts a day, and about 1 in 30 is followed by a transfer.

By age band (ROC-AUC): 18-44 0.839, 45-64 0.849, 65-79 0.87, 80+ 0.859. Performance is similar across groups.

### Section E: What a Good Recommendation Says

- The model beats the simple score, mainly because lactate and changes in vitals add signal.
- The alarm burden is the real decision. Thirty-odd alerts per 100 patient days with about 1 in 30 real needs nursing input before go-live.
- A silent pilot comes first: score patients without alerting, and compare against real outcomes.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Data integrity | 20 | Removes duplicates, converts Fahrenheit and mg/dL, treats impossible heart rates as missing, and drops vitals taken after transfer. |
| Point-in-time features | 25 | Matches vitals on `entered_time` and labs on `resulted_time`, stops checkpoints at transfer, and explains why. |
| Baseline and model | 20 | A justified points-based score, a model near ROC-AUC 0.85 against it, and the 2024 to 2025 split. |
| Operating point | 15 | Alerts per 100 patient days, precision, and warning time at the stated threshold, translated into alerts per shift. |
| Recommendation | 10 | A clear position on a pilot, grounded in the alarm burden, with conditions for go-live. |
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
| Matching on `recorded_time` and `collected_time` | ROC-AUC near 0.88 that will not hold in practice | Leakage; the central trap |
| Keeping checkpoints after the transfer | The model learns from ICU vitals | Did not define the population at risk |
| Leaving Fahrenheit temperatures in | Fever looks extreme in 3 percent of rows | Did not profile values |
| Reporting ROC-AUC only | Hides a 3 percent alert precision | Ignored a rare outcome |
| No baseline | No way to tell if the model adds value | Weak evaluation habits |

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

1. Which timestamp did you use for labs, and why?
2. How many alerts per 12-hour shift would a 30-bed ward get?
3. What would you need to see in a silent pilot before turning alerts on?
