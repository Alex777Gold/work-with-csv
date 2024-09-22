import pandas as pd
from datetime import datetime, timedelta


def add_publish_date_column(input_file, output_file, input_date, hours_step, num_entries):
    # Convert the input date to the desired format
    start_datetime = datetime.strptime(input_date, '%Y-%m-%dT%H:%M:%S')

    # Creating a list of dates in increments of specified hours
    publish_dates = [(start_datetime + timedelta(hours=hours_step * i)
                      ).strftime('%Y-%m-%dT%H:%M:%S') for i in range(num_entries)]

    # Reading CSV file
    df = pd.read_csv(input_file)

    # Check that the number of dates matches the number of lines in the file
    if len(publish_dates) != len(df):
        raise ValueError(
            "Количество дат не совпадает с количеством строк в CSV файле.")

    # Adding a new column before 'Keywords'
    df.insert(df.columns.get_loc('Keywords'), 'Publish date', publish_dates)

    # Saving the modified DataFrame to a new CSV file
    df.to_csv(output_file, index=False)


# Usage
input_file = 'input.csv'  # Input file
output_file = 'scheduled_output.csv'  # Output filr
input_date = '2022-05-17T17:00:00'  # Initial time
hours_step = 5  # Step in hours for publications

df = pd.read_csv(input_file)

num_entries = len(df)

add_publish_date_column(input_file, output_file,
                        input_date, hours_step, num_entries)
