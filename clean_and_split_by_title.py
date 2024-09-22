import csv


def process_csv(input_file, output_file):
    unique_titles = set()  # To store unique Title values
    unique_rows = []       # To store strings with unique titles
    duplicate_rows = []    # To store strings with duplicate headers

    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)  # Read all the rows at once

        # String search for filtering
        for row in rows:
            title = row.get('Title', '').strip()
            media_url = row.get('Media URL', '').strip()

            # Delete lines where the Media URL field is empty
            if not media_url:
                continue

            # Check Title for uniqueness
            if title not in unique_titles:
                unique_titles.add(title)
                unique_rows.append(row)
            else:
                duplicate_rows.append(row)

    # Write the result to a new CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = unique_rows[0].keys()  # Save headers from CSV
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        # First we write the lines with unique titles Title
        writer.writerows(unique_rows)
        # Then record the lines with duplicate Title headings
        writer.writerows(duplicate_rows)


# Usage
input_file = 'input.csv'
output_file = 'cleaned_output.csv'

process_csv(input_file, output_file)
