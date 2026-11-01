# Answer Key: Subscription Cohort Review

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Medium, code track | 2 hours |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs. All data is synthetic.

## What This Assessment Measures

Cohort construction, retention with right-censoring, revenue recognition for annual plans, and unit economics by channel.

## Expected Results

### Part 1: Data Problems

| Problem | Rows | Correct Handling |
| --- | ---: | --- |
| Duplicate renewal events | 7,000 | Remove; they double revenue |
| Acquisition channel in lowercase | 3,000 customers | Standardize; there are 10 raw values for 5 channels |
| Refunds within 14 days | 5,990 | Cancel the payment they follow; the customer never retained |
| Customers who cancelled and came back | 3,635 | Same customer, not a new one; counting them as new lowers acquisition cost slightly |

### Part 2: Retention

Retention must be measured only on cohorts old enough. Counting every customer at month 12, including those who signed up less than a year ago, gives 29.1 percent instead of **51.0 percent**.

| Channel | Month 1 | Month 3 | Month 6 | Month 12 |
| --- | ---: | ---: | ---: | ---: |
| Referral | 88.3% | 83.7% | 77.3% | 69.6% |
| Organic | 90.0% | 84.1% | 76.1% | 62.2% |
| Paid Search | 88.4% | 80.2% | 70.3% | 53.3% |
| Social Ads | 84.0% | 72.6% | 59.2% | 39.5% |
| Affiliate | 83.7% | 71.4% | 57.9% | 37.2% |
| All | 86.9% | 78.1% | 67.6% | 51.0% |

### Part 3: Unit Economics

| Paid Channel | Acquisition Cost | 12-Month Value | Value to Cost | Payback Month |
| --- | ---: | ---: | ---: | ---: |
| Referral | $24.90 | $198.99 | 7.99 | 2 |
| Affiliate | $60.49 | $153.12 | 2.53 | 4 |
| Social Ads | $70.96 | $155.66 | 2.19 | 5 |
| Paid Search | $95.73 | $177.03 | 1.85 | 6 |

Organic customers cost nothing to acquire and are worth $188.40 in their first year.

### Part 4: What a Good Answer Says

- **Referral is the best channel** by far: the highest retention and value, at a quarter of Paid Search's cost.
- **Paid Search has the weakest return** of the paid channels, 1.85 times its cost, even though its customers stay better than Social or Affiliate customers. The problem is its price.
- **Social Ads and Affiliate customers churn fastest,** losing about 60 percent within a year, but their low cost keeps them above 2 times.
- **Before cutting a channel,** check whether its customers would arrive another way, and whether its cost rises as spend grows.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Data checks | 15 | Removes duplicate renewals, standardizes channels, applies refunds, and treats reactivations as returning customers. |
| Retention | 25 | A correct cohort table, with each month measured only on cohorts old enough; 12-month retention near 51 percent. |
| Unit economics | 25 | Acquisition cost, 12-month value, ratio, and payback by paid channel matching the key. |
| Recommendations | 25 | Shifts budget toward Referral, and questions Paid Search on price rather than quality. |
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
| Measuring 12-month retention on all customers | 29.1 percent instead of 51.0 percent | Missed right-censoring; the key trap |
| Keeping duplicate renewals | Revenue and value overstated | Skipped the data check |
| Booking annual payments in month one | Early-month value overstated, payback too fast | Confused cash with revenue |
| Comparing channels on retention alone | Misses that Paid Search's problem is cost | Ignored acquisition cost |

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

1. How did you decide which cohorts count at month 12?
2. Why does Paid Search look weak even though its customers stay?
3. What would you test before moving budget to Referral?
