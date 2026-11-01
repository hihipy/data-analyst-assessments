# Answer Key: Bank Reconciliation

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Medium, spreadsheet track | 90 minutes |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs. All data is synthetic.

## What This Assessment Measures

Matching records between two systems, one-to-one and many-to-one, separating timing differences from errors, and closing to the cent.

## Expected Results

### The Reconciliation

| Item | Amount |
| --- | ---: |
| Bank balance, September 30 | $1,279,406.16 |
| Add: deposit in transit (September 30 customer receipts) | $59,774.05 |
| Add: card settlement in transit (September 30, net of fees) | $12,938.36 |
| Less: 31 outstanding checks | $-52,474.50 |
| **Adjusted bank balance** | **$1,299,644.07** |
| Book balance, September 30 | $1,299,373.09 |
| Less: card processing fees (2.6 percent, all September settlements) | $-6,881.44 |
| Less: monthly service fee | $-95.00 |
| Add: interest paid | $312.47 |
| Less: returned check (NSF), Customer O | $-1,293.63 |
| Add back: two duplicated ACH entries | $8,181.58 |
| Correct: three ACH amounts keyed wrong | $47.00 |
| **Adjusted book balance** | **$1,299,644.07** |

The two adjusted balances agree to the cent.

### How the Transactions Match

- **Checks** match on check number. The four August checks on `Prior_Outstanding` clear in September and are already in the August books, so they are not reconciling items this month.
- **ACH payments** match on the trace number in both references.
- **Customer receipts** are recorded one by one in the ledger but deposited as one daily batch at the bank. They match many to one on the batch reference (`DB-MMDD`).
- **Card settlements** match on the batch reference, but the bank amount is net of a 2.6 percent fee. The fee has to be booked.
- **Bank-only items** are the service fee, interest, and the returned check.

### Book Errors

- Duplicated entries: ACH770239 ($-3,340.25), ACH770191 ($-4,841.33).
- Amounts keyed wrong, as recorded and as cleared: ACH770130 ($-2,683.01 recorded, $-2,638.01 cleared), ACH770291 ($-6,323.53 recorded, $-6,322.53 cleared), ACH770037 ($-5,034.17 recorded, $-5,033.17 cleared).

### Journal Entries Needed

Card fees, the service fee, interest, the returned check (back to the customer's receivable), reversal of the two duplicates, and corrections for the three keying errors. Deposits in transit and outstanding checks need no entry.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Matching | 25 | Checks and ACH matched on reference, deposits matched many to one by batch, card settlements matched net of fees. |
| Reconciling items | 25 | Outstanding checks, both in-transit items, fees, interest, and the returned check, each with the right sign. |
| Error detection | 20 | Finds both duplicate entries and all three keying errors. |
| Balance | 15 | Adjusted balances agree at $1,299,644.07. |
| Journal entries and controls | 10 | Entries for every book-side item, and two sensible controls. |
| Workbook clarity and AI transparency | 5 | Matching logic visible. An AI log, if used, at the Strong level. |

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
| Treating August's checks as September outstanding items | Reconciliation off by $6,585.88 | Did not use Prior_Outstanding |
| Matching card settlements on amount | Every card batch looks unmatched | Did not notice the fee deduction |
| Forcing the difference into one plug | The books stay wrong | Gave up on finding the items |
| Recording deposits in transit as book entries | Double counting next month | Confused timing with errors |

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

1. How did you match the customer receipts to the bank deposits?
2. How did you find the keying errors?
3. Which items need a journal entry, and which don't?
