# Answer Key: Open-Ended Sales Question

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Easy, code track | 60 minutes |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs. All data is synthetic.

## What This Assessment Measures

Turning a vague request into an answerable question: scoping, stating assumptions, checking data completeness, decomposing a change, and answering in plain language.

## Expected Results

### What This Assessment Rewards

There is no single right answer. The strongest submissions define the question before answering it, check the data before trusting it, and separate what is happening from what only looks like it.

### Part 1: Good Scoping

Useful questions include: what "sales" means (gross bookings or net revenue after discounts and refunds), soft compared with what (last month, last year, or plan), and since when. Strong answers state their assumptions plainly, for example "net revenue, third quarter against the same quarter last year."

### Part 2: The Facts

| Comparison | Change |
| --- | ---: |
| September against August, net | -16.3% |
| September 2025 against September 2024, as loaded | -6.1% |
| September against last September, same days only | +4.2% |
| Third quarter against last year, gross | +4.7% |
| Third quarter against last year, net | +1.7% |

- **The data is missing three days.** `daily_load_log.csv.gz` shows the loads for September 22 to 24, 2025 failed, so those orders are absent. They account for most of September's apparent decline. September is also seasonally slower than August every year.
- **Overall sales are not down.** Third-quarter net sales rose 1.7 percent, on 2.6 percent more order lines and 2.1 percent more customers.
- **Gross grew faster than net,** for two reasons:
  - Discounts rose from 7.9 to 10.1 percent of gross.
  - Refunds jumped to about 6.5 percent of orders from June 2025, against a 2024 average of 4.0 percent, consistent with a policy change. August and September refund rates look lower only because many refunds have not happened yet, so net sales for those months will fall further.
- **One category is soft.** Home fell 15.5 percent against last year, starting in July, while Electronics grew 12.0 percent and the rest were flat to slightly up.

### Part 3: What a Good Answer to the CEO Says

Sales are not falling overall; September looks weak because three days of orders failed to load. Two real problems sit underneath: Home is down sharply since July, and discounts and refunds are eating more of each sale. Fix the data load, find out what happened in Home, and review the discount and refund policies.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Scoping | 25 | Clarifying questions and explicit assumptions about the definition, period, and comparison. |
| Data check | 20 | Finds the three failed loads before drawing conclusions. |
| Decomposition | 25 | Separates volume, discounts, refunds, and category mix, and finds Home's decline. |
| Answer | 20 | A two-minute answer that says what is and isn't happening, with one or two actions. |
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
| Comparing September with August | A 16 percent decline that is mostly missing days and seasonality | Did not choose a fair comparison |
| Not checking the load log | Reports a data outage as a sales drop | Trusted the data |
| Using gross sales only | Misses the discount and refund squeeze | Did not define sales |
| Reporting every cut of the data | The CEO cannot find the answer | Did not prioritize |

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

1. What did you assume "sales" meant, and why?
2. How did you find the missing days?
3. If you had five minutes with the CEO, what would you say first?
