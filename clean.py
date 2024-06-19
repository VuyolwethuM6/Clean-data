import pandas as pd

# Load the data
file_path = '../../Downloads/Dam Levels Master Data_2024_06_03.xlsx'
master_df = pd.read_excel(file_path, sheet_name='MASTER')

# Rename the columns
date_columns = master_df.iloc[0, 3:].values
columns = ['Province', 'Dam Name', '2022'] + list(date_columns)
master_df.columns = columns

# Drop the first row which was used for column names
master_df = master_df.drop(0)

# Convert date columns to datetime
for col in master_df.columns[3:]:
    master_df[col] = pd.to_numeric(master_df[col], errors='coerce')

# Display the cleaned data
master_df.head()
