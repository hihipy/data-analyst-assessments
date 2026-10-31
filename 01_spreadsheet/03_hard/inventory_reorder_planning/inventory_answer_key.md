# Answer Key: Inventory Reorder Planning

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Hard, spreadsheet track | 3 hours |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs.

## What This Assessment Measures

Rebuilding a complete daily demand series from sparse data, unit conversion, standard reorder math, cost trade-offs, and writing a decision memo that names the risks.

## Expected Results

### Part 1: Data Problems

| Problem | Where | Effect If Missed |
| --- | --- | --- |
| Zero-demand days have no row | `Daily_Demand`: 38,890 rows instead of 150 × 365 | Averaging the rows overstates daily demand (median overstatement 35 percent) and understates variability. With row averages, 28 SKUs look due for an order instead of 18. |
| Quantities recorded in cases | 772 rows across 9 SKUs, January to April: SKU-1001, 1025, 1042, 1057, 1070, 1082, 1109, 1114, 1134 | Those SKUs' demand is understated unless CS is multiplied by `case_pack`. |
| Customer returns | 233 negative rows, −641 units | Returns are not demand; exclude them (netting them in is acceptable if stated). |
| Duplicate SKU in the master | SKU-1017 appears twice, at $4.24 and $4.75 | Lookups return whichever comes first; flag it. This key uses $4.24. |
| Discontinued SKU with an open order | SKU-1149, PO-7056 for 240 units | Do not reorder; recommend cancelling the PO. |

Daily demand uses calendar days, per the Parameters sheet: annual units ÷ 365. Standard deviation is taken over all 365 days, zeros included.

### Part 2: ABC Classification (149 Active SKUs)

| Class | SKUs | Annual Value |
| --- | ---: | ---: |
| A | 53 | $8,102,502 |
| B | 46 | $1,572,387 |
| C | 50 | $509,320 |

Counts can move by one SKU at each boundary depending on whether the SKU that crosses 80 percent is counted as A. Either convention is fine if stated.

### Part 3 and Part 4: Reorder Plan

Eighteen active SKUs have an inventory position at or below their reorder point. Order value at the rounded economic order quantity is $117,680.06. Total safety stock across active SKUs is worth $263,579.

| SKU | Class | Supplier | Inventory Position | Reorder Point | Order Quantity | Order Value |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| SKU-1113 | A | S03 | 213 | 564.9 | 204 | $16,264.92 |
| SKU-1041 | C | S03 | 65 | 79.5 | 500 | $16,030.00 |
| SKU-1050 | A | S03 | 396 | 1,125.0 | 370 | $13,764.00 |
| SKU-1129 | A | S05 | 548 | 662.9 | 400 | $11,228.00 |
| SKU-1018 | B | S01 | 31 | 54.0 | 500 | $9,910.00 |
| SKU-1104 | A | S05 | 150 | 322.2 | 216 | $7,842.96 |
| SKU-1010 | A | S02 | 160 | 225.0 | 300 | $6,291.00 |
| SKU-1098 | B | S02 | 647 | 842.1 | 1,150 | $5,037.00 |
| SKU-1084 | B | S03 | 486 | 945.9 | 1,224 | $4,308.48 |
| SKU-1107 | B | S05 | 196 | 365.1 | 490 | $4,292.40 |
| SKU-1003 | B | S04 | 175 | 188.7 | 500 | $4,265.00 |
| SKU-1148 | B | S03 | 157 | 450.9 | 500 | $4,015.00 |
| SKU-1076 | C | S01 | 99 | 104.8 | 380 | $3,260.40 |
| SKU-1132 | C | S03 | 193 | 215.2 | 350 | $3,097.50 |
| SKU-1130 | C | S02 | 52 | 143.4 | 450 | $2,781.00 |
| SKU-1074 | C | S03 | 230 | 251.0 | 480 | $2,534.40 |
| SKU-1075 | C | S02 | 199 | 262.5 | 1,050 | $1,638.00 |
| SKU-1036 | C | S05 | 103 | 110.1 | 700 | $1,120.00 |

