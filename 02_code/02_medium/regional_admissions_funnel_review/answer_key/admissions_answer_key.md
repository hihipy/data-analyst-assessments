# Answer Key: Regional Admissions Funnel Review

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Medium, code track | 2 hours |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs.

The forecasts below pace each school against last year, the method the exercise is built to reward. Other defensible methods should land close to these figures.

## What This Assessment Measures

Rebuilding a partial-cycle position from dated records, forecasting with a defensible method, applying capacity limits, separating volume problems from conversion problems, and judging marketing efficiency with incomplete attribution.

## Expected Results

### The Files

| File | Rows | Grain |
| --- | ---: | --- |
| `admissions_prospects.csv.gz` | 4,018 | One row per prospect, both cycles, including 12 duplicates |
| `admissions_web_sessions.csv.gz` | 1,232,943 | One row per website session, both cycles; 2,871 sessions carry a `prospect_id` |
| `admissions_school_targets.csv.gz` | 6 | One row per school |
| `admissions_marketing_spend.csv.gz` | 161 | One row per month, school, and source |

Every figure below comes from aggregating these files. "At March 31" for 2024-25 means a date on or before 2025-03-31.

### Part 1: Data Traps

| Issue | Where | Why It Matters |
| --- | --- | --- |
| Duplicate rows | 12 exact duplicates in `admissions_prospects.csv.gz`, all 2025-26, each repeating a `prospect_id` | Left in, they inflate current-cycle counts. |
| Blank source | 85 current-cycle prospects (43 applications, 16 deposits) have no `source`, and none has a linked web session | Their channel cannot be recovered. Source-level results cover attributed prospects only, and a strong answer says so. Spend is fully attributed, so cost per deposit by source still uses all spend. |
| Budget enrollment exceeds seat capacity | School E: budget 110, capacity 105 | The budget cannot be met. The real ceiling is 105. |
| Forecast exceeds seat capacity | School D: forecast about 54, capacity 50 | Extra demand becomes a waitlist, not revenue. |
| Deposits are not enrollments | 2024-25 has 447 deposits but 418 enrolled | Pacing must divide deposits at March 31 by final enrollment, not by final deposits, or the forecast overstates enrollment. |
| Partial cycle | 2025-26 runs only to March 31 | Comparing to-date counts with full-year budgets understates every school. |

### Part 2: Conversion (Percent, Whole Numbers)

| School | Inq to App YTD | Inq to App LY | App to Dep YTD | App to Dep LY | Inq to Dep YTD | Inq to Dep LY |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| A | 42 | 42 | 27 | 27 | 11 | 11 |
| B | 41 | 47 | 20 | 27 | 8 | 13 |
| C | 38 | 40 | 29 | 30 | 11 | 12 |
| D | 41 | 42 | 34 | 29 | 14 | 12 |
| E | 40 | 40 | 30 | 30 | 12 | 12 |
| F | 32 | 41 | 25 | 30 | 8 | 12 |

LY means last year at March 31. Diagnosis:

- **School B** has a conversion problem. Inquiries are up 30 percent on last year's pace, but app-to-deposit fell from 27 to 20 percent.
- **School C** has a volume problem. Inquiries are down 30 percent on last year's pace, and conversion is roughly flat.
- **School F** has both problems. Inquiries are down 22 percent and every conversion step fell. It is the worst school by any reasonable measure.
- **School D** is the best performer on conversion and pace.

### Part 3: Forecast (Pacing Against Last Year)

Forecast = YTD ÷ (last year's March 31 figure ÷ last year's final figure), for each funnel stage.

| School | Forecast Inquiries | Forecast Enroll | Budget | Capacity | Gap to Budget | Additional Inquiries Needed |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| A | 475 | 81 | 90 | 100 | −9 | 54 |
| B | 375 | 46 | 60 | 70 | −14 | 118 |
| C | 275 | 48 | 75 | 85 | −27 | 155 |
| D | 273 | 54, capped at 50 | 45 | 50 | +5 | None |
| E | 622 | 109, capped at 105 | 110 | 105 | −5, unreachable | Not a volume issue |
| F | 265 | 31 | 65 | 75 | −34 | 290 |

