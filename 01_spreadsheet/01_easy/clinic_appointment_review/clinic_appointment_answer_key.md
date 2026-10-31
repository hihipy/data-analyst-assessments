# Answer Key: Clinic Appointment Review

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Easy, spreadsheet track | 45 minutes |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs. All data is synthetic.

## What This Assessment Measures

Filtering by status before counting revenue, choosing the right denominator for a rate, deriving lead time from two dates, and noticing a gap in the data.

## Expected Results

### The Traps

Only completed visits earn a fee. Completed revenue is $517,485.00; summing every row gives $653,555.00, which counts 473 no-shows and 310 cancellations as paid visits.

Cancellations are not no-shows. The no-show rate is 13.6 percent of completed plus no-show appointments. Dividing by every row gives 12.5 percent.

Riverside has no appointments from March 10 to March 21, 2025. Its March revenue dip is a closure, not a demand problem, and a good answer notices the missing days.

### Part 1: Calculations

Completed-visit revenue by month and clinic:

| Month | Harbor | Northside | Riverside | Westgate |
| --- | ---: | ---: | ---: | ---: |
| January | $17,975.00 | $24,640.00 | $23,880.00 | $21,595.00 |
| February | $17,390.00 | $24,550.00 | $20,945.00 | $21,445.00 |
| March | $16,945.00 | $26,680.00 | $9,940.00 | $19,970.00 |
| April | $22,200.00 | $25,180.00 | $22,595.00 | $22,120.00 |
| May | $17,440.00 | $27,545.00 | $19,205.00 | $25,910.00 |
| June | $20,065.00 | $25,855.00 | $20,640.00 | $22,775.00 |

No-show rate by clinic (percent): Harbor 11.1, Northside 12.7, Riverside 13.2, Westgate 16.8.

No-show rate by department (percent): Cardiology 15.3, Dermatology 12.9, Pediatrics 14.4, Primary Care 12.7.

No-show rate by lead time (percent): 0 to 7 days 8.8, 8 to 30 days 12.8, 31 days or more 25.6.

### Part 2: What a Good Answer Says

- **Lead time is the strongest driver.** Appointments booked more than a month out are no-shows at nearly three times the rate of those booked within a week.
- **Westgate is the concern.** Its no-show rate of 16.8 percent is the highest, driven by new patients: 24.8 percent for new against 10.3 percent for returning.
- **New patients miss more everywhere,** 15.6 to 24.8 percent against about 10 percent for returning patients.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Status filtering | 25 | Revenue from completed visits only, and cancellations kept out of the no-show rate. |
| Calculations | 25 | Monthly revenue by clinic, no-show rates by clinic, department, and lead time matching the key. |
| Analysis | 20 | Names lead time as the strongest driver, flags Westgate's new patients, and explains Riverside's March dip as a closure. |
| Chart and summary | 20 | A correct monthly chart by clinic and a one-page summary a manager could act on. |
| Workbook clarity and AI transparency | 10 | Formulas or pivots traceable in the workbook. An AI log, if used, at the Strong level. |

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
| Summing fees on every row | Revenue overstated by $136,070 | Did not read the status column; the key trap |
| Dividing no-shows by all appointments | No-show rate understated | Used the wrong denominator |
| Calling Riverside's March a slump | A false operational finding | Did not check for missing days |
| Reporting rates without lead time | Misses the main lever | Stopped at the obvious cuts |

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

1. Why did you leave cancellations out of the no-show rate?
2. What would you test first to bring Westgate's new-patient no-shows down?
3. How did you notice Riverside was closed in March?
