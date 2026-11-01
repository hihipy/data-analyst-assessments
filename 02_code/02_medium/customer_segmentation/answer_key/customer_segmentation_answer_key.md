# Answer Key: Customer Segmentation

Spoilers: for reviewers only.

| Level | Time Limit |
| --- | --- |
| Medium, code track | 2 hours |

## How to Use This Key

Score each submission against the rubric, using the expected results to check the numbers. Small differences from rounding or from a stated, reasonable choice are fine. The common mistakes table shows what each error usually reveals about the candidate, and the interview questions test whether the work is truly theirs. All data is synthetic.

## What This Assessment Measures

Feature engineering from transactions, scaling and outliers in clustering, choosing and validating the number of segments, and turning clusters into marketing actions.

## Expected Results

### Part 1: Features and Data Problems

- **Returns:** 40,395 rows with negative amounts. Net them out of spend; leave them out of order counts and basket size.
- **Business accounts:** 40 customers spend far more than anyone else and account for all of the top 40 spenders. Set them aside as their own group before clustering.
- **Scale:** spend runs in thousands while shares run from 0 to 1. Without log transforms and standardization, spend dominates the clusters.

### Part 2: Segments

Silhouette scores by number of clusters (scaled features, business accounts removed): 3: 0.44, 4: 0.536, 5: 0.618, 6: 0.599, 7: 0.462, 8: 0.397. Five segments score highest.

| Segment | Share of Customers | Share of Spend | Days Since Last Order | Orders per Month | Average Basket | Promotion Use | Online Share |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Weekly Regulars | 30.2% | 53.0% | 6 | 4.06 | $58 | 15% | 25% |
| Monthly Stock-Up | 18.0% | 25.1% | 23 | 0.97 | $201 | 20% | 55% |
| Deal Seekers | 21.9% | 12.2% | 12 | 1.89 | $40 | 70% | 35% |
| Lapsed | 14.9% | 4.6% | 355 | 0.63 | $63 | 25% | 29% |
| New Online | 15.0% | 5.2% | 9 | 2.73 | $74 | 19% | 92% |

The data was simulated from five shopper types. A scaled five-cluster model recovers them almost exactly (adjusted Rand index 0.998), and refitting on half the customers gives the same segments (index 1.0). Clustering the raw features with business accounts included scores 0.293.

### Part 3: What a Good Answer Says

- **Weekly regulars drive revenue:** about 30 percent of customers and over half of spend. Protect them with loyalty, not discounts.
- **Lapsed customers are most at risk:** no order in almost a year. Win them back, or stop spending on them.
- **Deal seekers use promotions on most orders:** target them with promotions, and don't discount to the others.
- **New online customers are young accounts:** onboarding and a second-order offer matter most.

## Scoring Rubric (100 Points)

| Criterion | Points | Full Marks Require |
| --- | ---: | --- |
| Features | 25 | Customer-level features with returns handled and business accounts set aside. |
| Clustering | 25 | Scaled features, a justified number of segments, and a stability check. |
| Profiles | 25 | Sizes, spend shares, and names that match the behavior. |
| Recommendations | 15 | One action per segment, with revenue priority and risk identified. |
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
| Clustering unscaled features | Segments split on spend alone | Did not scale; the key trap |
| Leaving business accounts in | A few huge accounts pull the clusters off center | Did not look for outliers |
| Picking the number of segments without evidence | Segments may not be real | Skipped validation |
| Naming segments by cluster number | Marketing cannot use them | Did not translate the analysis |

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

1. Why did you scale the features?
2. How did you choose five segments?
3. Which segment would you invest in first?
