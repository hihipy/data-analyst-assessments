# Answer Key: Support Ticket Review

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Easy, code track | 60 minutes |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs. All data is synthetic.

## What This Assessment Measures

Cleaning and categorizing free text at scale, validating a method against labeled data, and spotting an emerging issue in a time series.

## Expected Results

### Part 1: Data Problems

| Problem | Rows | Correct Handling |
| --- | ---: | --- |
| Resubmissions: same customer, same text, within 15 minutes | 20,000 | Remove; they inflate volume |
| Automatic out-of-office replies | 15,309 | Remove; they are not requests |
| Tickets in Spanish | 65,054 | Categorize them too; dropping them loses 6 percent of customers |

Removing the noise leaves 1,065,000 real tickets; raw counts overstate volume by 3.3 percent.

### Part 1: Method

Simple keyword rules, in English and Spanish, reach 99.7 percent accuracy on the labeled sample, so a model is not required. Any method is fine if it is checked against the sample.

### Part 2: Results

Lowest satisfaction (average, 1 to 5): Verification Code 2.6, Product Defect 3.1, Refund 3.29, Login 3.39. Only 34.9 percent of tickets have a rating, so these averages come from about a third of tickets.

Median minutes to resolve: Product Defect 75, Verification Code 59, Shipping 41, Other 38.

**The new problem:** tickets about verification codes not arriving start in July 2025 and reach 8,300 in August, 14.6 percent of all tickets in the third quarter. They have the lowest satisfaction of any category. Login tickets did not rise to match, so this is a new failure, not a relabeling.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Cleaning | 20 | Removes resubmissions and auto-replies, and keeps Spanish tickets. |
| Categorization | 25 | A documented method with accuracy checked on the labeled sample. |
| Analysis | 30 | Volume by month and category, satisfaction and resolution by category, and the verification-code spike found and sized. |
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
| Counting resubmissions | Volume overstated | Did not look for repeats |
| Dropping Spanish tickets | Loses 6 percent of customers | Assumed one language |
| No accuracy check | No evidence the categories are right | Skipped validation |
| Missing the July spike | A new problem goes unreported | Looked only at totals |

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

1. How did you decide two tickets were the same request?
2. How accurate was your method, and where did it fail?
3. When did the verification problem start, and what would you check next?
