# Answer Key: Workforce Attrition and Pay Review

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Hard, code track | 4 hours |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs.

`reference_solution.py`, kept with this key, reproduces every figure from the six data files. The exchange rates in `fx_rates.csv.gz` are synthetic.

## What This Assessment Measures

Point-in-time joins across effective-dated files, version resolution by timestamp, currency conversion with mixed quote conventions, honest leakage control in a predictive model, and clear communication of sensitive people data.

## Expected Results

Hard level: the difficulty is in point-in-time joins across files. Most mistakes come from reading a row that was not yet true on the date being analyzed, or from a currency that was never converted.

### The Files

| File | Rows | Grain |
| --- | ---: | --- |
| `employees.csv.gz` | 306,500 | One row per employee record; 300,000 real employees |
| `job_history.csv.gz` | 1,653,941 | One row per job event, effective-dated |
| `performance_reviews.csv.gz` | 1,313,942 | One row per annual review |
| `engagement_surveys.csv.gz` | 1,842,943 | One row per survey response |
| `locations.csv.gz` | 121 | One row per location |
| `fx_rates.csv.gz` | 1,288 | One row per currency per month |

### Section A: Data Problems

| Problem | Rows | Correct Handling |
| --- | ---: | --- |
| Exact duplicate employee rows | 4,500 | Remove |
| Stale employee versions, each wrongly showing a 2025 resignation | 2,000 | Keep the latest `last_updated`. Keeping the stale row overstates 2025 attrition. |
| Employee IDs in lowercase | 1,200 | Uppercase before deduplicating and joining |
| Hire dates as MM/DD/YYYY, DD-Mon-YYYY, and spreadsheet serial dates | 6,000; 3,000; 1,500 | Parse all three; none should be left unparsed |
| Name order "Last, First" | 3,000 | Parse both orders |
| Education and termination reason variants | 4,000; 2,500 | Map to the standard values |
| Hired after the snapshot date | 5,470 | Exclude from every snapshot and metric |
| Country aliases and trailing spaces in `locations.csv.gz` | 28 distinct raw values for 12 countries | Map to 12 countries |
| One city under two IDs | L101 and L999 (New York City) | Treat as one location |
| `fx_rates.csv.gz` quoted two ways | JPY, MXN, INR, and BRL are units per US dollar | Invert those rates. Without that, Japan comes out the best-paid country. |
| Same-day job history corrections | 9,029 | Keep the later `recorded_at` |
| Salaries as text ("85k", "85,000") | 6,000 | Parse to numbers |
| Department name variants | 7,000 | Map to the 7 departments |
| Manager IDs not in `employees.csv.gz` | 4,965 | Treat as unknown manager |
| Job history rows for unknown employees | 800 | Exclude |
| Invalid ratings (0, 6, N/A, blank) | 2,500 | Exclude; "4.0" style ratings are safe to coerce |
| Revised reviews (same employee and year) | 2,990 | Keep the later `review_date` |
| Survey duplicates and the 999 sentinel | 6,000; 3,000 | Remove duplicates; treat 999 as missing |

The snapshot has **174,051 active employees** on May 31, 2025. Each employee's job, pay, and manager come from their last `job_history` row dated on or before that day, and pay converts at May 2025 rates.

### Section B: Workforce Metrics (May 31, 2025)

Attrition over the prior 12 months: 13,933 terminations against 166,158 active on May 31, 2024, or **8.4 percent**. By reason: Resigned 8,114, Terminated 2,981, Retired 2,838.

| Country | Active Headcount | Median Pay (USD) |
| --- | ---: | ---: |
| United States of America | 45,243 | $86,400 |
| United Kingdom | 17,433 | $71,466 |
| India | 17,374 | $19,145 |
| Canada | 13,896 | $70,140 |
| Germany | 12,153 | $72,751 |
| Australia | 10,673 | $74,576 |
| Mexico | 10,448 | $31,032 |
| Japan | 10,427 | $61,395 |
| Brazil | 10,380 | $26,172 |
| France | 10,342 | $64,008 |
| Spain | 8,745 | $51,285 |
| Italy | 6,937 | $52,534 |

### Section C: Hiring Trend

43,534 hires from June 2023 to May 2025. The final month, as a check:

