# Answer Key: Specialist Referral Follow-Through

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Medium, code track | 2 hours |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs. All data is synthetic.

## What This Assessment Measures

Handling right-censored outcomes, joining capacity to demand by month, measuring access against targets, and separating a capacity problem from a behavior problem.

## Expected Results

### Part 1: Data Problems

| Problem | Rows | Correct Handling |
| --- | ---: | --- |
| Exact duplicate referrals | 9,000 | Remove |
| Urgency written "URGENT" or "routine" | 5,000 | Standardize |
| Appointment date before the referral date | 600 | Treat the appointment date as unknown and flag |
| Referring clinic "PC99" not in `clinics.csv.gz` | 1,200 | Keep for specialty results; flag for clinic results |

### Part 2: Follow-Through

Only referrals made at least 60 days before June 30, 2025 have had time to complete. On that basis, **69.8 percent** completed within 60 days. Including every referral gives 68.0 percent.

The monthly view shows why: the rate holds near 70 percent through April 2025, then falls to 60.8 percent for May and 27.3 percent for June. Those referrals are not failing; they have not had time.

By specialty (percent): Cardiology 72.6, Dermatology 63.0, Endocrinology 73.2, Gastroenterology 69.0, Neurology 65.9, Orthopedics 75.1.

### Part 3: Access and Leakage

| Specialty | Median Days, Routine (In Network) | Median Days, Urgent (In Network) | Within Target | Leakage |
| --- | ---: | ---: | ---: | ---: |
| Cardiology | 24 | 11 | 77.9% | 14.5% |
| Dermatology | 44 | 21 | 48.0% | 34.9% |
| Endocrinology | 24 | 11 | 79.8% | 14.2% |
| Gastroenterology | 30 | 14 | 67.4% | 18.9% |
| Neurology | 37 | 17 | 57.3% | 26.7% |
| Orthopedics | 20 | 9 | 86.4% | 10.4% |

Average monthly referrals per in-network slot in the first half of 2025: Cardiology 1.17, Dermatology 1.34, Endocrinology 1.1, Gastroenterology 1.15, Neurology 1.25, Orthopedics 1.05.

- **Dermatology** is short all the time: the longest in-network waits, under half seen within target, and the highest leakage.
- **Cardiology** is a new problem. Its in-network slots were cut through 2025, and leakage rose from 7.9 percent in the fourth quarter of 2024 to 29.2 percent in the second quarter of 2025.
- Leakage rises with the demand-to-slot ratio across specialties, so capacity, not referral habits, is the main driver.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Data checks | 15 | Finds the duplicates, urgency variants, impossible appointment dates, and the unknown clinic. |
| Follow-through | 25 | Limits the rate to referrals with 60 days of follow-up, and explains the drop at the end of the monthly series. |
| Access and leakage | 25 | In-network waits against targets, leakage by quarter, and the link between demand-to-slot ratios and leakage. |
| Recommendations | 25 | Dermatology and Cardiology named for different reasons, and a stated, checkable slot estimate. |
| Reproducibility and AI transparency | 10 | Code or notebook reruns from the files. An AI log, if used, at the Strong level. |

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
| Including recent referrals in the completion rate | May and June look like a collapse | Missed right-censoring; the key trap |
| Measuring waits across all visits | Out-of-network visits hide in-network delays | Mixed two populations |
| Blaming referring doctors for leakage | Wrong intervention | Did not compare demand with slots |
| Missing Cardiology's 2025 change | A new problem goes unseen | Looked only at full-period averages |

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

1. Why does completion fall so sharply for May and June 2025?
2. How did you estimate the extra Dermatology slots needed?
3. What would you check before telling Cardiology its slots were cut?
