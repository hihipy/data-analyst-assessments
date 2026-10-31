# Answer Key: Hospital Length of Stay and Readmissions

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Medium, spreadsheet track | 90 minutes |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs. All data is synthetic.

## What This Assessment Measures

Lookups across sheets, date arithmetic, an observation window that must be complete, a self-join to find readmissions, and turning stays into daily occupancy.

## Expected Results

### Part 1: Data Problems

| Problem | Rows | Correct Handling |
| --- | ---: | --- |
| Exact duplicate admissions | 18 | Remove |
| Discharge date before admit date | 12 | Exclude and flag |
| Unit "6 South" not on the `Units` sheet | 35 | Keep in length of stay and readmissions; leave out of occupancy, since it has no bed count |
| Still in hospital on December 31 (blank discharge) | 81 | Leave out of length of stay; count their days in occupancy |

Stays that began in December 2024 are not in the file, so January occupancy reads low. A strong answer says so rather than reporting a January dip.

### Part 2: Length of Stay

Overall average: 4.39 days.

| Diagnosis Group | Average Length of Stay | O/E |
| --- | ---: | ---: |
| COPD | 4.12 | 1.11 |
| Heart Failure | 4.84 | 1.13 |
| Hip Replacement | 2.58 | 1.03 |
| Kidney Infection | 3.43 | 1.04 |
| Pneumonia | 4.12 | 1.03 |
| Sepsis | 6.12 | 1.02 |
| Stroke | 5.46 | 1.19 |

Stroke (1.19) and Heart Failure (1.13) run longest against benchmark. By unit, 5 North averages 5.05 days, the longest outside the ICU.

### Part 3: Readmissions

Eligible discharges are those from January 1 to November 30, 2025, excluding deaths and transfers out: 4,793. Of those, 836 were readmitted within 30 days, a rate of **17.4 percent**.

Counting every discharge, including December, deaths, and transfers, gives 14.5 percent. December discharges have not had 30 days to be readmitted, so including them understates the rate.

By diagnosis (percent): COPD 20.4, Heart Failure 24.1, Hip Replacement 5.6, Kidney Infection 14.9, Pneumonia 15.2, Sepsis 21.0, Stroke 14.8. By disposition (percent): AMA 28.5, Home 16.1, Home Health 17.7, Skilled Nursing 18.4. Patients who left against medical advice come back most often.

### Part 4: Occupancy

Annual occupancy (percent): 3 East 84.3, 3 West 83.6, 4 East 86.4, 4 West 86.1, 5 North 90.9, ICU 87.0. Every unit runs above 85 percent in several months; 5 North is above 85 percent from June through December and passes 100 percent in August, September, and December, which means patients waiting in overflow beds.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Data checks | 15 | Finds the duplicates, impossible dates, the unknown unit, and the stays still open on December 31. |
| Length of stay | 15 | Same-day stays counted as 1 day, open stays excluded, and O/E ratios matching the key. |
| Readmissions | 25 | Discharges limited to January through November, deaths and transfers out of the denominator, elective returns excluded; rate near 17.4 percent. |
| Occupancy | 20 | Patient days counted as midnights, open stays carried to year end, and units over 85 percent identified by month. |
| Recommendations | 15 | Two recommendations tied to numbers, for example 5 North's occupancy or the readmission rate after discharges against medical advice. |
| Workbook clarity and AI transparency | 10 | Formulas traceable. An AI log, if used, at the Strong level. |

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
| Including December discharges | Readmission rate understated | Did not think about the observation window |
| Keeping deaths and transfers in the denominator | Readmission rate understated | Ignored a written definition |
| Counting elective returns as readmissions | Rate overstated | Did not apply the non-elective rule |
| Reporting a January occupancy dip as real | A false finding | Did not notice stays from 2024 are missing |
| Dividing patient days by 365 for every unit and month | Monthly occupancy wrong | Used the wrong days-in-month |

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

1. How did you match each discharge to a later admission?
2. Why does January occupancy look low?
3. 5 North is over 100 percent in some months. What does that mean on the ward?
