import pandas as pd

# Load a CSV file
cleaned_file = 'input_data.csv'
df_cleaned = pd.read_csv(cleaned_file)

# Extracting the required columns (Titel and Keywords)
titles = df_cleaned['Title']
keywords = df_cleaned['Keywords']

# Writing to a text file
with open('output.txt', 'w', encoding='utf-8') as f:
    for title, keyword in zip(titles, keywords):
        f.write(f'Title: {title}\nKeywords: {keyword}\n\n')

print("The data has been successfully saved to 'output.txt'.")
