# Answer Key: Employee Survey Analysis

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Medium, spreadsheet track | 90 minutes |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs. All data is synthetic.

## What This Assessment Measures

Cleaning survey codes, reverse-coding negative items, weighting to the population, margins of error, and reporting responsibly on small groups.

## Expected Results

### Part 1: Data Problems

| Problem | Rows | Correct Handling |
| --- | ---: | --- |
| Duplicate submissions | 45 | Remove |
| Answers coded 9, not applicable | 1,083 answers | Treat as missing, not as a high score |
| Two negatively worded items: q4 ("I often think about leaving") and q8 ("My workload is often unmanageable") | Every response | Reverse-code before calling 4 or 5 favorable. Without it, q4 reads 27.9 percent favorable instead of 40.4. |
| Legal has only 3 respondents | 3 | Suppress; below the minimum of 5 |

### Part 2: Results

| Department | Response Rate | Respondents | Engagement Favorable | Margin of Error | Change vs 2024 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Headquarters | 77.3% | 634 | 61.4% | ±1.8 | -1.6 |
| Engineering | 68.6% | 439 | 52.2% | ±2.6 | +2.2 |
| Finance | 66.2% | 139 | 51.4% | ±4.8 | -1.6 |
| Field Sales | 38.4% | 557 | 38.0% | ±3.2 | -1.0 |
| Customer Service | 51.5% | 979 | 33.1% | ±2.1 | -6.9 |
| Warehouse | 29.0% | 755 | 25.4% | ±2.6 | -1.6 |
| Legal | 7.9% | 3 | Suppressed |  |  |

Company-wide engagement is **36.5 percent** weighted by headcount, against 40.4 percent unweighted. Headquarters answered at 77.3 percent and the Warehouse at 29.0 percent, so the unweighted figure overstates how engaged the company is.

Item favorable shares (percent): q1 40.5, q2 40.8, q3 49.8, q4 40.4, q5 49.0, q6 27.5, q7 28.3, q8 39.3, q9 41.1, q10 40.4. Recognition (q6) and career growth (q7) are lowest.

### Part 3: What a Good Answer Says

- **Customer Service is the only real change.** It fell 6.9 points, more than three times its margin of error. Every other change is within its margin.
- **The Warehouse is lowest** at 25.4 percent and has one of the lowest response rates, so leaders there should hear both results.
- **Legal is not reported.** With 3 responses, showing its score would identify people.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Data checks | 20 | Removes duplicates, treats 9 as missing, reverse-codes q4 and q8, and suppresses Legal. |
| Results | 25 | Response rates, engagement by department with margins of error, and item scores matching the key. |
| Weighting | 15 | Weights to headcount and explains why the unweighted figure is too high. |
| Change since last year | 20 | Identifies Customer Service as the only change beyond its margin. |
| Recommendations | 10 | Tied to numbers, and mindful of anonymity. |
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
| Counting 9 as a score | Favorable shares inflated | Did not read the scale |
| Not reverse-coding q4 and q8 | Engagement understated, and those items look terrible | Did not read the question wording; the key trap |
| Reporting Legal | Identifies three people | Missed the anonymity rule |
| Calling every change real | Leaders react to noise | Ignored margins of error |

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

1. Which items did you reverse-code, and how did you find them?
2. Why weight by headcount?
3. What would you say to the Customer Service leader?
