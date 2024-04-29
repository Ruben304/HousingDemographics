import pandas as pd

# Assuming 'input.csv' is your CSV file with the data as shown in the image
df = pd.read_csv('Zip_zori_uc_sfrcondomfr_sm_month.csv')  # Replace 'input.csv' with your actual file path

# List of the columns that you want to keep unchanged
id_vars = ['RegionName', 'City', 'Metro', 'CountyName']

# This assumes that all other columns are in the format 'GrowthRateYYYY'
value_vars = [col for col in df.columns if col.startswith('GrowthRate')]

# Melt the dataframe
melted_df = pd.melt(df, id_vars=id_vars, value_vars=value_vars, 
                    var_name='Year', value_name='GrowthRate')

# Extract year from the 'Year' column (e.g., 'GrowthRate2016' becomes '2016')
melted_df['Year'] = melted_df['Year'].str.extract('(\d+)').astype(int)

# Replace '#DIV/0!' with NaN (optional step)
melted_df.replace('#DIV/0!', pd.NA, inplace=True)

# Save the restructured data to a new CSV file
melted_df.to_csv('output.csv', index=False)  # 'output.csv' will be your new file

# Print the first few rows to check
print(melted_df.head())
