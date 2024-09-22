import pandas as pd

# Load a CSV file
input_file = 'input_data.csv'  # input file path
output_file = 'output_data.csv'  # file path after deleting empty lines

# Reading a CSV file using pandas
df = pd.read_csv(input_file)

# Delete rows where the 'Media URL' column is empty
df_cleaned = df.dropna(subset=['Media URL'])

# Saving a cleared file
df_cleaned.to_csv(output_file, index=False)

print(f"File without empty Medial URL empty rows '{output_file}'")