A strong answer notices that for several SKUs, such as SKU-1113 and SKU-1050, one order quantity does not lift the inventory position back above the reorder point, and either orders more or flags it. It also notices that SKU-1041's minimum order of 500 units is close to a year of demand.

**Stockout risk:** 18 SKUs have less on hand than their expected demand over the lead time. Eight have open purchase orders that lift their inventory position above the reorder point. The other ten are on the order-now list. A strong answer checks whether each open order arrives before stock runs out.

| SKU | Class | Days of Cover On Hand | Lead Time (Days) | Open PO |
| --- | --- | ---: | ---: | --- |
| SKU-1074 | C | 7.3 | 37 | Yes |
| SKU-1133 | A | 7.4 | 26 | Yes |
| SKU-1030 | B | 7.6 | 17 | Yes |
| SKU-1018 | B | 8.3 | 10 | No |
| SKU-1016 | C | 8.7 | 12 | Yes |
| SKU-1061 | A | 10.0 | 11 | Yes |
| SKU-1130 | C | 11.1 | 21 | No |
| SKU-1055 | B | 13.2 | 22 | Yes |
| SKU-1103 | A | 15.3 | 27 | Yes |
| SKU-1052 | C | 15.4 | 26 | Yes |
| SKU-1113 | A | 17.4 | 38 | No |
| SKU-1050 | A | 17.5 | 36 | No |
| SKU-1148 | B | 18.7 | 38 | No |
| SKU-1010 | A | 19.3 | 22 | No |
| SKU-1104 | A | 19.8 | 30 | No |
| SKU-1107 | B | 20.8 | 26 | No |
| SKU-1084 | B | 20.8 | 33 | No |
| SKU-1128 | B | 21.6 | 27 | Yes |

### Part 5: Price Breaks (Supplier S03)

All 28 S03 SKUs are cheaper at a price-break quantity than at the economic order quantity at base cost. The total annual saving is $151,773, about $112,000 of it from four SKUs: SKU-1105 ($54,455), SKU-1050 ($21,146), SKU-1113 ($18,198), and SKU-1043 ($17,901). A strong answer weighs the saving against the extra inventory carried and the S03 lead-time risk in Part 6.

### Part 6: Scenario

Adding 7 days to every S03 lead time requires $8,401 of additional safety stock across the 28 S03 SKUs.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Demand rebuild | 25 | Fills zero-demand days, converts cases to units, excludes returns, and divides by 365 calendar days. |
| ABC classification | 10 | 53, 46, and 50 SKUs in A, B, and C, within one SKU at each boundary. |
| Reorder parameters | 20 | Safety stock, reorder point, and EOQ correct, with case-pack and minimum-order rounding. |
| Reorder plan | 15 | 18 SKUs to order now for $117,680.06, the discontinued SKU excluded, and stockout risks listed. |
| Price breaks and scenario | 15 | S03 saving near $151,773 and $8,401 of added safety stock, with the two parts connected. |
| Memo | 10 | One page, leads with the decision, and names the risks and the decisions needed from the VP. |
| Workbook clarity and AI transparency | 5 | Formulas traceable on a large sheet. An AI log, if used, at the Strong level. |

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
| Averaging only the rows that exist | Daily demand about 35 percent high; 28 SKUs flagged instead of 18 | Did not notice missing zero days; the key trap |
| Ignoring the uom column | 9 SKUs' demand understated | Did not profile the data |
| Leaving open orders out of inventory position | Too many orders placed | Misapplied the reorder rule |
| Reordering the discontinued SKU | Dead stock | Did not use the status column |
| Taking every price break with no caveat | Cash tied up with a supplier whose lead times are slipping | Did not connect Parts 5 and 6 |

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

1. How did you work out that zero-demand days were missing?
2. SKU-1041 has a 500-unit minimum, close to a year of demand. What would you recommend?
3. If the VP could approve only half the order value, how would you prioritize?
