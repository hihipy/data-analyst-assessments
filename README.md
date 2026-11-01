# Data Analyst Assessments

[![Link Check](https://github.com/hihipy/data-analyst-assessments/actions/workflows/links.yml/badge.svg)](https://github.com/hihipy/data-analyst-assessments/actions/workflows/links.yml)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

**Built with**

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://html.spec.whatwg.org)
[![KaTeX](https://img.shields.io/badge/KaTeX-329894?style=flat&logoColor=white)](https://katex.org)
[![Mermaid](https://img.shields.io/badge/Mermaid-FF3670?style=flat&logo=mermaid&logoColor=white)](https://mermaid.js.org)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)

Take-home assessments for data analysts, from easy to hard, in two tracks: one for people who work in spreadsheets and one for people who work in code. Each assessment comes with its own dataset, instructions, and an answer key for whoever does the grading.

---

## Why This Exists

Most take-home tests for analysts fall into one of two traps. Some are so small and tidy that they only show whether someone can build a pivot table. Others hand over a single messy file and call that hard. Neither looks much like real work, where data is spread across several files, arrives with problems nobody mentioned, and has to be turned into a decision someone can act on.

Most tests also either ban AI tools or say nothing about them. Neither choice reflects how analysts work now.

---

## The Assessments

| Track | Level | Assessment | Setting | Time Limit |
| --- | --- | --- | --- | --- |
| Spreadsheet | Easy | [Online Store Order Review](01_spreadsheet/01_easy/online_store_order_review/) | E-commerce | 45 minutes |
| Spreadsheet | Easy | [Clinic Appointment Review](01_spreadsheet/01_easy/clinic_appointment_review/) | Healthcare | 45 minutes |
| Spreadsheet | Easy | [Department Budget Review](01_spreadsheet/01_easy/department_budget_review/) | Finance | 45 minutes |
| Spreadsheet | Easy | [Sales Dashboard Critique](01_spreadsheet/01_easy/sales_dashboard_critique/) | Technology sales | 45 minutes |
| Spreadsheet | Easy | [Website Conversion Funnel Review](01_spreadsheet/01_easy/web_funnel_review/) | Marketing | 45 minutes |
| Spreadsheet | Medium | [Sales Commission Review](01_spreadsheet/02_medium/sales_commission_review/) | Software sales | 90 minutes |
| Spreadsheet | Medium | [Hospital Length of Stay and Readmissions](01_spreadsheet/02_medium/hospital_stay_review/) | Healthcare | 90 minutes |
| Spreadsheet | Medium | [Bank Reconciliation](01_spreadsheet/02_medium/bank_reconciliation/) | Banking | 90 minutes |
| Spreadsheet | Medium | [Employee Survey Analysis](01_spreadsheet/02_medium/employee_survey_analysis/) | Human resources | 90 minutes |
| Spreadsheet | Medium | [New Location Business Case](01_spreadsheet/02_medium/expansion_business_case/) | Restaurants | 90 minutes |
| Spreadsheet | Hard | [Inventory Reorder Planning](01_spreadsheet/03_hard/inventory_reorder_planning/) | Distribution | 3 hours |
| Spreadsheet | Hard | [Emergency Department Throughput and Staffing](01_spreadsheet/03_hard/emergency_department_review/) | Healthcare | 3 hours |
| Spreadsheet | Hard | [Checkout A/B Test Review](01_spreadsheet/03_hard/checkout_ab_test_review/) | Marketing | 3 hours |
| Spreadsheet | Hard | [Price Elasticity Review](01_spreadsheet/03_hard/price_elasticity_review/) | Grocery retail | 3 hours |
| Spreadsheet | Hard | [Production Quality Review](01_spreadsheet/03_hard/production_quality_review/) | Manufacturing | 3 hours |
| Code | Easy | [Coffee Shop Sales Review](02_code/01_easy/coffee_shop_sales_review/) | Retail | 60 minutes |
| Code | Easy | [Pharmacy Claims Review](02_code/01_easy/pharmacy_claims_review/) | Healthcare | 60 minutes |
| Code | Easy | [Parcel Delivery Review](02_code/01_easy/parcel_delivery_review/) | Logistics | 60 minutes |
| Code | Easy | [Support Ticket Review](02_code/01_easy/support_ticket_review/) | Customer support | 60 minutes |
| Code | Easy | [Open-Ended Sales Question](02_code/01_easy/open_ended_sales_question/) | E-commerce | 60 minutes |
| Code | Medium | [Regional Admissions Funnel Review](02_code/02_medium/regional_admissions_funnel_review/) | Education | 2 hours |
| Code | Medium | [Specialist Referral Follow-Through](02_code/02_medium/specialist_referral_review/) | Healthcare | 2 hours |
| Code | Medium | [Subscription Cohort Review](02_code/02_medium/subscription_cohort_review/) | Marketing | 2 hours |
| Code | Medium | [Delivery Zone Coverage](02_code/02_medium/delivery_zone_coverage/) | Grocery delivery | 2 hours |
| Code | Medium | [Customer Segmentation](02_code/02_medium/customer_segmentation/) | Grocery retail | 2 hours |
| Code | Hard | [Workforce Attrition and Pay Review](02_code/03_hard/workforce_attrition_and_pay_review/) | Human resources | 4 hours |
| Code | Hard | [Inpatient Deterioration Early Warning](02_code/03_hard/deterioration_early_warning/) | Healthcare | 4 hours |
| Code | Hard | [Warehouse Demand Forecasting](02_code/03_hard/demand_forecasting/) | Manufacturing and distribution | 4 hours |
| Code | Hard | [Store Program Impact Evaluation](02_code/03_hard/program_impact_evaluation/) | Retail | 4 hours |
| Code | Hard | [Card Fraud Detection](02_code/03_hard/card_fraud_detection/) | Banking | 4 hours |

Each name links to its folder.

**Spreadsheet track:** every part can be done in [Excel](https://www.microsoft.com/microsoft-365/excel), [Google Sheets](https://workspace.google.com/products/sheets/), [LibreOffice Calc](https://www.libreoffice.org/discover/calc/), [Numbers](https://www.apple.com/numbers/), or similar. The data comes as a single workbook (`.xlsx`). Candidates who prefer code can use it.

**Code track:** the data is too large for a spreadsheet, so candidates work in a programming language of their choice, such as [Julia](https://julialang.org), [Python](https://www.python.org), [R](https://www.r-project.org), or SQL. Notebooks like [Jupyter](https://jupyter.org), [marimo](https://marimo.io), [Pluto](https://plutojl.org), and [Quarto](https://quarto.org) are welcome. The data files are CSVs compressed with [gzip](https://www.gnu.org/software/gzip/) (`.csv.gz`), which most tools read directly.

## Find an Assessment by Skill

Every assessment tests several skills. This table lists the ones where each skill is central, so you can pick the assessments that fit a role. Every assessment also asks for a written summary or recommendation, so communication is tested throughout.

| Skill | What It Covers | Assessments |
| --- | --- | --- |
| Aggregation and pivot tables | Totals, averages, and breakdowns by group | [Online Store Order Review](01_spreadsheet/01_easy/online_store_order_review/), [Clinic Appointment Review](01_spreadsheet/01_easy/clinic_appointment_review/), [Department Budget Review](01_spreadsheet/01_easy/department_budget_review/), [Coffee Shop Sales Review](02_code/01_easy/coffee_shop_sales_review/), [Pharmacy Claims Review](02_code/01_easy/pharmacy_claims_review/) |
| Rates and denominators | Choosing what to divide by, and what to leave out | [Clinic Appointment Review](01_spreadsheet/01_easy/clinic_appointment_review/), [Online Store Order Review](01_spreadsheet/01_easy/online_store_order_review/), [Hospital Length of Stay and Readmissions](01_spreadsheet/02_medium/hospital_stay_review/), [Regional Admissions Funnel Review](02_code/02_medium/regional_admissions_funnel_review/), [Parcel Delivery Review](02_code/01_easy/parcel_delivery_review/), [Website Conversion Funnel Review](01_spreadsheet/01_easy/web_funnel_review/) |
| Data cleaning and validation | Duplicates, bad values, mixed formats, and records that contradict each other | [Sales Commission Review](01_spreadsheet/02_medium/sales_commission_review/), [Hospital Length of Stay and Readmissions](01_spreadsheet/02_medium/hospital_stay_review/), [Employee Survey Analysis](01_spreadsheet/02_medium/employee_survey_analysis/), [Inventory Reorder Planning](01_spreadsheet/03_hard/inventory_reorder_planning/), [Emergency Department Throughput and Staffing](01_spreadsheet/03_hard/emergency_department_review/), [Delivery Zone Coverage](02_code/02_medium/delivery_zone_coverage/), [Workforce Attrition and Pay Review](02_code/03_hard/workforce_attrition_and_pay_review/), [Website Conversion Funnel Review](01_spreadsheet/01_easy/web_funnel_review/), [Production Quality Review](01_spreadsheet/03_hard/production_quality_review/) |
| Joining and matching records | Lookups across files, and matching records that do not line up one to one | [Sales Commission Review](01_spreadsheet/02_medium/sales_commission_review/), [Bank Reconciliation](01_spreadsheet/02_medium/bank_reconciliation/), [Pharmacy Claims Review](02_code/01_easy/pharmacy_claims_review/), [Regional Admissions Funnel Review](02_code/02_medium/regional_admissions_funnel_review/), [Workforce Attrition and Pay Review](02_code/03_hard/workforce_attrition_and_pay_review/) |
| Dates, time zones, and time windows | Date math, daylight saving, and what was true on a given date | [Sales Commission Review](01_spreadsheet/02_medium/sales_commission_review/), [Hospital Length of Stay and Readmissions](01_spreadsheet/02_medium/hospital_stay_review/), [Emergency Department Throughput and Staffing](01_spreadsheet/03_hard/emergency_department_review/), [Parcel Delivery Review](02_code/01_easy/parcel_delivery_review/), [Workforce Attrition and Pay Review](02_code/03_hard/workforce_attrition_and_pay_review/) |
| Reshaping event data | Turning logs and line items into one row per customer, package, or transaction | [Coffee Shop Sales Review](02_code/01_easy/coffee_shop_sales_review/), [Pharmacy Claims Review](02_code/01_easy/pharmacy_claims_review/), [Parcel Delivery Review](02_code/01_easy/parcel_delivery_review/), [Subscription Cohort Review](02_code/02_medium/subscription_cohort_review/) |
| Incomplete or censored data | Partial periods, outcomes not yet known, and demand hidden by stockouts | [Coffee Shop Sales Review](02_code/01_easy/coffee_shop_sales_review/), [Regional Admissions Funnel Review](02_code/02_medium/regional_admissions_funnel_review/), [Specialist Referral Follow-Through](02_code/02_medium/specialist_referral_review/), [Subscription Cohort Review](02_code/02_medium/subscription_cohort_review/), [Warehouse Demand Forecasting](02_code/03_hard/demand_forecasting/), [Card Fraud Detection](02_code/03_hard/card_fraud_detection/), [Open-Ended Sales Question](02_code/01_easy/open_ended_sales_question/) |
| Financial analysis | Budgets, reconciliations, commissions, and pricing | [Department Budget Review](01_spreadsheet/01_easy/department_budget_review/), [Bank Reconciliation](01_spreadsheet/02_medium/bank_reconciliation/), [Sales Commission Review](01_spreadsheet/02_medium/sales_commission_review/), [Price Elasticity Review](01_spreadsheet/03_hard/price_elasticity_review/), [Pharmacy Claims Review](02_code/01_easy/pharmacy_claims_review/), [New Location Business Case](01_spreadsheet/02_medium/expansion_business_case/) |
| Operations and capacity | Inventory, staffing, beds, appointment slots, and coverage | [Inventory Reorder Planning](01_spreadsheet/03_hard/inventory_reorder_planning/), [Emergency Department Throughput and Staffing](01_spreadsheet/03_hard/emergency_department_review/), [Hospital Length of Stay and Readmissions](01_spreadsheet/02_medium/hospital_stay_review/), [Specialist Referral Follow-Through](02_code/02_medium/specialist_referral_review/), [Delivery Zone Coverage](02_code/02_medium/delivery_zone_coverage/) |
| Forecasting | Projecting what comes next and measuring forecast error | [Regional Admissions Funnel Review](02_code/02_medium/regional_admissions_funnel_review/), [Inventory Reorder Planning](01_spreadsheet/03_hard/inventory_reorder_planning/), [Warehouse Demand Forecasting](02_code/03_hard/demand_forecasting/) |
| Experiments and statistical testing | Confidence intervals, significance, and margins of error | [Checkout A/B Test Review](01_spreadsheet/03_hard/checkout_ab_test_review/), [Employee Survey Analysis](01_spreadsheet/02_medium/employee_survey_analysis/) |
| Causal inference | Measuring an effect without a randomized test | [Store Program Impact Evaluation](02_code/03_hard/program_impact_evaluation/), [Checkout A/B Test Review](01_spreadsheet/03_hard/checkout_ab_test_review/) |
| Regression | Estimating drivers and sensitivities | [Price Elasticity Review](01_spreadsheet/03_hard/price_elasticity_review/), [Store Program Impact Evaluation](02_code/03_hard/program_impact_evaluation/) |
| Predictive modeling and leakage | Building models only from what was known at the time | [Workforce Attrition and Pay Review](02_code/03_hard/workforce_attrition_and_pay_review/), [Inpatient Deterioration Early Warning](02_code/03_hard/deterioration_early_warning/), [Card Fraud Detection](02_code/03_hard/card_fraud_detection/), [Warehouse Demand Forecasting](02_code/03_hard/demand_forecasting/) |
| Cohorts and lifetime value | Retention curves, acquisition cost, and payback | [Subscription Cohort Review](02_code/02_medium/subscription_cohort_review/) |
| Clustering | Finding and validating groups | [Customer Segmentation](02_code/02_medium/customer_segmentation/) |
| Survey analysis | Weighting, reverse-coded items, and small groups | [Employee Survey Analysis](01_spreadsheet/02_medium/employee_survey_analysis/) |
| Text data | Categorizing free text | [Support Ticket Review](02_code/01_easy/support_ticket_review/) |
| Geospatial analysis | Distance, coverage, and choosing a location | [Delivery Zone Coverage](02_code/02_medium/delivery_zone_coverage/) |
| Financial modeling and scenarios | Building a model from assumptions, with sensitivity and risk | [New Location Business Case](01_spreadsheet/02_medium/expansion_business_case/) |
| Statistical process control | Control charts, process capability, and root causes | [Production Quality Review](01_spreadsheet/03_hard/production_quality_review/) |
| Scoping an open-ended question | Defining a vague request, stating assumptions, and answering plainly | [Open-Ended Sales Question](02_code/01_easy/open_ended_sales_question/) |
| Dashboard and chart design | Checking a dashboard and building a clearer one | [Sales Dashboard Critique](01_spreadsheet/01_easy/sales_dashboard_critique/) |

---

## How They Work

- **Instructions as a web page:** each assessment is a single HTML file that opens in any browser, works offline, and can be sent as an email attachment. It adapts to phones, dark mode, and printing, and typesets its formulas with [KaTeX](https://katex.org).
- **Column descriptions, not answers:** the instructions describe each data file and show how the files connect in a [Mermaid](https://mermaid.js.org) diagram, but never show the values. Candidates have to open and explore the data themselves.
- **Problems hidden in the data:** duplicates, mixed date formats, missing days, mismatched units, and records that contradict each other. Spotting them is part of the test, and the harder levels hide more of them.
- **Difficulty from judgment:** the easy assessments test careful calculation. The hard ones test whether someone can tell what was true on a given date, avoid using information from the future, and explain their choices.
- **AI allowed, with a log:** candidates may use AI assistants for any part of the work. If they do, they submit a short log of the tools used, example prompts, and how they checked the results.

---

## Using an Assessment

**If you're hiring:**

1. Pick an assessment from [the table above](#the-assessments).
2. Send the candidate the HTML instructions and the data files from that folder.
3. Keep the answer key to yourself.
4. Score the submission with the rubric in the answer key, then use its follow-up questions in the interview.

**If you're practicing:**

1. Open the HTML instructions and work through the assessment within the time limit.
2. Compare your work with the answer key afterward.

---

## Answer Keys

Each assessment has an answer key with:

- The expected results for every part, so a grader can check numbers without redoing the work.
- A 100-point scoring rubric, with what full marks require for each part.
- The common mistakes, what each one does to the results, and what it usually says about the person who made it.
- Guidance on judging AI use, based on transparency and checking rather than whether AI was used.
- Follow-up questions for an interview.

The hard code-track assessments also include a Python script, `reference_solution.py`, that reproduces every figure in the key from the data files. The forecasting assessment's key also holds the actual demand for the forecast weeks, so a candidate's forecast can be scored.

---

## About the Data

All data is synthetic. The people, stores, schools, and companies are invented, and so are the exchange rates. Any resemblance to a real organization is a coincidence.

---

## Project Structure

Assessments are grouped by track, then by level, with each assessment in its own folder, so a level can hold more than one.

<!-- tree:start -->
```
data-analyst-assessments/
├── 01_spreadsheet/
│   ├── 01_easy/
│   │   ├── clinic_appointment_review/
│   │   │   ├── clinic_appointment_answer_key.md         # Answer key
│   │   │   ├── clinic_appointment_review.html           # Instructions
│   │   │   └── clinic_appointments.xlsx                 # Data
│   │   ├── department_budget_review/
│   │   │   ├── department_budget_answer_key.md          # Answer key
│   │   │   ├── department_budget_data.xlsx              # Data
│   │   │   └── department_budget_review.html            # Instructions
│   │   ├── online_store_order_review/
│   │   │   ├── online_store_answer_key.md               # Answer key
│   │   │   ├── online_store_order_review.html           # Instructions
│   │   │   └── online_store_orders.xlsx                 # Data
│   │   ├── sales_dashboard_critique/
│   │   │   ├── regional_sales_dashboard.xlsx            # Data
│   │   │   ├── sales_dashboard_answer_key.md            # Answer key
│   │   │   └── sales_dashboard_critique.html            # Instructions
│   │   └── web_funnel_review/
│   │       ├── web_funnel_answer_key.md                 # Answer key
│   │       ├── web_funnel_data.xlsx                     # Data
│   │       └── web_funnel_review.html                   # Instructions
│   ├── 02_medium/
│   │   ├── bank_reconciliation/
│   │   │   ├── bank_reconciliation.html                 # Instructions
│   │   │   ├── bank_reconciliation_answer_key.md        # Answer key
│   │   │   └── bank_reconciliation_data.xlsx            # Data
│   │   ├── employee_survey_analysis/
│   │   │   ├── employee_survey_analysis.html            # Instructions
│   │   │   ├── employee_survey_answer_key.md            # Answer key
│   │   │   └── employee_survey_data.xlsx                # Data
│   │   ├── expansion_business_case/
│   │   │   ├── expansion_business_case.html             # Instructions
│   │   │   ├── expansion_business_case_answer_key.md    # Answer key
│   │   │   └── expansion_model_inputs.xlsx              # Data
│   │   ├── hospital_stay_review/
│   │   │   ├── hospital_stay_answer_key.md              # Answer key
│   │   │   ├── hospital_stay_review.html                # Instructions
│   │   │   └── hospital_stays_data.xlsx                 # Data
│   │   └── sales_commission_review/
│   │       ├── sales_commission_answer_key.md           # Answer key
│   │       ├── sales_commission_data.xlsx               # Data
│   │       └── sales_commission_review.html             # Instructions
│   └── 03_hard/
│       ├── checkout_ab_test_review/
│       │   ├── checkout_ab_test_answer_key.md           # Answer key
│       │   ├── checkout_ab_test_data.xlsx               # Data
│       │   └── checkout_ab_test_review.html             # Instructions
│       ├── emergency_department_review/
│       │   ├── ed_throughput_data.xlsx                  # Data
│       │   ├── emergency_department_answer_key.md       # Answer key
│       │   └── emergency_department_review.html         # Instructions
│       ├── inventory_reorder_planning/
│       │   ├── inventory_answer_key.md                  # Answer key
│       │   ├── inventory_planning_data.xlsx             # Data
│       │   └── inventory_reorder_planning.html          # Instructions
│       ├── price_elasticity_review/
│       │   ├── price_elasticity_answer_key.md           # Answer key
│       │   ├── price_elasticity_data.xlsx               # Data
│       │   └── price_elasticity_review.html             # Instructions
│       └── production_quality_review/
│           ├── production_quality_answer_key.md         # Answer key
│           ├── production_quality_data.xlsx             # Data
│           └── production_quality_review.html           # Instructions
├── 02_code/
│   ├── 01_easy/
│   │   ├── coffee_shop_sales_review/
│   │   │   ├── answer_key/
│   │   │   │   └── coffee_answer_key.md                 # Answer key
│   │   │   ├── coffee_shop_sales_review.html            # Instructions
│   │   │   └── data/                                    # Data (.csv.gz)
│   │   ├── open_ended_sales_question/
│   │   │   ├── answer_key/
│   │   │   │   └── open_ended_sales_answer_key.md       # Answer key
│   │   │   ├── data/                                    # Data (.csv.gz)
│   │   │   └── open_ended_sales_question.html           # Instructions
│   │   ├── parcel_delivery_review/
│   │   │   ├── answer_key/
│   │   │   │   └── parcel_delivery_answer_key.md        # Answer key
│   │   │   ├── data/                                    # Data (.csv.gz)
│   │   │   └── parcel_delivery_review.html              # Instructions
│   │   ├── pharmacy_claims_review/
│   │   │   ├── answer_key/
│   │   │   │   └── pharmacy_claims_answer_key.md        # Answer key
│   │   │   ├── data/                                    # Data (.csv.gz)
│   │   │   └── pharmacy_claims_review.html              # Instructions
│   │   └── support_ticket_review/
│   │       ├── answer_key/
│   │       │   └── support_ticket_answer_key.md         # Answer key
│   │       ├── data/                                    # Data (.csv.gz)
│   │       └── support_ticket_review.html               # Instructions
│   ├── 02_medium/
│   │   ├── customer_segmentation/
│   │   │   ├── answer_key/
│   │   │   │   └── customer_segmentation_answer_key.md  # Answer key
│   │   │   ├── customer_segmentation.html               # Instructions
│   │   │   └── data/                                    # Data (.csv.gz)
│   │   ├── delivery_zone_coverage/
│   │   │   ├── answer_key/
│   │   │   │   └── delivery_zone_answer_key.md          # Answer key
│   │   │   ├── data/                                    # Data (.csv.gz)
│   │   │   └── delivery_zone_coverage.html              # Instructions
│   │   ├── regional_admissions_funnel_review/
│   │   │   ├── answer_key/
│   │   │   │   └── admissions_answer_key.md             # Answer key
│   │   │   ├── data/                                    # Data (.csv.gz)
│   │   │   └── regional_admissions_funnel_review.html   # Instructions
│   │   ├── specialist_referral_review/
│   │   │   ├── answer_key/
│   │   │   │   └── specialist_referral_answer_key.md    # Answer key
│   │   │   ├── data/                                    # Data (.csv.gz)
│   │   │   └── specialist_referral_review.html          # Instructions
│   │   └── subscription_cohort_review/
│   │       ├── answer_key/
│   │       │   └── subscription_cohort_answer_key.md    # Answer key
│   │       ├── data/                                    # Data (.csv.gz)
│   │       └── subscription_cohort_review.html          # Instructions
│   └── 03_hard/
│       ├── card_fraud_detection/
│       │   ├── answer_key/
│       │   │   ├── card_fraud_answer_key.md             # Answer key
│       │   │   └── reference_solution.py                # Reproduces the answer key
│       │   ├── card_fraud_detection.html                # Instructions
│       │   └── data/                                    # Data (.csv.gz)
│       ├── demand_forecasting/
│       │   ├── answer_key/
│       │   │   ├── demand_forecasting_answer_key.md     # Answer key
│       │   │   ├── future_actuals.csv.gz
│       │   │   └── reference_solution.py                # Reproduces the answer key
│       │   ├── data/                                    # Data (.csv.gz)
│       │   └── demand_forecasting.html                  # Instructions
│       ├── deterioration_early_warning/
│       │   ├── answer_key/
│       │   │   ├── deterioration_answer_key.md          # Answer key
│       │   │   └── reference_solution.py                # Reproduces the answer key
│       │   ├── data/                                    # Data (.csv.gz)
│       │   └── deterioration_early_warning.html         # Instructions
│       ├── program_impact_evaluation/
│       │   ├── answer_key/
│       │   │   ├── program_impact_answer_key.md         # Answer key
│       │   │   └── reference_solution.py                # Reproduces the answer key
│       │   ├── data/                                    # Data (.csv.gz)
│       │   └── program_impact_evaluation.html           # Instructions
│       └── workforce_attrition_and_pay_review/
│           ├── answer_key/
│           │   ├── reference_solution.py                # Reproduces the answer key
│           │   └── workforce_answer_key.md              # Answer key
│           ├── data/                                    # Data (.csv.gz)
│           └── workforce_attrition_and_pay_review.html  # Instructions
├── LICENSE.md
└── README.md
```
<!-- tree:end -->

---

## License

This project is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). The full text is in [LICENSE.md](LICENSE.md).

You are free to:
- Use, share, and adapt this work
- Use it at your job

Under these terms:
- **Attribution:** Credit the original author
- **NonCommercial:** No selling or commercial products
- **ShareAlike:** Derivatives must use the same license
