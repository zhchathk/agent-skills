#!/usr/bin/env python3
"""
Excel Data Visualization Script
Generates matplotlib charts from Excel files with flexible configuration.
"""

import pandas as pd
import matplotlib.pyplot as plt
import argparse
import sys
from pathlib import Path


def plot_all_columns(df, output_file='chart.png'):
    """Plot all numeric columns with year-week x-axis labels."""
    # Create x-axis labels
    if 'Year' in df.columns and 'week' in df.columns:
        df['Year-Week'] = df['Year'].astype(str) + '-W' + df['week'].astype(str)
        x_label = 'Year-Week'
    else:
        x_label = 'Index'
    
    # Get numeric columns (excluding Year and week)
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    if 'Year' in numeric_cols:
        numeric_cols.remove('Year')
    if 'week' in numeric_cols:
        numeric_cols.remove('week')
    
    plt.figure(figsize=(14, 6))
    
    # Plot each numeric column
    markers = ['o', 's', '^', 'D', 'v', '<', '>', 'p', '*', 'h']
    for idx, col in enumerate(numeric_cols):
        marker = markers[idx % len(markers)]
        plt.plot(df.index, df[col], label=col, marker=marker, markersize=3)
    
    plt.ylim(bottom=0)
    
    # Set x-axis labels
    if 'Year-Week' in df.columns:
        tick_positions = range(0, len(df), max(1, len(df) // 15))
        tick_labels = [df['Year-Week'].iloc[i] for i in tick_positions]
        plt.xticks(tick_positions, tick_labels, rotation=45, ha='right')
    
    plt.xlabel(x_label)
    plt.ylabel('Value')
    plt.title('All Data Points for All Years')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Chart saved as '{output_file}'")


def plot_by_year(df, column, output_file='chart.png'):
    """Plot a single column with one line per year."""
    if 'Year' not in df.columns or 'week' not in df.columns:
        print("Error: DataFrame must have 'Year' and 'week' columns")
        sys.exit(1)
    
    if column not in df.columns:
        print(f"Error: Column '{column}' not found in data")
        sys.exit(1)
    
    plt.figure(figsize=(12, 6))
    
    # Plot for each year
    for year in sorted(df['Year'].unique()):
        year_data = df[df['Year'] == year]
        plt.plot(year_data['week'], year_data[column], label=f'{year}', marker='o', markersize=4)
    
    plt.ylim(bottom=0)
    plt.xlabel('Week')
    plt.ylabel(column)
    plt.title(f'{column} by Week - One Line per Year')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Chart saved as '{output_file}'")


def main():
    parser = argparse.ArgumentParser(description='Generate charts from Excel files')
    parser.add_argument('excel_file', help='Path to Excel file')
    parser.add_argument('--mode', choices=['all', 'by-year'], default='all',
                        help='Chart mode: "all" for all columns, "by-year" for one column per year')
    parser.add_argument('--column', help='Column name (required for by-year mode)')
    parser.add_argument('--output', default='chart.png', help='Output file name')
    parser.add_argument('--sheet', default=0, help='Sheet name or index (default: 0)')
    
    args = parser.parse_args()
    
    # Validate inputs
    if args.mode == 'by-year' and not args.column:
        print("Error: --column is required for by-year mode")
        sys.exit(1)
    
    if not Path(args.excel_file).exists():
        print(f"Error: File '{args.excel_file}' not found")
        sys.exit(1)
    
    # Read Excel file
    try:
        df = pd.read_excel(args.excel_file, sheet_name=args.sheet)
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        sys.exit(1)
    
    # Generate chart
    if args.mode == 'all':
        plot_all_columns(df, args.output)
    else:
        plot_by_year(df, args.column, args.output)


if __name__ == '__main__':
    main()
