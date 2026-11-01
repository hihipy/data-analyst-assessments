# Answer Key: Production Quality Review

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Hard, spreadsheet track | 3 hours |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs. All data is synthetic.

## What This Assessment Measures

Statistical process control: control charts from a stable baseline, within versus overall capability, Pareto analysis, and root-cause reasoning from lots and shifts.

## Expected Results

### Part 1: Data Problems

On September 10, Line 1's gauge recorded 80 diameters in inches (about 0.98) instead of millimeters. Multiply by 25.4; as recorded, every one of those parts looks wildly out of specification.

### Part 2: Defects

Defects by type: Burr 51, Scratch 49, Out of Spec 4. Defect rate by line (percent): Line 1 0.88, Line 2 0.84, Line 3 1.53.

Line 3's scratches are concentrated on the evening shift in September: 2.88 percent of evening parts against 0.5 percent in August, while the day shift stayed near 0.25 percent. A change in September, such as skipped maintenance or a new setup, is the likely cause and worth asking about.

### Part 3: Control and Capability

| Line | Mean (mm) | Within-Subgroup Sigma | Overall Sigma | Cp | Cpk (Within) | Overall Performance (Ppk) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Line 1 | 25.0001 | 0.009 | 0.009 | 1.86 | 1.85 | 1.85 |
| Line 2 | 25.0082 | 0.0101 | 0.0146 | 1.65 | 1.38 | 0.96 |
| Line 3 | 25.0039 | 0.014 | 0.0139 | 1.19 | 1.09 | 1.11 |

- **Line 2 drifted with supplier lot L-2291.** With limits set from August 4 to 15 (center 25.0, limits 24.9871 to 25.0129), Line 2 is out of control from 2025-08-18 to 2025-09-05: 237 subgroups. Lot L-2291 averages 25.0218 mm against 25.001 to 25.002 for every other lot. Line 2's within-subgroup Cpk of 1.38 looks acceptable, but its overall Ppk of 0.96 shows what the customer received. That gap is the sign of a shifted process.
- **Line 3 is not capable.** Its Cp of 1.19 means its spread is too wide for the specification even when centered; it fails the 1.33 target regardless of lot.
- **Line 1 is capable** at Cpk 1.85.

### Part 4: What a Good Memo Says

- Quarantine and return lot L-2291, and check any parts from it already shipped.
- Line 3 needs a process fix, such as tooling, fixtures, or machine maintenance, to reduce variation; centering alone won't help.
- Investigate Line 3's evening shift in September for the scratch problem.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Data check | 15 | Finds and converts the inch readings. |
| Defect analysis | 15 | Pareto by type, and rates by line, shift, and lot. |
| Control charts | 25 | Limits from a stable period, and Line 2's shift from August 18 to September 5 found. |
| Capability | 25 | Cp and Cpk from within-subgroup sigma, Ppk from overall, and the Line 2 gap explained. |
| Memo | 15 | Causes, priorities, and actions for each line. |
| Workbook clarity and AI transparency | 5 | Calculations traceable. An AI log, if used, at the Strong level. |

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
| Leaving the inch readings in | 80 parts look like scrap | Did not profile the data |
| Setting control limits from all the data | The shifted period widens the limits and hides itself | Baseline not chosen |
| Reporting only within-subgroup Cpk | Line 2 looks capable | Confused potential with actual performance |
| Trying to center Line 3 | Does not fix a spread problem | Misread Cp against Cpk |

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

1. How did you choose the period for your control limits?
2. Why do Line 2's Cpk and Ppk disagree?
3. What would you check on Line 3's evening shift?
