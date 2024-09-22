import pandas as pd

# Upload CSV file
file_path = 'input.csv'
df = pd.read_csv(file_path)

# Remove duplicates on the 'Title' column
df_unique = df.drop_duplicates(subset='Title')

# Save the result to a new CSV file
output_path = 'unique_output.csv'
df_unique.to_csv(output_path, index=False)

print(f'Duplicates have been deleted. The result is saved in {output_path}')
