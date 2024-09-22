import pandas as pd

# Loading data from files
file_to_clean = 'input_data.csv'  # The file from which delete lines
reference_file = 'unique_records.csv'  # File with data for comparison

# Reading CSV files
df_to_clean = pd.read_csv(file_to_clean)
reference_df = pd.read_csv(reference_file)

# Remove lines from df_to_clean that are present in reference_df
cleaned_df = df_to_clean[~df_to_clean.isin(
    reference_df.to_dict(orient='list')).all(axis=1)]

# Save the cleaned file
cleaned_df.to_csv('cleaned_file.csv', index=False)

print("The deletion is complete. The result is saved in 'cleaned_file.csv'.")
