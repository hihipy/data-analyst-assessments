# Answer Key: Online Store Order Review

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Easy, spreadsheet track | 45 minutes |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs.

## What This Assessment Measures

Filtering by status before summing, building pivots, computing rates with the right denominator, and turning a small dataset into two or three clear observations.

## Expected Results

### The Trap

Only completed orders count as revenue. Completed revenue is $171,813.50. Summing every row gives $189,916.60, which wrongly includes 87 returned and 49 cancelled orders.

### Part 1: Calculations

Revenue by month and category (completed orders):

| Month | Bath | Bedding | Decor | Kitchen | Lighting | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| January | $2,361.05 | $8,282.75 | $3,648.55 | $4,250.45 | $4,641.75 | $23,184.55 |
| February | $2,895.00 | $7,315.05 | $4,935.00 | $4,128.60 | $2,462.00 | $21,735.65 |
| March | $3,402.45 | $8,529.95 | $5,723.50 | $5,282.65 | $4,624.25 | $27,562.80 |
| April | $2,824.80 | $10,864.75 | $7,958.00 | $4,539.95 | $2,818.50 | $29,006.00 |
| May | $3,750.40 | $9,110.60 | $7,982.15 | $6,669.15 | $4,437.50 | $31,949.80 |
| June | $4,757.80 | $9,722.95 | $9,646.90 | $7,619.05 | $6,628.00 | $38,374.70 |
| Total | $19,991.50 | $53,826.05 | $39,894.10 | $32,489.85 | $25,612.00 | $171,813.50 |

Average order value by region: North $104.17 (512 orders), South $102.23 (404), East $99.80 (360), West $96.83 (426).

Top 5 products: Area Rug 5x8 $18,625.20, Cotton Sheet Set $18,360.70, Linen Duvet Cover $16,815.15, Wall Mirror $10,827.00, Bath Towel Set $10,554.60.

Return rate (returned ÷ completed plus returned):

| Category | Returned | Completed | Return Rate |
| --- | ---: | ---: | ---: |
| Lighting | 23 | 127 | 15% |
| Bedding | 24 | 404 | 6% |
| Decor | 17 | 397 | 4% |
| Bath | 12 | 359 | 3% |
| Kitchen | 11 | 415 | 3% |

### Part 2: What a Good Answer Says

- **Lighting is the concern.** Its return rate of 15 percent is more than double any other category's.
- **Revenue grew every month after February**, from $21,735.65 to $38,374.70 in June, a 76.6 percent rise.
- **Bedding is the largest category** at $53,826.05, 31.3 percent of revenue.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Status filtering | 25 | Counts only completed orders as revenue ($171,813.50) and excludes cancelled orders from the return rate. |
| Calculations | 25 | Monthly and category revenue, average order value by region, top 5 products, and return rates matching the key. |
| Analysis | 20 | Flags Lighting's 15 percent return rate and supports two further observations with numbers. |
| Chart and summary | 20 | A correct monthly revenue chart and a one-page summary a manager could act on. |
| Workbook clarity and AI transparency | 10 | Formulas or pivots visible and traceable in the workbook. An AI log, if used, at the Strong level. |

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
| Summing every row | Revenue of $189,916.60, overstated by $18,103.10 | Did not read the status column; the key trap |
| Return rate over all orders, cancelled included | Rates slightly low | Picked the wrong denominator |
| Pasting values instead of formulas | Work cannot be checked | Weak working habits |
| Calling Bedding the concern because it is largest | Misses the return problem | Confused size with risk |

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

1. Why did you leave cancelled orders out of the return rate?
2. What would you check before telling the manager to stop selling floor lamps?
3. June is the best month. What would you need to know before calling it a trend?
