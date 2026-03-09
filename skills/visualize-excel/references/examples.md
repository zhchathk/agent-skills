# Visualize-Excel Examples

## Common Usage Patterns

### Example 1: Plot All Columns
User request: "Show me all the data in one chart"

```bash
python scripts/plot_excel.py data.xlsx --mode all --output all_data.png
```

### Example 2: Revenue by Year
User request: "Create a chart showing revenue with one line per year"

```bash
python scripts/plot_excel.py data.xlsx --mode by-year --column Revenue --output revenue_by_year.png
```

### Example 3: Cost by Year
User request: "Show cost trends across years"

```bash
python scripts/plot_excel.py data.xlsx --mode by-year --column Cost --output cost_by_year.png
```

### Example 4: Marketing Expense by Year
User request: "Compare marketing expenses year over year"

```bash
python scripts/plot_excel.py data.xlsx --mode by-year --column Marketing-expense --output marketing_by_year.png
```

## Expected Data Format

The script expects Excel files with:
- Year column (for year-based grouping)
- week column (for x-axis in by-year mode)
- One or more numeric columns to visualize

Example structure:
```
Year | week | Revenue | Cost | Marketing-expense
2024 |  1   | 10008.9 | 6005.4 | 4000.0
2024 |  2   | 10227.4 | 6136.5 | 4012.0
...
```

## Chart Features

All charts include:
- Y-axis starting at 0
- Grid lines for readability
- Legend for multiple series
- High-resolution output (300 DPI)
- Automatic marker styles for different series
