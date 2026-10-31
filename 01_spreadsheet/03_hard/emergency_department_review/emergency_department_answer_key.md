# Answer Key: Emergency Department Throughput and Staffing

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Hard, spreadsheet track | 3 hours |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs. All data is synthetic.

## What This Assessment Measures

Cleaning timestamps, percentiles by group, spotting a daylight saving gap from a stated time zone, averaging per hour over the right number of days, and turning arrivals into a staffing plan.

## Expected Results

### Part 1: Data Problems

| Problem | Rows | Correct Handling |
| --- | ---: | --- |
| Exact duplicate visits | 150 | Remove |
| Provider time before arrival | 320 | Exclude from door-to-provider times and flag |
| Left without being seen, but with a provider time | 76 | Flag the contradiction; keep the visit as left without being seen |
| Triage written as "ESI 3" | 900 | Convert to the number |
| Arrivals between 2:00 and 3:00 on March 9, 2025 | 7 | That hour did not exist: clocks moved from 2:00 to 3:00 for daylight saving time. Flag as clock errors. |

### Part 2: Door to Provider

| Triage Level | Median (minutes) | 90th Percentile (minutes) |
| --- | ---: | ---: |
| 1 | 6 | 15 |
| 2 | 7 | 16 |
| 3 | 19 | 44 |
| 4 | 19 | 45 |
| 5 | 18 | 44 |

95.6 percent of patients were seen within the target for their triage level.

### Part 3: Patient Flow

Left without being seen: **5.8 percent** of visits, almost three times the 2 percent target. It peaks at 9:00, 18:00, and 22:00, the hours when arrivals outrun the schedule.

Median time in the ED (hours): Admitted 5.8, Discharged 2.42, Left Without Being Seen 1.08, Transferred 2.95.

Boarding, from admit decision to departure, has a median of 135 minutes overall, but about 210 to 225 minutes in January, February, and December, against 110 to 125 in other months. Winter boarding is a hospital bed problem, not an ED staffing problem.

### Part 4: Staffing

Average arrivals must be divided by the number of each weekday in 2025, not by 365 or by the number of days with arrivals. Mondays are busiest; the peak hour is Mon 17:00, with 7.9 arrivals on average.

Comparing providers needed with the schedule gives **67 provider-hours short per week**, spread over 66 weekday-hours. The 9:00, 16:00 to 19:00, and 22:00 hours are short on every day of the week, and Monday has the most short hours. Those are also the hours with the most patients leaving without being seen.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Data checks | 20 | Finds the duplicates, clock errors, contradictions, text triage values, and the arrivals in the hour that did not exist. |
| Door to provider | 15 | Medians and 90th percentiles by triage level, with bad intervals excluded. |
| Patient flow | 15 | Left-without-being-seen rate near 5.8 percent, time in ED by disposition, and the winter boarding pattern. |
| Staffing analysis | 25 | Arrivals averaged per weekday-hour over the count of each weekday, providers needed rounded up, and about 67 provider-hours short per week. |
| Memo | 15 | Leads with the staffing change, connects it to patients leaving without being seen, and separates boarding as a bed problem. |
| Workbook clarity and AI transparency | 10 | Formulas traceable on a large sheet. An AI log, if used, at the Strong level. |

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
| Averaging arrivals over 365 days or over days with data | Every hour's demand is wrong | Did not think about what the average is per |
| Missing the March 9 gap | Clock errors treated as real visits | Did not read the time zone note |
| Keeping negative intervals | Door-to-provider times pulled down | Did not check that times run in order |
| Rounding providers needed down | Understates the gap | Misread a capacity calculation |
| Proposing more ED staff to fix boarding | Money spent on the wrong problem | Did not separate ED flow from hospital beds |

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

1. Why can't there be arrivals at 2:30 on March 9?
2. How did you average arrivals for Mondays at 9:00?
3. If you could add only 20 provider-hours a week, where would they go?
