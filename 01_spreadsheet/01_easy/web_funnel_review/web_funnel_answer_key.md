# Answer Key: Website Conversion Funnel Review

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Easy, spreadsheet track | 45 minutes |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs. All data is synthetic.

## What This Assessment Measures

Funnel analysis: step conversion, segment comparisons, and noticing when the way data is recorded breaks the funnel's logic.

## Expected Results

### The Traps

- **Express checkout skips steps.** 362 mobile purchases used a one-tap wallet and never reached the cart or checkout steps: 36.4 percent of mobile purchases. Counting them in the purchase step pushes checkout-to-purchase conversion above what the checkout page achieves. Analyze them as a separate path.
- **A tracking outage.** From August 12 to 14, the checkout step was not recorded at all (855 sessions). Leave those days out of step rates.

Counting every row naively gives a checkout-to-purchase rate of 79.6 percent instead of 62.5 percent.

### Part 1: Calculations

Standard funnel, outage days and express purchases excluded:

| Step | Sessions | Conversion From Previous Step |
| --- | ---: | ---: |
| All sessions | 24,799 |  |
| Product page | 14,943 | 60.3% |
| Cart | 4,384 | 29.3% |
| Checkout | 2,452 | 55.9% |
| Purchase | 1,532 | 62.5% |

| Device | Cart to Checkout | Checkout to Purchase | Session Conversion | Revenue per Session |
| --- | ---: | ---: | ---: | ---: |
| Desktop | 66.5% | 73.1% | 9.99% | $8.02 |
| Mobile | 47.9% | 52.2% | 6.11% | $5.17 |
| Tablet | 61.9% | 63.5% | 8.04% | $7.05 |

By source (session conversion, revenue per session): Direct 9.52% and $7.76, Email 13.52% and $11.42, Organic Search 7.62% and $6.24, Paid Search 7.45% and $6.19, Social 2.48% and $2.13.

### Part 2: What a Good Answer Says

- **The biggest drop is product page to cart,** and it is worse on mobile: 26.5 percent of mobile product viewers add to cart, against 33.8 percent on desktop and tablet.
- **Mobile checkout is the fixable problem.** Mobile loses far more shoppers at cart-to-checkout and checkout-to-purchase than desktop, and mobile is most of the traffic. The express wallet's popularity points to the fix: make mobile checkout shorter.
- **Social traffic converts at about a third of the average,** worth checking against what it costs.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Funnel logic | 25 | Handles express purchases that skip steps, and excludes the August 12 to 14 outage. |
| Calculations | 25 | Step counts and rates, device and source comparisons matching the key. |
| Analysis | 20 | Identifies mobile checkout as the main fixable loss. |
| Chart and summary | 20 | A clear funnel chart and a one-page summary. |
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
| Counting express purchases in the checkout funnel | Checkout-to-purchase near 80 percent instead of 62.5 | Assumed every step is recorded for everyone; the key trap |
| Keeping the outage days | A false checkout dip in mid-August | Did not check the data over time |
| Comparing devices on session conversion only | Misses where mobile loses shoppers | Stopped at the top-line rate |

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

1. How did you handle purchases with no cart?
2. What happened on August 12 to 14?
3. What would you change on mobile first?
