# Answer Key: Checkout A/B Test Review

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Hard, spreadsheet track | 3 hours |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs. All data is synthetic.

## What This Assessment Measures

Experiment validity checks, the right unit of analysis, two-proportion tests and intervals, guardrail metrics, and time effects.

## Expected Results

### Part 1: Problems With the Test

| Problem | Size | Correct Handling |
| --- | ---: | --- |
| Users seen in both variants | 390 users | Exclude; their exposure is mixed |
| Bots: users with 30 or more sessions and no orders | 25 users, 1,997 sessions | Exclude |
| Sample ratio mismatch | 29,805 A users against 27,887 B, chi-square 63.8, p about 1.3e-15 | Find the cause before reading any result |

The mismatch comes from Android. From September 8 to 14, no Android users were recorded in B, while A kept recording them. The share of Android users in B falls to zero on those days, then jumps to about 60 percent on September 15 and 16, as B users whose earlier visits were lost reappear as if they were new. Excluding Android users first seen in that week from both arms restores the split: 27,605 against 27,887, p = 0.231.

The unit of randomization is the user, so results must be per user, not per session. Session-level conversion is 3.61 against 3.94 percent, which mixes up visits and people.

### Part 2: Results

| Measure | A | B | Difference |
| --- | ---: | ---: | ---: |
| Conversion per user, with the logging bug | 6.87% | 7.33% | +0.46 points (+6.7%), p = 0.0309 |
| Conversion per user, cleaned | 7.05% | 7.33% | +0.28 points (+4.0%), 95% CI -0.15 to 0.71, p = 0.2015 |
| Revenue per user, cleaned | $5.44 | $5.28 | 95% CI $-0.52 to $0.19 |
| Average order value, cleaned | $77.21 | $72.02 | -6.7% |

Lift by week of first visit: week 1 +10.9%, week 2 +8.3%, week 3 +6.4%, week 4 -8.3%. The lift fades from about 11 percent in week 1 to negative in week 4, the pattern of a novelty effect.

Lift by device: iOS +3.3%, Android +2.2%, Desktop +6.7%.

### Part 3: What a Good Recommendation Says

- **The "win" is mostly the bug.** Dropping Android users from B removed low-converting users from one arm only. With that fixed, the lift is 4.0 percent, the confidence interval includes zero, and p = 0.2015.
- **Revenue does not improve.** B's orders are about 7 percent smaller, so revenue per user is slightly lower in B.
- **The lift is fading.** Week 4 is negative.
- **Do not ship B.** Fix the logging, then rerun for at least four clean weeks with revenue per user as a guardrail metric.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Validity checks | 25 | Runs the sample ratio check, traces the mismatch to Android in September 8 to 14, and excludes it symmetrically. |
| Data cleaning | 15 | Removes users in both variants and bots, and aggregates to users. |
| Inference | 25 | Lift near 4 percent with a confidence interval spanning zero and p near 0.20 after cleaning. |
| Guardrails and time effects | 15 | Shows lower order value, flat revenue per user, and the lift fading by week. |
| Recommendation | 15 | Does not ship; proposes a rerun with clear success criteria. |
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
| Skipping the sample ratio check | Reports a significant 6.7 percent lift that is mostly the bug | Trusted the randomization; the key trap |
| Analyzing sessions instead of users | Wrong denominator and overstated precision | Ignored the unit of randomization |
| Excluding the bug window from B only | Still biased | Did not keep the arms comparable |
| Ignoring revenue per user | Ships a change that does not raise revenue | Looked at one metric |
| Pooling all four weeks without a time view | Misses the novelty effect | Did not check stability |

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

1. How did you find where the split went wrong?
2. Why analyze users rather than sessions?
3. What would make you ship B after a rerun?
