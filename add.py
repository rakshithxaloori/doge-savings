import csv


def parse_currency(currency_str):
    """
    Convert a currency string (e.g., '$145,000') to a float.
    Handles dollar signs, commas, and decimal points.
    """
    # Remove all non-numeric characters except for the decimal point
    currency_str = currency_str.replace("$", "").replace(",", "").strip()

    # Convert to float, handling potential errors
    try:
        return float(currency_str)
    except ValueError:
        print(
            f"Warning: Could not convert '{currency_str}' to a number. Ignoring this value."
        )
        return 0.0


# Input file path
input_csv = "table_data.csv"

# Initialize total
total_saved = 0.0

# Read the CSV file and sum the "Saved" column
with open(input_csv, "r", encoding="utf-8") as infile:
    # Create CSV reader
    reader = csv.reader(infile)

    # Read header row first
    header = next(reader)

    # Find the index of the "Saved" column
    try:
        saved_index = header.index("Saved")
    except ValueError:
        print("Error: No 'Saved' column found in the CSV file.")
        exit(1)

    # Process each row and add to total
    for row in reader:
        if saved_index < len(row):
            # Parse the currency value and add to total
            value = parse_currency(row[saved_index])
            total_saved += value

# Print the total
print(f"Total Saved: ${total_saved:,.2f}")
