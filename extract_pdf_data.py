#!/usr/bin/env python3
"""Extract text from a PDF and prepare a structured data file for analysis.

This script creates a simple, repeatable pipeline for the project:
1. read PDF text
2. split content into page/line records
3. store raw text and CSV output
4. ready the cleaned dataset for downstream analysis branches
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
import fitz


def extract_pdf_lines(pdf_path: Path) -> list[dict]:
    """Return a list of page/line records extracted from the PDF."""
    doc = fitz.open(pdf_path)
    rows: list[dict] = []

    for page_number in range(doc.page_count):
        page = doc[page_number]
        text = page.get_text("text")
        for line in text.splitlines():
            cleaned = line.strip()
            if cleaned:
                rows.append(
                    {
                        "page": page_number + 1,
                        "line_text": cleaned,
                    }
                )

    doc.close()
    return rows


def write_outputs(rows: list[dict], output_dir: Path) -> tuple[Path, Path]:
    """Write raw text and CSV outputs to disk."""
    output_dir.mkdir(parents=True, exist_ok=True)

    raw_text_path = output_dir / "pdf_extracted_text.txt"
    csv_path = output_dir / "pdf_extracted_data.csv"

    with raw_text_path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(f"Page {row['page']}: {row['line_text']}\n")

    df = pd.DataFrame(rows)
    df.to_csv(csv_path, index=False)
    return raw_text_path, csv_path


def build_analysis_branches(rows: list[dict]) -> dict[str, list[str]]:
    """Summarize the possible downstream analysis branches after extraction."""
    text_blob = "\n".join(row["line_text"] for row in rows)
    lower_text = text_blob.lower()

    branches = {
        "data_cleaning": [
            "remove duplicate rows and empty fields",
            "normalize brands, categories, and product names",
            "fix inconsistent formatting and missing values",
        ],
        "product_analytics": [
            "compare products by category and brand",
            "identify top-selling and low-performing SKUs",
            "review assortment performance",
        ],
        "pricing_intelligence": [
            "compare price points and discount patterns",
            "evaluate value perception and margin opportunities",
            "track promotional sensitivity",
        ],
        "inventory_demand": [
            "review stock health and deadstock risk",
            "monitor replenishment and seasonal demand signals",
            "flag product gaps and supply issues",
        ],
        "customer_store_insights": [
            "analyze store-level performance patterns",
            "segment demand behavior and merchandising outcomes",
            "link customer trends to product assortment",
        ],
        "sales_performance": [
            "compare sales contribution by channel and region",
            "monitor revenue trend and conversion trends",
            "identify high-velocity and underperforming categories",
        ],
        "merchandising_strategy": [
            "optimize product placement and assortment mix",
            "review category adjacency and bundle opportunities",
            "evaluate display and promotion effectiveness",
        ],
        "forecasting_and_planning": [
            "predict demand using trend and seasonality signals",
            "plan procurement and markdown strategy",
            "support inventory and assortment planning",
        ],
        "ai_recommendations": [
            "generate product recommendations from patterns",
            "score likely high-conversion items",
            "support intelligent pricing and assortment decisions",
        ],
    }

    if "price" in lower_text or "pricing" in lower_text:
        branches["pricing_intelligence"].append("pricing signals detected in source content")
    if "inventory" in lower_text or "stock" in lower_text:
        branches["inventory_demand"].append("inventory signals detected in source content")
    if "store" in lower_text or "customer" in lower_text:
        branches["customer_store_insights"].append("customer/store signals detected in source content")

    return branches


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract text from a PDF and create analysis-ready outputs.")
    parser.add_argument(
        "--pdf",
        type=Path,
        default=Path("Trent_AI_GitHub_Profile_Showcase.pdf"),
        help="Path to the source PDF file.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("output"),
        help="Directory where extracted outputs will be saved.",
    )
    args = parser.parse_args()

    pdf_path = args.pdf.resolve()
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    rows = extract_pdf_lines(pdf_path)
    raw_text_path, csv_path = write_outputs(rows, args.output_dir.resolve())
    branches = build_analysis_branches(rows)

    print(f"Extracted {len(rows)} non-empty lines from {pdf_path.name}")
    print(f"Raw text saved to: {raw_text_path}")
    print(f"CSV saved to: {csv_path}")

    print("\nSuggested downstream branches after PDF extraction:")
    for branch_name, tasks in branches.items():
        print(f"- {branch_name}: {', '.join(tasks[:2])}")


if __name__ == "__main__":
    main()
