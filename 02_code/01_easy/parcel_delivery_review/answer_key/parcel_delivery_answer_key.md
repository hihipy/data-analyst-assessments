# Answer Key: Parcel Delivery Review

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Easy, code track | 60 minutes |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs. All data is synthetic.

## What This Assessment Measures

Reshaping an event log into one row per entity, handling time zones, excluding outcomes not yet observable, and locating where performance broke.

## Expected Results

### The Traps

- **Time zones.** Each `event_time` carries its hub's UTC offset, and promised dates are local to the destination. Comparing the local delivery date with the promised date gives **89.3 percent on time**. Converting every scan to UTC first gives 74.1 percent, because evening deliveries roll into the next UTC day.
- **Packages not yet due.** 13,822 packages have promised dates after September 30 and cannot be judged. Including them and counting them late gives 84.9 percent.
- **Duplicate scans.** 24,115 rows repeat an earlier scan.

### Part 1: Calculations

On time by service: Ground 89.3 percent, Express 89.1 percent, out of 238,178 packages due by September 30.

Median business days in transit: Ground 3, Express 2.

Packages with no delivery scan a week or more after their promised date: 875. Exceptions: 2.85 percent of packages.

Worst lanes with at least 500 packages (percent on time): DAL to MIA 73.6, DAL to SEA 80.1, DAL to DAL 80.6, DAL to CHI 80.6, CHI to DAL 80.8.

### Part 2: What a Good Answer Says

- **Dallas broke down in August.** Packages through Dallas were 60.3 percent on time in August, against 92.9 percent in July and 91.3 percent in September.
- **Miami had one bad week.** Packages to Miami shipped the week of September 1 were 12.8 percent on time, the pattern of a weather closure, and recovered within two weeks.
- **Outside those two events, the network runs at 92.7 percent on time,** so the overall number understates normal performance.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Data handling | 25 | Removes duplicate scans, compares local delivery dates with promised dates, and excludes packages not yet due. |
| Calculations | 25 | On-time rate near 89.3 percent, by service and lane, transit times, and missing deliveries. |
| Analysis | 25 | Finds Dallas in August and Miami in early September, and the 92.7 percent on-time rate outside them. |
| Communication | 15 | One page or 3 slides, a clear chart, and claims tied to numbers. |
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
| Converting delivery times to UTC dates | On-time rate drops to 74.1 percent | Did not think about time zones; the key trap |
| Counting packages not yet due as late | On-time rate drops to 84.9 percent | Did not handle the data cutoff |
| Counting scan rows instead of packages | Inflated volumes | Did not reshape the event log |

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

1. Why compare local dates rather than UTC?
2. How did you decide which packages could be judged?
3. What happened in Dallas in August?
