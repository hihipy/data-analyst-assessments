# Answer Key: Pharmacy Claims Review

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Easy, code track | 60 minutes |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs. All data is synthetic.

## What This Assessment Measures

Loading a file too large for a spreadsheet, netting reversals against the claims they cancel, assigning spending to the right period, and separating like-for-like growth from network growth.

## Expected Results

### The Files

`pharmacy_claims.csv.gz` has 1,169,255 rows, including 39,540 reversals. A reversal cancels an earlier claim: it repeats the claim with negative amounts and names it in `original_claim_id`.

### The Traps

- **Reversals.** Net fills are originals that were not reversed: 508,080 in 2024 and 582,095 in 2025. Counting every original row overstates fills by about 4 percent.
- **Reversals that cross the year.** 849 reversals are dated in a later year than the claim they cancel, including some in January 2026. Spending belongs to the year of the original fill. Summing rows by their own date leaves a negative 2026 total.
- **New pharmacies.** Eight pharmacies joined the network in the second half of 2024, so 2025 includes a full year of them. Total plan spending rose 23.9 percent, but for pharmacies in the network the whole time it rose 11.5 percent.

### Part 1: Calculations

| Drug Class | Plan Paid 2024 | Plan Paid 2025 | Change |
| --- | ---: | ---: | ---: |
| Antibiotic | $282,504.80 | $330,025.83 | +16.8% |
| Blood Pressure | $940,331.14 | $1,085,285.13 | +15.4% |
| Cholesterol | $4,835,470.58 | $6,081,932.48 | +25.8% |
| Diabetes | $57,629,054.12 | $72,617,903.64 | +26.0% |
| Immunology | $27,399,702.44 | $32,357,497.46 | +18.1% |
| Mental Health | $10,041,920.45 | $12,684,521.39 | +26.3% |
| Respiratory | $10,940,403.61 | $13,685,774.19 | +25.1% |

Total: $112,069,387.14 in 2024 and $138,842,940.12 in 2025.

Cost per 30-day supply, 2024 to 2025: Diabetes $328.23 to $355.02, Immunology $3,373.52 to $3,676.15.

Generic share of fills: 86.9 percent in 2024 and 87.1 percent in 2025. Brand drugs are about 13 percent of fills but 96.0 percent of spending.

Top 10 drugs by 2025 plan spending: Ozempic $49,230,799.05, Humira $32,357,497.46, Jardiance $22,658,382.10, Vraylar $12,045,149.74, Trelegy $11,978,908.81, Repatha $4,998,969.68, Albuterol $1,706,865.38, Metformin $728,722.49, Atorvastatin $584,602.52, Rosuvastatin $498,360.28.

### Part 2: What a Good Answer Says

- Reports the comparable-pharmacy growth of 11.5 percent alongside the headline 23.9 percent.
- Names Diabetes, led by Ozempic, as the largest driver, and separates its price increase from the extra volume.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Data handling | 20 | Nets reversals by `original_claim_id`, assigns them to the original fill year, and counts net fills. |
| Calculations | 25 | Spending by class and year, cost per 30 days, generic share, and the top 10 matching the key. |
| Analysis and judgment | 25 | Reports the 11.5 percent comparable-pharmacy growth beside the 23.9 percent headline and splits Diabetes growth into volume and price. |
| Communication | 15 | One page or 3 slides, a clear chart, and every claim tied to a number. |
| Reproducibility and AI transparency | 15 | Code or notebook reruns from the files. An AI log, if used, at the Strong level. |

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
| Counting original rows as fills | Fills overstated by about 4 percent | Did not read what a reversal is |
| Grouping reversals by their own date | A negative 2026 total, and years slightly off | Did not assign reversals to the claim they cancel |
| Reporting 23.9 percent growth as performance | About half the reported growth is new pharmacies | Missed the pharmacies that joined in 2024 |
| Counting fills by row instead of days supplied | Mail-order 90-day fills undercounted | Ignored `days_supply` |

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

1. How did you decide which claims were reversed?
2. What would you tell the director about the 23.9 percent?
3. Is Ozempic growth more prescriptions or higher prices?
