# Answer Key: Delivery Zone Coverage

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Medium, code track | 2 hours |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs. All data is synthetic.

## What This Assessment Measures

Cleaning coordinates, great-circle distance, coverage analysis, and a simple location search with stated assumptions.

## Expected Results

### Part 1: Data Problems

| Problem | Rows | Correct Handling |
| --- | ---: | --- |
| Latitude and longitude swapped | 5,492 | Swap back; latitude cannot be below -90 |
| Coordinates of 0, 0 | 2,200 | Exclude; that point is in the Atlantic Ocean |
| Store ST17 has a positive longitude | 1 store | Flip the sign; as recorded, it is in China, and every distance to it is wrong |

### Part 2: Distance and Delivery

| Distance Band | Share of Orders | On Time |
| --- | ---: | ---: |
| 0 to 3 km | 68.5% | 99.2% |
| 3 to 5 km | 16.3% | 92.1% |
| 5 to 8 km | 6.1% | 53.9% |
| over 8 km | 9.0% | 15.7% |

Overall, 87.8 percent of orders were on time. The share of orders more than 5 km from their store rose every month, from 2.6 percent in January to 25.8 percent in September. The far orders cluster in one area about 16 km west and 18 km north of the city center, where demand grew from nothing in January.

### Part 3: New Store

The best single site, chosen by searching a 0.5 km grid for the point that brings the most third-quarter orders within 3 km, is near latitude 33.6122, longitude -112.2429. It would move 34,206 third-quarter orders (9.1 percent) within 3 km.

Using the parameters' travel model, estimated on-time delivery for the third quarter rises from 86.5 to 99.1 percent. The model has no traffic or batching, so the actual third-quarter rate was lower (81.7 percent); a strong answer says the estimate is optimistic and focuses on the size of the gain.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Data checks | 20 | Fixes swapped coordinates, drops zeros, and corrects store ST17. |
| Distance and delivery | 25 | On-time by distance band, and the monthly rise in far orders. |
| Finding the gap | 20 | Locates the growing northwest area far from any store. |
| New store | 25 | A justified site near the key's, the orders it brings within 3 km, and a caveated on-time estimate. |
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
| Using Euclidean distance on raw degrees | Distances distorted east to west | Did not convert coordinates |
| Missing the store with the wrong sign | Its orders look thousands of kilometers away | Did not sanity-check the stores |
| Siting the store at the city center | Adds capacity where it is not needed | Followed density, not the gap |
| Presenting the travel-model estimate as a promise | Overstates the gain | Ignored the model's limits |

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

1. How did you find the coordinate problems?
2. How did you choose the new store's location?
3. What would make your on-time estimate wrong?
