# Answer Key: Sales Commission Review

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Medium, spreadsheet track | 90 minutes |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs.

## What This Assessment Measures

Lookups across sheets, prorating quotas by dates, applying marginal commission tiers correctly, cleaning deal data, and weighting a pipeline by probability.

## Expected Results

### Part 1: Data Problems

| Problem | Rows | Handling |
| --- | ---: | --- |
| Exact duplicate deals | 24 | Remove; each repeats a Closed Won deal and would inflate bookings |
| Deals whose `rep_id` is not on the Reps sheet (R199, R207) | 42 | Exclude from commission and flag; they include $75,300 of won bookings |
| Close date before created date | 16 (9 won, 7 lost) | Exclude and flag as data errors |
| Won deals closed after the rep's end date | 16 | No commission, per the rules; $555,200 of bookings |

Excluding the close-before-created rows is a judgment call. A candidate who keeps them and says so is also acceptable, and the totals shift slightly.

### Part 2: Commissions

Bookings are Closed Won deals closed in 2025, after removing the problems above. Commission uses marginal tiers: 4 percent on bookings up to 50 percent of quota, 8 percent from 50 to 100 percent, and 12 percent above 100 percent.

| Rep | Name | Months | Prorated Quota | Bookings | Attainment | Commission |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| R101 | Avery Collins | 12 | $1,400,000 | $635,100 | 45.4% | $25,404 |
| R102 | Jordan Lindqvist | 12 | $1,000,000 | $764,600 | 76.5% | $41,168 |
| R103 | Riley Sato | 12 | $1,100,000 | $842,600 | 76.6% | $45,408 |
| R104 | Morgan Patel | 12 | $1,100,000 | $289,200 | 26.3% | $11,568 |
| R105 | Casey Moreau | 12 | $1,000,000 | $1,059,400 | 105.9% | $67,128 |
| R106 | Taylor Delgado | 7 | $583,333 | $457,300 | 78.4% | $24,917 |
| R107 | Quinn Nguyen | 12 | $1,200,000 | $1,644,500 | 137.0% | $125,340 |
| R108 | Reese Tanaka | 12 | $1,100,000 | $521,600 | 47.4% | $20,864 |
| R109 | Skyler Novak | 12 | $1,000,000 | $3,676,100 | 367.6% | $381,132 |
| R110 | Drew Okafor | 12 | $1,100,000 | $1,174,000 | 106.7% | $74,880 |
| R111 | Rowan Brennan | 12 | $1,200,000 | $355,000 | 29.6% | $14,200 |
| R112 | Emerson Hughes | 12 | $1,200,000 | $3,791,400 | 315.9% | $382,968 |
| R113 | Hayden Ramirez | 12 | $1,100,000 | $145,100 | 13.2% | $5,804 |
| R114 | Parker Castillo | 12 | $1,200,000 | $518,000 | 43.2% | $20,720 |
| R115 | Sawyer Mensah | 7 | $700,000 | $395,600 | 56.5% | $17,648 |
| R116 | Logan Kowalski | 12 | $1,400,000 | $1,439,000 | 102.8% | $88,680 |
| R117 | Blake Fischer | 12 | $1,200,000 | $2,186,800 | 182.2% | $190,416 |
| R118 | Cameron Romano | 12 | $900,000 | $1,359,600 | 151.1% | $109,152 |
| R119 | Dakota Haddad | 12 | $1,200,000 | $2,898,400 | 241.5% | $275,808 |
| R120 | Finley Abara | 12 | $1,100,000 | $991,300 | 90.1% | $57,304 |
| R121 | Avery Okafor | 12 | $1,100,000 | $1,230,500 | 111.9% | $81,660 |
| R122 | Jordan Brennan | 12 | $1,100,000 | $1,274,400 | 115.9% | $86,928 |
| R123 | Riley Hughes | 6 | $500,000 | $401,800 | 80.4% | $22,144 |
| R124 | Morgan Ramirez | 12 | $1,000,000 | $774,600 | 77.5% | $41,968 |
| R125 | Casey Castillo | 12 | $1,200,000 | $570,900 | 47.6% | $22,836 |
| R126 | Taylor Mensah | 12 | $1,200,000 | $1,610,900 | 134.2% | $121,308 |
| R127 | Quinn Kowalski | 12 | $1,100,000 | $1,602,100 | 145.6% | $126,252 |
| R128 | Reese Fischer | 12 | $900,000 | $359,600 | 40.0% | $14,384 |
| R129 | Skyler Romano | 12 | $1,100,000 | $828,700 | 75.3% | $44,296 |
| R130 | Drew Haddad | 12 | $1,100,000 | $2,529,100 | 229.9% | $237,492 |
| R131 | Rowan Abara | 12 | $1,200,000 | $2,457,400 | 204.8% | $222,888 |
| R132 | Emerson Collins | 7 | $816,667 | $958,400 | 117.4% | $66,008 |
| R133 | Hayden Lindqvist | 6 | $700,000 | $311,700 | 44.5% | $12,468 |
| R134 | Parker Sato | 7 | $583,333 | $269,800 | 46.3% | $10,792 |
| R135 | Sawyer Patel | 5 | $416,667 | $234,200 | 56.2% | $10,403 |
| R136 | Logan Moreau | 8 | $800,000 | $474,500 | 59.3% | $21,960 |
| R137 | Blake Delgado | 7 | $700,000 | $915,400 | 130.8% | $67,848 |
| R138 | Cameron Nguyen | 6 | $700,000 | $531,400 | 75.9% | $28,512 |
| R139 | Dakota Tanaka | 10 | $833,333 | $1,456,600 | 174.8% | $124,792 |
| R140 | Finley Novak | 8 | $666,667 | $1,255,900 | 188.4% | $110,708 |

