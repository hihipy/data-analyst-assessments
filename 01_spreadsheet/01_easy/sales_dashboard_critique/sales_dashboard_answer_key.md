# Answer Key: Sales Dashboard Critique

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Easy, spreadsheet track | 45 minutes |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs. All data is synthetic.

## What This Assessment Measures

Checking numbers against their source, recognizing misleading chart choices, and designing views that answer real questions for every reader.

## Expected Results

### Part 1: The Problems

| Element | Problem | Correct Value or View |
| --- | --- | --- |
| Total 2025 revenue | The formula stops before December, leaving out 20 rows | $62,595,395, not $58,149,253 |
| Growth vs 2024 | Built on the wrong total, so it shows a decline | +2.5 percent, not -4.8 percent |
| Target attainment | Built on the wrong total | 96.6 percent, not 89.7 percent |
| Revenue by region bar chart | The value axis starts at $8,000,000, not zero, which exaggerates small differences; the title claims growth everywhere, but West fell 1.0 percent | Start the axis at zero, or show growth rates directly; title it with the actual finding |
| Revenue by region colors | The two years are told apart only by red and green | A color-blind-safe pair, or labels on the bars |
| Revenue mix pie chart | 20 slices are unreadable and hide the region and product structure | A bar chart or a small table by region and product line |
| Revenue vs target line chart | Compares a running total with a monthly target, which can never match | Monthly revenue against monthly target, or both cumulative |

Region growth, 2025 against 2024 (percent): North +4.3, South +2.7, East +2.9, West -1.0, Central +3.8. West revenue fell 13.3 percent from the first half of 2025 to the second, the story the original dashboard hides.

Target attainment by region (percent): North 97.9, South 97.2, East 97.0, West 92.7, Central 98.3.

### Part 2: What a Good Redesign Has

- Headline numbers that match the data, with the period stated.
- One view that makes West's decline visible, such as monthly revenue by region.
- Monthly revenue against target, on the same basis.
- Charts that do not rely on red and green alone: labels, patterns, or a color-blind-safe palette.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Finding the errors | 30 | Catches the formula that drops December, and its effect on all three headline numbers. |
| Chart critique | 25 | Names the truncated axis, the misleading title, the 20-slice pie, and the running total against a monthly target. |
| Redesign | 25 | Three to five views, each tied to a question, with West's decline visible and accessible colors. |
| Explanation | 10 | A short critique a manager could read in two minutes. |
| Workbook clarity and AI transparency | 10 | Corrected formulas visible. An AI log, if used, at the Strong level. |

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
| Accepting the headline numbers | Reports a 4.8 percent decline instead of 2.5 percent growth | Did not check formulas; the key trap |
| Critiquing style only | Misses the wrong totals | Treats dashboards as decoration |
| Rebuilding the same charts more neatly | West's decline stays hidden | Did not ask what the dashboard is for |

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

1. How did you find the formula error?
2. What question should the first chart on the dashboard answer?
3. Why does the axis starting point matter on a bar chart?