| Department | Hires, May 2025 | 3-Month Average |
| --- | ---: | ---: |
| Finance | 197 | 199.0 |
| HR | 109 | 108.7 |
| IT | 492 | 491.7 |
| Marketing | 225 | 214.0 |
| Operations | 307 | 297.3 |
| R&D | 145 | 143.3 |
| Sales | 357 | 354.7 |

Department comes from the `Hire` row in `job_history.csv.gz`, after mapping name variants. Hires dated after May 31, 2025 are excluded.

### Section D: Pay Review

4,162 employees are high outliers within their department, title, and country group. The top 10:

| Employee | Title | Country | Pay (USD) |
| --- | --- | --- | ---: |
| E1217613 | Operations Director | United States of America | $445,100 |
| E1114456 | Operations Director | United States of America | $425,100 |
| E1028779 | Sales Director | United States of America | $424,800 |
| E1067946 | Operations Director | United States of America | $405,100 |
| E1200157 | Sales Director | United States of America | $403,900 |
| E1134553 | Operations Director | United States of America | $401,300 |
| E1265028 | Sales Director | United States of America | $394,100 |
| E1181081 | IT Manager | United States of America | $392,000 |
| E1231227 | Sales Director | United States of America | $382,300 |
| E1159758 | Sales Director | United States of America | $382,100 |

**Compa-ratio and attrition:** among employees active on May 31, 2024, attrition over the next 12 months falls steadily by compa-ratio quartile: 10.7 percent in the lowest quartile, then 8.7, 6.6, and 4.2 percent in the highest. Underpaid employees leave at about 2.5 times the rate of the best paid.

### Section E: Attrition Model

| Model | ROC-AUC | PR-AUC |
| --- | ---: | ---: |
| Baseline, tenure only | 0.575 | 0.091 |
| Gradient boosting, point-in-time features | 0.794 | 0.289 |
| Same model with leakage (latest review and survey, regardless of date) | 0.842 | not reported |

Training population: 158,006 active on May 31, 2023, with 7.7 percent leaving within a year. Test population: 166,158 active on May 31, 2024, with 7.5 percent leaving.

**Leakage traps:** `termination_date` and `termination_reason` are the outcome itself. Reviews from December 2024 and surveys from September 2024 onward postdate the cutoff, and the September survey carries a pre-departure dip. Job history rows after the cutoff reveal later promotions and pay. Using the latest rows raises ROC-AUC from 0.794 to 0.842, and that gain is fake.

**Most important features** (by permutation importance): latest engagement score, latest rating, and change in engagement over the prior year, followed by compa-ratio and years since last promotion. A missing survey response also carries signal: those employees leave at 11.4 percent against 7.1 percent.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Data integrity | 20 | Resolves employee versions and history corrections by timestamp, parses all date formats, and handles orphans, sentinels, and duplicates with counts. |
| Point-in-time snapshot | 20 | Builds `employee_snapshot.csv` from as-of joins, gets about 174,051 active employees, and excludes the 5,470 future hires. |
| Metrics and hiring trend | 10 | Reusable functions, 8.4 percent attrition as of May 31, 2025, and a 24-month hiring series with zero-filled months. |
| Pay review | 15 | Inverts the four UNIT_PER_USD rates, converts at the as-of month, and links compa-ratio quartiles to attrition. |
| Attrition model | 20 | Features built as of each cutoff, the out-of-time split, ROC-AUC near 0.79 against a baseline, an explicit leakage list, and top features explained in plain terms. |
| Governance | 5 | Minimum group sizes, access limits, and a clear position on individual risk scores. |
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
| Taking each employee's latest job-history row | Snapshot shows later promotions and pay; the model leaks | Does not think in time; the central trap |
| Treating every exchange rate as US dollars per unit | Japan becomes the best-paid country | Did not read `quote_basis` |
| Keeping stale employee versions | 2,000 extra resignations in 2025 | Deduplicated by row instead of by key and timestamp |
| Using the latest review or survey as a feature | ROC-AUC near 0.84 that will not hold up | Leakage; reporting it as a result is a serious error |
| Counting future hires as active | Headcount about 3 percent high | Did not compare dates with the snapshot |
| Reporting a model with no baseline | No way to judge whether the model adds value | Weak evaluation habits |

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

1. How did you decide which job-history row applies on a given date?
2. Your first model probably scored higher than your final one. What changed?
3. Engagement is the strongest predictor. What would you tell an executive who wants to act on individual scores?
4. If HR said salaries for one country looked wrong, where would you look first?
