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
| Weeks with zero units, likely out of stock | 191 | Exclude; the logarithm of zero is undefined, and they reflect supply, not price |

### Part 2: Elasticities

The data was simulated so that price response is not constant. Small price changes follow each product's local elasticity, deeper discounts draw extra demand as shoppers stock up, and sales dip in the week after a promotion. A single log-log slope averages these together.

| Product | True Local Elasticity | Price Only | Display and Holiday Controls | Plus Store Effects | Extended Model |
| --- | ---: | ---: | ---: | ---: | ---: |
| Sparkling Water 12-pack | -1.6 | -3.3 | -1.91 | -2.13 | -1.56 |
| Cold Brew Coffee | -2.3 | -4.27 | -2.89 | -2.84 | -2.51 |
| Paper Towels 6-roll | -0.7 | -2.72 | -1.16 | -1.29 | -0.89 |
| Granola Bars 10-ct | -1.9 | -4.08 | -2.64 | -2.53 | -1.97 |
| Olive Oil 1L | -1.1 | -3.12 | -1.71 | -1.73 | -1.32 |
| Ice Cream Pint | -2.7 | -4.88 | -3.54 | -3.42 | -2.95 |

- **Price only** is far too negative, because promotions bundle a price cut with a display, and both cluster in holiday weeks.
- **Adding display and holiday controls** removes most of that bias, but the estimates stay 0.3 to 0.8 too negative, because deep discounts are more powerful than small price moves.
- **The extended model** adds a term for discounts deeper than 10 percent and a term for the week after a promotion, and lands within about 0.25 of the truth. It finds the extra deep-discount effect (Cold Brew Coffee -0.55, Granola Bars 10-ct -0.93, Ice Cream Pint -0.77, and so on) and a post-promotion dip of -17.5 to -11.6 percent.

Display lifts sales by about 57 percent across products.

### Part 3: Pricing

Profit change for a 5 percent price change, using each product's unit cost:

| Product | +5% (True Response) | -5% (True Response) | +5% (Simple Model) | -5% (Simple Model) |
| --- | ---: | ---: | ---: | ---: |
| Sparkling Water 12-pack | +1.3% | -1.8% | -1.2% | +0.9% |
| Cold Brew Coffee | -3.0% | +3.0% | -5.6% | +5.9% |
| Paper Towels 6-roll | +10.1% | -10.8% | +7.0% | -8.0% |
| Granola Bars 10-ct | -1.0% | +0.8% | -4.0% | +4.1% |
| Olive Oil 1L | +6.4% | -7.2% | +3.2% | -4.1% |
| Ice Cream Pint | -5.4% | +5.8% | -8.7% | +9.8% |

### What a Good Memo Says

- **Raise prices on Paper Towels and Olive Oil.** Demand is inelastic or close to it, and profit rises with price under any model.
- **Lower prices on Ice Cream and Cold Brew.** Both are highly elastic, with room in their margins.
- **Sparkling Water shows why the model matters.** The simple model says a cut raises profit; the true small-move response says a 5 percent increase does. A candidate who notices that deep-discount weeks drive the simple estimate, and tests a small increase, gets this right.
- **Promotions borrow from the following week.** Part of every promotion's lift comes back as a dip afterward, so promotion lifts measured in the promotion week alone overstate their value.
- **Test before rolling out:** a small price change in a few stores for four to six weeks.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Data checks | 15 | Fixes the cents prices and drops zero-unit weeks. |
| Estimation | 25 | Log-log models with display and holiday controls, store effects, and intervals. |
| Model checking | 25 | Shows why price-only estimates are too negative, and finds that deep discounts or the week after a promotion behave differently. |
| Pricing analysis | 20 | Profit change at plus and minus 5 percent using unit cost, with Sparkling Water's direction handled carefully. |
| Memo | 10 | Clear recommendations with a testing plan. |
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
| Price-only regression | Elasticities 1.7 to 2.2 points too negative | Missed omitted-variable bias; the key trap |
| One slope for every discount depth | Overstates sensitivity to small price changes; flips Sparkling Water's direction | Did not check whether the model fits |
| Keeping zero-unit weeks | Formulas break, or zeros are replaced arbitrarily | Did not think about the log model |
| Optimizing revenue instead of profit | Wrong price direction for some products | Ignored unit cost |

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
2. How did you check whether one elasticity fits every discount depth?
3. Would you raise or lower Sparkling Water's price, and how would you test it?
