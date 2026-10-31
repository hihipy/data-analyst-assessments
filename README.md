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
| Spreadsheet | Easy | Online Store Order Review | E-commerce | 45 minutes |
| Spreadsheet | Medium | Sales Commission Review | Software sales | 90 minutes |
| Spreadsheet | Hard | Inventory Reorder Planning | Distribution | 3 hours |
| Code | Easy | Coffee Shop Sales Review | Retail | 60 minutes |
| Code | Medium | Regional Admissions Funnel Review | Education | 2 hours |
| Code | Hard | Workforce Attrition and Pay Review | Human resources | 4 hours |

**Spreadsheet track:** every part can be done in Excel, Google Sheets, LibreOffice Calc, Numbers, or similar. The data comes as a single workbook (`.xlsx`). Candidates who prefer code can use it.

**Code track:** the data is too large for a spreadsheet, so candidates work in a programming language of their choice, such as Julia, Python, R, or SQL. Notebooks like Jupyter, marimo, Pluto, and Quarto are welcome. The data files are compressed CSVs (`.csv.gz`), which most tools read directly.

---

## How They Work

- **Instructions as a web page:** each assessment is a single HTML file that opens in any browser, works offline, and can be sent as an email attachment. It adapts to phones, dark mode, and printing.
- **Column descriptions, not answers:** the instructions describe each data file and show how the files connect in a diagram, but never show the values. Candidates have to open and explore the data themselves.
- **Problems hidden in the data:** duplicates, mixed date formats, missing days, mismatched units, and records that contradict each other. Spotting them is part of the test, and the harder levels hide more of them.
- **Difficulty from judgment:** the easy assessments test careful calculation. The hard ones test whether someone can tell what was true on a given date, avoid using information from the future, and explain their choices.
- **AI allowed, with a log:** candidates may use AI assistants for any part of the work. If they do, they submit a short log of the tools used, example prompts, and how they checked the results.

---

## Using an Assessment

**If you're hiring:**

1. Pick an assessment from the table above.
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

The hard code-track assessment also includes a Python script that reproduces every figure in its key from the data files.

---

## About the Data

All data is synthetic. The people, stores, schools, and companies are invented, and so are the exchange rates. Any resemblance to a real organization is a coincidence.

---

## Project Structure

```
data-analyst-assessments/
├── 01_spreadsheet/
│   ├── 01_easy/online_store_order_review/
│   ├── 02_medium/sales_commission_review/
│   └── 03_hard/inventory_reorder_planning/
└── 02_code/
    ├── 01_easy/coffee_shop_sales_review/
    ├── 02_medium/regional_admissions_funnel_review/
    └── 03_hard/workforce_attrition_and_pay_review/
```

Each spreadsheet-track folder holds the HTML instructions, the workbook, and the answer key. Each code-track folder holds the HTML instructions, a `data` folder, and an `answer_key` folder.

---

## License

This project is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

You are free to:
- Use, share, and adapt this work
- Use it at your job

Under these terms:
- **Attribution:** Credit the original author
- **NonCommercial:** No selling or commercial products
- **ShareAlike:** Derivatives must use the same license