The capped regional forecast is about 361 enrollments against a budget of 445. Net tuition at risk is about $1.45 million: A −$171,000, B −$300,000, C −$459,000, D +$123,000, E −$98,000, F −$543,000.

Realism test: School F is forecast to add about 77 more inquiries before the cycle ends (265 forecast minus 188 to date). Reaching budget needs 290 on top of the forecast, nearly four times what the rest of the cycle is expected to bring. A strong answer says F's budget is out of reach and the fix is conversion, not volume.

### Part 4: Cost per Deposit by Source (Attributed Prospects Only)

| Source | Inquiries | Deposits | Cost per Inquiry | Cost per Deposit |
| --- | ---: | ---: | ---: | ---: |
| Referral | 140 | 34 | $43 | $176 |
| Organic Web | 180 | 25 | $50 | $360 |
| Campus Events | 210 | 38 | $150 | $829 |
| Paid Search | 520 | 41 | $138 | $1,756 |
| Social Media | 410 | 22 | $107 | $2,000 |
| Third-Party Lists | 100 | 4 | $240 | $6,000 |

These figures slightly overstate cost per deposit, because the 16 deposits with no source belong to some of these channels. The ranking is clear enough that it does not change the recommendation.

**Session-to-inquiry conversion, 2025-26:** Referral 0.64 percent, Campus Events 0.56 percent, Third-Party Lists 0.34 percent, Paid Search 0.27 percent, Social Media 0.23 percent, Organic Web 0.12 percent, across 494,562 sessions. Organic Web converts worst per session but is cheap per deposit, because it costs little. Sessions are a volume measure, and cost per deposit remains the decision measure. Not every inquiry has a session: campus event and referral inquiries often arrive offline, so session conversion understates those two channels.

The remaining full-year budget is $87,500. A strong reallocation moves money out of third-party lists and social media and into events and referral programs. It points the money at Schools C and A, where volume is the constraint, rather than School F, where conversion is. It should also say that average cost per deposit understates marginal cost, because referral and organic channels do not scale linearly with spend.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Data checks | 15 | Finds the 12 duplicates, the 85 blank sources, budget over capacity at School E, and the deposits-versus-enrollment gap. |
| Conversion and diagnosis | 20 | Rebuilds the March 31, 2025 position from dates. Names B as a conversion problem, C as a volume problem, and F as both. |
| Forecasting | 25 | Paces against last year or uses an equally defensible method, caps D and E at capacity, and lands within about 10 percent of the key's capped total of 361. |
| Marketing efficiency | 15 | Cost per deposit by source and school, session conversion treated as a volume measure, and a reallocation that matches the cause of each school's gap. |
| Recommendations and communication | 15 | Executive summary leads with the revenue at risk, and each recommendation is tied to a number. |
| Reproducibility and AI transparency | 10 | Code or notebook reruns from the CSV files. An AI log, if used, at the Strong level. |

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
| Comparing to-date counts with full-year budgets | Every school looks far behind | Missed that the cycle is partial; the key trap |
| Forecasting from deposits as if they were enrollments | Forecasts run about 7 percent high | Did not check melt between deposit and enrollment |
| Ignoring seat capacity | D forecast at 54 against 50 seats; E's budget treated as reachable | Read the targets file without checking it against capacity |
| Leaving duplicates in | Current-cycle counts slightly high | Skipped the data check |
| Silently dropping blank sources | Source results presented as complete | Did not disclose a known gap |
| Pushing more inquiry volume at School F | Money spent on the wrong lever | Did not separate volume from conversion |

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

1. Walk me through how you rebuilt last year's March 31 position.
2. Your forecast for School F is far below budget. What would you tell its director first?
3. Why did you allocate the $40,000 the way you did, and what would change your mind?
4. Which forecast are you least confident in, and what data would firm it up?
