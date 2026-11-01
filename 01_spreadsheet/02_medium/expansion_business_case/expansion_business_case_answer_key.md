# Answer Key: New Location Business Case

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Medium, spreadsheet track | 90 minutes |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs. All data is synthetic.

## What This Assessment Measures

Building a financial model from assumptions and comparables: ramp curves, discounting, break-even, sensitivity, and survivorship bias.

## Expected Results

### The Trap

Two of the 12 comparable stores, Store 04 and Store 09, closed after 14 and 20 months. Their rows simply stop. Averaging whichever stores are open each month quietly drops the failures, so the revenue curve shows only survivors: about $124,243 a month by month 24.

The two closed stores ran at roughly half the revenue of the others. With 2 of 12 failing, a fair model gives a new location a one-in-six chance of following that path.

### Part 2: Model Results

| Measure | Site A | Site B |
| --- | ---: | ---: |
| NPV if the store succeeds (survivor revenue curve) | $247,258 | $-175,275 |
| Payback month if it succeeds | 40 | Not within 60 months |
| NPV if it fails (weak revenue, closed at month 17) | $-988,871 | $-929,802 |
| **Expected NPV** (5 in 6 succeed) | **$41,237** | **$-301,030** |
| Monthly revenue to break even (year 1 rent) | $99,194 | $88,710 |

The model uses the survivors' average revenue by month since opening, holds months 37 to 60 at the month 25 to 36 average, scales by each site's traffic factor, applies the 62 percent margin, fixed costs, three months of launch marketing, and rent rising 3 percent a year, and discounts monthly at the 10 percent annual rate. Other reasonable choices will move the numbers somewhat, but not the ranking.

### Part 3: Sensitivity (Expected NPV)

| Scenario | Site A | Site B |
| --- | ---: | ---: |
| rev -20%, rent -10% | $-501,473 | $-734,367 |
| rev -20%, rent +0% | $-594,904 | $-798,880 |
| rev -20%, rent +10% | $-688,336 | $-863,391 |
| rev +0%, rent -10% | $134,668 | $-236,518 |
| rev +0%, rent +0% | $41,237 | $-301,030 |
| rev +0%, rent +10% | $-52,195 | $-365,541 |
| rev +20%, rent -10% | $770,810 | $261,332 |
| rev +20%, rent +0% | $677,378 | $196,821 |
| rev +20%, rent +10% | $583,947 | $132,308 |

### Part 4: What a Good Recommendation Says

- **Site B does not pay back** in any scenario except revenue 20 percent above plan.
- **Site A is marginal.** Ignoring the closures makes it look clearly worth doing; with closure risk, its expected NPV is close to zero, and a 20 percent revenue shortfall makes it a large loss.
- **A defensible answer is Site A only with conditions,** such as a rent concession or early-exit clause, or neither until the group understands why two stores failed. Either is fine if argued from the numbers.
- **Five years with no value afterward is conservative,** and a strong answer says so.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Revenue ramp | 25 | Builds the curve from comparables and handles the two closed stores explicitly. |
| Model mechanics | 25 | Monthly cash flows, rent escalation, launch costs, and correct monthly discounting. |
| Risk | 25 | A sensitivity table and a closure scenario or equivalent adjustment. |
| Recommendation | 15 | A clear choice with the conditions that must hold. |
| Workbook clarity and AI transparency | 10 | Inputs separated from calculations. An AI log, if used, at the Strong level. |

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
| Averaging only the stores still open | Site A worth $247,000 instead of close to zero | Survivorship bias; the key trap |
| Discounting monthly flows at 10 percent a month | NPV wildly too low | Mixed up rates and periods |
| Ignoring rent increases | NPV overstated | Missed an assumption |
| Recommending Site B for its lower rent | Picks the site that never pays back | Optimized one input |

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

1. How did you treat the stores that closed?
2. Which assumption moves the answer most?
3. What would make you sign the Site A lease?
