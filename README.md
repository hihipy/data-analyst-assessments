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
| Spreadsheet | Medium | [Sales Commission Review](01_spreadsheet/02_medium/sales_commission_review/) | Software sales | 90 minutes |
| Spreadsheet | Medium | [Hospital Length of Stay and Readmissions](01_spreadsheet/02_medium/hospital_stay_review/) | Healthcare | 90 minutes |
| Spreadsheet | Hard | [Inventory Reorder Planning](01_spreadsheet/03_hard/inventory_reorder_planning/) | Distribution | 3 hours |
| Spreadsheet | Hard | [Emergency Department Throughput and Staffing](01_spreadsheet/03_hard/emergency_department_review/) | Healthcare | 3 hours |
| Code | Easy | [Coffee Shop Sales Review](02_code/01_easy/coffee_shop_sales_review/) | Retail | 60 minutes |
| Code | Easy | [Pharmacy Claims Review](02_code/01_easy/pharmacy_claims_review/) | Healthcare | 60 minutes |
| Code | Medium | [Regional Admissions Funnel Review](02_code/02_medium/regional_admissions_funnel_review/) | Education | 2 hours |
| Code | Medium | [Specialist Referral Follow-Through](02_code/02_medium/specialist_referral_review/) | Healthcare | 2 hours |
| Code | Hard | [Workforce Attrition and Pay Review](02_code/03_hard/workforce_attrition_and_pay_review/) | Human resources | 4 hours |
| Code | Hard | [Inpatient Deterioration Early Warning](02_code/03_hard/deterioration_early_warning/) | Healthcare | 4 hours |

Each name links to its folder.

**Spreadsheet track:** every part can be done in [Excel](https://www.microsoft.com/microsoft-365/excel), [Google Sheets](https://workspace.google.com/products/sheets/), [LibreOffice Calc](https://www.libreoffice.org/discover/calc/), [Numbers](https://www.apple.com/numbers/), or similar. The data comes as a single workbook (`.xlsx`). Candidates who prefer code can use it.

**Code track:** the data is too large for a spreadsheet, so candidates work in a programming language of their choice, such as [Julia](https://julialang.org), [Python](https://www.python.org), [R](https://www.r-project.org), or SQL. Notebooks like [Jupyter](https://jupyter.org), [marimo](https://marimo.io), [Pluto](https://plutojl.org), and [Quarto](https://quarto.org) are welcome. The data files are CSVs compressed with [gzip](https://www.gnu.org/software/gzip/) (`.csv.gz`), which most tools read directly.

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

The hard code-track assessments also include a Python script, `reference_solution.py`, that reproduces every figure in the key from the data files.

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
│   │   └── online_store_order_review/
│   │       ├── online_store_answer_key.md               # Answer key
│   │       ├── online_store_order_review.html           # Instructions
│   │       └── online_store_orders.xlsx                 # Data
│   ├── 02_medium/
│   │   ├── hospital_stay_review/
│   │   │   ├── hospital_stay_answer_key.md              # Answer key
│   │   │   ├── hospital_stay_review.html                # Instructions
│   │   │   └── hospital_stays_data.xlsx                 # Data
│   │   └── sales_commission_review/
│   │       ├── sales_commission_answer_key.md           # Answer key
│   │       ├── sales_commission_data.xlsx               # Data
│   │       └── sales_commission_review.html             # Instructions
│   └── 03_hard/
│       ├── emergency_department_review/
│       │   ├── ed_throughput_data.xlsx                  # Data
│       │   ├── emergency_department_answer_key.md       # Answer key
│       │   └── emergency_department_review.html         # Instructions
│       └── inventory_reorder_planning/
│           ├── inventory_answer_key.md                  # Answer key
│           ├── inventory_planning_data.xlsx             # Data
│           └── inventory_reorder_planning.html          # Instructions
├── 02_code/
│   ├── 01_easy/
│   │   ├── coffee_shop_sales_review/
│   │   │   ├── answer_key/
│   │   │   │   └── coffee_answer_key.md                 # Answer key
│   │   │   ├── coffee_shop_sales_review.html            # Instructions
│   │   │   └── data/                                    # Data (.csv.gz)
│   │   └── pharmacy_claims_review/
│   │       ├── answer_key/
│   │       │   └── pharmacy_claims_answer_key.md        # Answer key
│   │       ├── data/                                    # Data (.csv.gz)
│   │       └── pharmacy_claims_review.html              # Instructions
│   ├── 02_medium/
│   │   ├── regional_admissions_funnel_review/
│   │   │   ├── answer_key/
│   │   │   │   └── admissions_answer_key.md             # Answer key
│   │   │   ├── data/                                    # Data (.csv.gz)
│   │   │   └── regional_admissions_funnel_review.html   # Instructions
│   │   └── specialist_referral_review/
│   │       ├── answer_key/
│   │       │   └── specialist_referral_answer_key.md    # Answer key
│   │       ├── data/                                    # Data (.csv.gz)
│   │       └── specialist_referral_review.html          # Instructions
│   └── 03_hard/
│       ├── deterioration_early_warning/
│       │   ├── answer_key/
│       │   │   ├── deterioration_answer_key.md          # Answer key
│       │   │   └── reference_solution.py                # Reproduces the answer key
│       │   ├── data/                                    # Data (.csv.gz)
│       │   └── deterioration_early_warning.html         # Instructions
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
