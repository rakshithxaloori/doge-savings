# HTML Table Data Processing Scripts

As of 25th February, 2025's data, the savings add up to Total Saved: $9,601,135,843.23

This repository contains Python scripts for processing HTML table data from "https://doge.gov/savings" and performing calculations.

## Files

- `convert.py` - Converts an HTML table to CSV format
- `add.py` - Calculates total savings from the CSV data
- `requirements.txt` - Lists required Python packages
- `table.html` - Input HTML file containing the table data
- `table_data.csv` - Output CSV file generated from the HTML table

## Setup

1. Install requirements:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. First, convert the HTML table to CSV:

   ```
   python convert.py
   ```

   This will read the `table.html` file and generate `table_data.csv`.

2. Then, calculate the total savings:
   ```
   python add.py
   ```
   This will read the CSV file and display the total amount saved.
