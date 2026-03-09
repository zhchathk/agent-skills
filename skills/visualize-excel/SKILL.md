---
name: visualize-excel
description: Create matplotlib charts from Excel data with automatic formatting. Use when users need to visualize Excel data, create charts from spreadsheets, plot time-series data by year and week, compare metrics across years, or generate publication-quality visualizations. Supports both all-columns overview charts and year-by-year comparison charts with y-axis starting at 0.
---

# Visualize-Excel

Generate matplotlib charts from Excel files with consistent formatting and automatic y-axis scaling from 0.

## Quick Start

Use the `scripts/plot_excel.py` script for all chart generation tasks.

### Chart Mode 1: All Columns Overview

Plot all numeric columns on a single chart with year-week x-axis labels:

```bash
python scripts/plot_excel.py <excel_file> --mode all --output <output_file>
```

Example:
```bash
python scripts/plot_excel.py data.xlsx --mode all --output overview.png
```

### Chart Mode 2: Year-by-Year Comparison

Plot a single column with one line per year:

```bash
python scripts/plot_excel.py <excel_file> --mode by-year --column <column_name> --output <output_file>
```

Example:
```bash
python scripts/plot_excel.py data.xlsx --mode by-year --column Revenue --output revenue_trends.png
```

## Script Parameters

- `excel_file` (required): Path to the Excel file
- `--mode`: Chart type - "all" or "by-year" (default: all)
- `--column`: Column name to plot (required for by-year mode)
- `--output`: Output filename (default: chart.png)
- `--sheet`: Sheet name or index (default: 0)

## Expected Data Format

The Excel file should contain:
- `Year` column: Year values (e.g., 2024, 2025, 2026)
- `week` column: Week numbers (1-52)
- Numeric columns: Data to visualize (e.g., Revenue, Cost, Marketing-expense)

## Chart Features

All generated charts include:
- Y-axis starting at 0 for accurate visual comparison
- Grid lines with 30% transparency
- Legend for series identification
- Automatic marker styles (circles, squares, triangles, etc.)
- High-resolution output (300 DPI)
- Rotated x-axis labels for readability

## Workflow

1. Identify the Excel file and desired chart type
2. For overview charts, use `--mode all`
3. For year comparisons, use `--mode by-year` with specific column
4. Run the script with appropriate parameters
5. Verify the output file is generated

## Additional Examples

See [examples.md](references/examples.md) for more usage patterns and expected data formats.

## Environment Requirements

Required Python packages:
- pandas
- openpyxl
- matplotlib

Install with: `pip install pandas openpyxl matplotlib`
