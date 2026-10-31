# Answer Key: Coffee Shop Sales Review

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Easy, code track | 60 minutes |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs.

## What This Assessment Measures

Loading a file too large for a spreadsheet, aggregating item lines to transactions and to the quarter, separating customer count from spend per customer, and noticing that one store has fewer days of data than the others.

## Expected Results

### The Files

| File | Rows | Grain |
| --- | ---: | --- |
| `coffee_shop_transactions.csv.gz` | 1,134,659 | One row per item line; 512,700 distinct transactions |
| `coffee_shop_daily_staffing.csv.gz` | 1,070 | One row per store per day open |

Transactions must be counted as distinct `transaction_id` values. Counting rows overstates them by about 2.2 times.

### Part 1: Calculations

| Store | Revenue 2025 | Revenue 2024 | Revenue Change | Transaction Change | Avg Ticket 2025 | Avg Ticket 2024 | Ticket Change | Items per Transaction 2025 | Items per Transaction 2024 | Revenue per Staff Hour 2025 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Downtown | $412,564.80 | $388,112.69 | +6.3% | +2.1% | $6.68 | $6.42 | +4.1% | 2.38 | 2.36 | $79.34 |
| Riverside | $285,618.75 | $301,863.81 | −5.4% | −9.3% | $6.48 | $6.21 | +4.3% | 2.39 | 2.36 | $69.66 |
| Airport | $497,441.49 | $453,761.28 | +9.6% | +4.6% | $9.49 | $9.06 | +4.8% | 2.38 | 2.34 | $82.91 |
| Midtown | $218,568.64 | $242,236.55 | −9.8% | −4.2% | $5.92 | $6.29 | −5.9% | 2.26 | 2.47 | $60.71 |
| Lakeside | $168,254.37 | $60,971.93 | +176.0% | +169.6% | $6.12 | $5.98 | +2.4% | 2.35 | 2.37 | $62.32 |
| Harbor | $253,068.11 | $250,433.84 | +1.1% | −4.1% | $6.30 | $5.98 | +5.3% | 2.39 | 2.34 | $63.27 |

Items per transaction counts units, so it sums `quantity` rather than counting rows.

Chain revenue: $1,835,516.16 in 2025 against $1,697,380.10 in 2024, up 8.1 percent.

Overall 2025 rating, weighted by `rating_count`: Downtown 4.60, Lakeside 4.42, Midtown 4.42, Harbor 4.28, Riverside 4.19, Airport 3.87. A simple average of the daily ratings lands within 0.02 of these, so either method is acceptable at this level. Using `rating_count` is a plus.

**Busiest day:** Saturday, at about $23,417 of chain revenue per Saturday in 2025. Q3 2025 has 14 Tuesdays and 13 of every other weekday, so Tuesday's total ($245,495) edges past Monday's ($244,907) even though Tuesday is the slowest day on average. A strong answer compares averages per day rather than totals.

### Part 2: Analysis

- **The trap.** Lakeside's 2024 rows start on August 4, so its 2024 figure covers 58 days instead of 92. Its +176.0 percent is not real growth. Without Lakeside, the other five stores grew 1.9 percent ($1,667,261.79 against $1,636,408.17). The chain's 8.1 percent overstates performance, and a good answer says so.
- **Midtown is the worst store.** It is the only store where both customers (−4.2 percent) and spend per customer (−5.9 percent) fell. The line items show why: customers bought fewer items per visit (2.47 down to 2.26) while prices rose at every store. It also has the lowest revenue per staff hour.
- **Riverside lost customers but not spend.** Transactions fell 9.3 percent, the steepest drop among comparable stores, while the average ticket rose 4.3 percent. The problem is foot traffic.
- **Harbor looks flat but is losing customers.** Revenue rose 1.1 percent only because tickets rose 5.3 percent. Transactions fell 4.1 percent.
- **Best store depends on the measure, and the candidate should say which they used.** Airport leads on revenue growth (+9.6 percent), average ticket, and revenue per staff hour, but it has the lowest rating (3.9). Downtown is the most balanced: solid growth, more customers, and the highest rating (4.6). Either answer is acceptable if it is justified.

### Part 3: What Good Recommendations Look Like

- Tied to a number, for example Midtown's drop in items per transaction or Riverside's −9.3 percent transactions.
- Matched to the cause: traffic problems (Riverside, Harbor) need different fixes than basket-size problems (Midtown).
- A strong extra: Airport's low rating is a risk to watch, even though its numbers are strong.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Data handling | 20 | Counts distinct `transaction_id` values, sums `quantity` for items, notices Lakeside's 58 days of 2024 data, and uses `rating_count` or states why not. |
| Calculations | 25 | Revenue, transaction, and ticket changes within 0.1 percentage point of the key; ticket and revenue per staff hour within $0.01. |
| Analysis and judgment | 25 | Splits each revenue change into traffic and ticket, reports the 1.9 percent comparable-store growth, and justifies best and worst with a stated measure. |
| Communication | 15 | One page or 3 slides, at least one clear chart, and every claim tied to a number. |
| Reproducibility and AI transparency | 15 | Code or notebook reruns from the CSV files. An AI log, if used, that meets the Strong level below. |

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
| Counting rows as transactions | Transactions about 2.2 times too high, and tickets too low | Did not read the file's grain |
| Reporting 8.1 percent chain growth as performance | Overstates growth by about 6 points | Missed the partial year; the key trap at this level |
| Counting rows as items | Items per transaction slightly low | Ignored the `quantity` column |
| Comparing weekday totals instead of daily averages | Tuesday looks busier than Monday | Did not check how many of each weekday the quarter has |
| Calling Midtown a traffic problem only | Misses the basket-size drop | Stopped at revenue and transactions |

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

1. How did you confirm that your transaction count was right?
2. If Lakeside had opened on July 1, 2024, what would change in your answer?
3. Midtown's customers buy fewer items per visit. What two things would you check before recommending a fix?
4. Which number in your summary are you least sure of, and why?
