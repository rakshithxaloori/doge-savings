import csv
from bs4 import BeautifulSoup

# File paths
html_file_path = "table.html"  # Change this to your HTML file path
csv_file_path = "table_data.csv"  # Output CSV file path

# Read the HTML file
with open(html_file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find the table in the HTML
table = soup.find("table")

if not table:
    print("No table found in the HTML file.")
else:
    # Open a CSV file for writing
    with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)

        # Extract header information
        headers = []
        for th in table.find_all("th"):
            headers.append(th.text.strip())

        # Write the headers to the CSV file
        csv_writer.writerow(headers)

        # Extract data from table rows
        for row in table.find_all("tr")[1:]:  # Skip the header row
            row_data = []

            # Process each cell in the row
            for td in row.find_all("td"):
                # Check if cell contains a link
                link = td.find("a")
                if link:
                    # Get the href attribute from the link
                    href = link.get("href")
                    row_data.append(href)
                else:
                    # Get the text content of the cell
                    row_data.append(td.text.strip())

            # Only write non-empty rows
            if any(row_data):
                csv_writer.writerow(row_data)

    print(f"Conversion completed! The data has been saved to '{csv_file_path}'")