Total commission is $3,456,156 on $45,192,500 of bookings. Nineteen reps finished at or above 100 percent.

**The common mistake:** applying a single rate to all bookings based on the final tier gives $4,837,156, overpaying by $1,381,000.

### Part 3: Win Rates (Deals Closed in 2025)

| Product Line | Win Rate | Closed Deals |
| --- | ---: | ---: |
| Services | 53.6% | 966 |
| Analytics Add-On | 47.9% | 1,306 |
| Core Platform | 36.7% | 2,050 |
| Security Suite | 30.5% | 810 |

By region the spread is narrow: Central 43.6%, Northeast 42.2%, West 41.1%, Southeast 39.9%. Product line explains more of the difference than region.

### Part 4: Pipeline

| Stage | Deals | Value | Weighted Value |
| --- | ---: | ---: | ---: |
| Negotiation | 114 | $2,830,000 | $1,839,500 |
| Proposal | 234 | $4,851,400 | $1,697,990 |
| Prospecting | 285 | $7,163,800 | $716,380 |
| Total | 633 | $14,845,200 | $4,253,870 |

First-quarter quota for the 37 active reps is $10,525,000. Weighted coverage is 40.4 percent: the pipeline is not strong enough. Unweighted coverage is 141.0 percent, which looks healthy and is the trap. Eight of the open deals belong to the unknown reps R199 and R207.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Data checks | 15 | Finds the 24 duplicates, the 42 deals for unknown reps, the 16 date errors, and the 16 deals closed after a rep left. |
| Proration | 15 | Months employed are correct for the 9 new hires and the 3 leavers. |
| Marginal tiers | 20 | Total commission near $3,456,156. Flat-rate logic is the main failure. |
| Win rates | 10 | Won over won plus lost, by product line and region, for deals closed in 2025. |
| Pipeline | 15 | Weighted Q1 pipeline of $4,253,870 and 40.4 percent coverage, with the unweighted 141 percent called out as misleading. |
| Recommendations | 15 | Two recommendations, each tied to a number, for example pipeline coverage or the Security Suite win rate. |
| Workbook clarity and AI transparency | 10 | Lookups and tier logic visible in formulas. An AI log, if used, at the Strong level. |

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
| Applying one rate to all bookings | Commission overpaid by $1,381,000 | Misread the plan; the key trap |
| Not prorating quotas | New hires look like underperformers | Ignored hire and end dates |
| Paying leavers on deals closed after they left | $555,200 of ineligible bookings paid | Missed a written rule |
| Reporting unweighted pipeline | Coverage of 141 percent instead of 40.4 percent | Did not apply stage probabilities |
| Dropping unknown-rep deals without flagging them | $75,300 of won bookings disappears unexplained | Hid a data problem instead of escalating it |

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

1. Show me one rep's commission calculated by hand, band by band.
2. The VP asks why the pipeline looked fine last week. What do you say?
3. Who should decide what happens to the deals owned by R199 and R207?
