# Tata Trent AI Analytics

A retail intelligence and analytics project focused on Tata Trent brands such as Westside and Zudio. The project includes a dashboard-style web experience for product analytics, pricing intelligence, and operational insights supported by AI-driven retail analysis.

## Overview

This repository contains a browser-based dashboard and a data-processing workflow designed to:

- ingest retail/market data from PDF sources
- extract relevant information from documents
- clean and normalize the extracted data
- analyze product, pricing, and inventory patterns
- present insights in a dashboard for business review

The current repository includes:

- a front-end dashboard in HTML/JavaScript
- a PDF file used as part of the data extraction workflow
- a README that documents the setup and data pipeline

## Project Goals

- automate extraction from PDF and structured retail reports
- support AI-assisted business analysis for retail performance
- create an interactive dashboard for decision-makers
- build a repeatable data pipeline from raw documents to insights

## Tech Stack

- Python for data extraction, transformation, and analysis
- PDF parsing libraries such as PyMuPDF, pdfplumber, or tabula-py
- Pandas for cleaning and preprocessing
- Jupyter Notebook for exploratory analysis
- HTML, Tailwind CSS, and Chart.js for dashboard visualization

## Folder Structure

```text
.
├── README.md
├── Trent AI DATA ANALYSISER .html
├── Trent_AI_GitHub_Profile_Showcase.pdf
└── (future Python scripts / notebooks / data folders)
```

## Python Setup

Use Python 3.10+ for the analysis workflow.

### 1) Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install required packages

```bash
pip install --upgrade pip
pip install pandas numpy matplotlib seaborn plotly openpyxl pdfplumber pymupdf jupyter notebook
```

Optional packages depending on the extraction method:

```bash
pip install tabula-py camelot-py[cv]
```

### 3) Run a notebook or script

```bash
jupyter notebook
```

Or run a Python file:

```bash
python your_script.py
```

## PDF Extraction Workflow

The recommended pipeline is:

1. Load the PDF file
2. Extract text and table content
3. Clean and structure the output into rows and columns
4. Validate missing values and duplicates
5. Save the processed output into CSV/Excel/JSON
6. Feed the cleaned dataset into the dashboard or analytics notebook

### Example Python extraction flow

```python
import pandas as pd
import fitz

pdf_path = "Trent_AI_GitHub_Profile_Showcase.pdf"

doc = fitz.open(pdf_path)
text_chunks = []

for page in doc:
    text = page.get_text("text")
    text_chunks.append(text)

raw_text = "\n".join(text_chunks)
print(raw_text[:1000])
```

## Data Processing Branches After PDF Extraction

After extracting data from the PDF, the workflow can branch into multiple analytics tracks:

### 1) Data Cleaning Branch
- remove duplicate rows
- standardize product names and categories
- fix formatting and missing values
- validate numeric columns

### 2) Product Analytics Branch
- SKU-level analysis
- category performance review
- brand comparisons
- product mix and assortment analysis

### 3) Pricing Intelligence Branch
- compare price points across categories
- detect discount patterns
- calculate margin or value perception
- assess promotional impact

### 4) Inventory and Demand Branch
- stock health review
- deadstock detection
- replenishment opportunities
- seasonal demand patterns

### 5) Customer and Store Insights Branch
- store-level trends
- conversion and basket patterns
- customer demand segmentation
- merchandising strategy recommendations

### 6) Dashboard Reporting Branch
- export cleaned data for the front-end dashboard
- create charts and KPIs for reports
- share insights for business review and decision-making

### 7) Sales Performance Branch
- track revenue and sales contribution by brand, category, and channel
- identify growth opportunities and weak segments
- compare store and product performance over time

### 8) Merchandising Strategy Branch
- optimize assortment mix and product placement
- analyze bundle and cross-sell opportunities
- improve display and category strategy

### 9) Forecasting and Planning Branch
- build demand trend forecasts
- support inventory planning and seasonal readiness
- improve procurement and markdown decisions

### 10) AI Recommendation Branch
- recommend personalized or data-driven product suggestions
- score products using demand and pricing signals
- support smarter operational decision-making

## Dashboard Usage

Open the HTML dashboard in a browser to view the retail analytics interface:

```bash
xdg-open "Trent AI DATA ANALYSISER .html"
```

If the dashboard uses local assets or external data, make sure the files are served from the project folder or the data sources are available in the expected location.

## Suggested Next Steps

- build a Python script to extract tables from the PDF
- convert extracted content into a structured CSV dataset
- create an analytics notebook to visualize trends and KPIs
- connect the cleaned dataset to the dashboard
- extend the project with more AI-driven product recommendations

## Contributing

This project is intended for retail analytics experimentation and business intelligence exploration. Contributions, improvements, and additional extraction pipelines are welcome.

## License

This project is currently provided for internal learning and analytics use. Update the license if you plan to distribute it externally.
