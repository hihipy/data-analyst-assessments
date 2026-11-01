# Answer Key: Price Elasticity Review

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Hard, spreadsheet track | 3 hours |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs. All data is synthetic.

## What This Assessment Measures

Regression in a spreadsheet, omitted-variable bias, cleaning for log models, interpreting elasticities, and turning them into a profit decision.

## Expected Results

### Part 1: Data Problems

| Problem | Rows | Correct Handling |
| --- | ---: | --- |
| Prices recorded in cents at store ST107 | 30 | Divide by 100 or exclude |
| Weeks with zero units, likely out of stock | 182 | Exclude; the logarithm of zero is undefined, and they reflect supply, not price |

### Part 2: Elasticities

| Product | Price Only | With Display and Holiday | With Store Effects Too | 95% Interval | Display Lift |
| --- | ---: | ---: | ---: | ---: | ---: |
| Cold Brew Coffee | -3.73 | -2.17 | -2.36 | -2.49 to -2.23 | +54.4% |
| Granola Bars 10-ct | -3.37 | -1.85 | -1.93 | -2.06 to -1.81 | +57.1% |
| Ice Cream Pint | -3.98 | -2.83 | -2.79 | -2.97 to -2.61 | +53.8% |
| Olive Oil 1L | -2.7 | -1.1 | -1.1 | -1.22 to -0.98 | +57.9% |
| Paper Towels 6-roll | -2.19 | -0.72 | -0.73 | -0.85 to -0.62 | +56.8% |
| Sparkling Water 12-pack | -3.12 | -1.68 | -1.73 | -1.91 to -1.56 | +54.6% |

The price-only estimates are far too negative because promotions bundle a price cut with an in-store display, and both cluster in holiday weeks when demand is high anyway. The regression credits all of that extra demand to the price cut. Adding display and holiday controls fixes most of the bias; store effects tighten the estimates. The data was simulated with known elasticities (Sparkling Water 12-pack -1.6, Cold Brew Coffee -2.3, Paper Towels 6-roll -0.7, Granola Bars 10-ct -1.9, Olive Oil 1L -1.1, Ice Cream Pint -2.7), and the controlled estimates recover them.

### Part 3: Pricing

| Product | Profit Change at +5% Price | Profit Change at -5% Price | Direction |
| --- | ---: | ---: | ---: |
| Sparkling Water 12-pack | +0.7% | -1.2% | Raise |
| Cold Brew Coffee | -3.3% | +3.3% | Lower |
| Paper Towels 6-roll | +9.9% | -10.6% | Raise |
| Granola Bars 10-ct | -1.2% | +0.9% | Lower |
| Olive Oil 1L | +6.4% | -7.2% | Raise |
| Ice Cream Pint | -5.8% | +6.3% | Lower |

### What a Good Memo Says

- **Raise prices on Paper Towels and Olive Oil.** Demand is inelastic or nearly so, and profit rises with price.
- **Lower prices on Ice Cream and Cold Brew.** They are highly elastic and have room in their margins.
- **Leave Sparkling Water and Granola Bars near current prices.** The gains either way are small.
- **Test before rolling out.** Olive Oil's elasticity is close to -1, where the profit-maximizing price formula breaks down, so a modest increase in a few stores comes before any big change.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Data checks | 15 | Fixes the cents prices and drops zero-unit weeks. |
| Estimation | 30 | Log-log models with display and holiday controls, elasticities near the key, with intervals. |
| Explaining the bias | 20 | Shows why price-only estimates are too negative. |
| Pricing analysis | 20 | Profit change at plus and minus 5 percent using unit cost, and the right direction per product. |
| Memo | 10 | Clear recommendations with a testing plan, and caution near an elasticity of -1. |
| Workbook clarity and AI transparency | 5 | Regression setup traceable. An AI log, if used, at the Strong level. |

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
| Price-only regression | Elasticities 1.2 to 1.6 points too negative | Missed omitted-variable bias; the key trap |
| Keeping zero-unit weeks | Formulas break, or zeros are replaced arbitrarily | Did not think about the log model |
| Optimizing revenue instead of profit | Wrong price direction for some products | Ignored unit cost |
| Trusting the formula for Olive Oil | Recommends a price several times higher | Did not sanity-check the result |

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

1. Why are the price-only estimates so much larger?
2. How did you set up the regression?
3. What test would you run before raising Olive Oil's price?
