import pandas as pd

# Load datasets
housing_data = pd.read_csv('../Datasets/housing/housing_data_growth.csv')
census_data = pd.read_csv('../Datasets/census/data-clean/census-2022.csv')

# Inspecting the data
print(housing_data.head())
print(census_data.head())

# Assuming 'zipcode' is the common column
# Ensure that the 'zipcode' column is the same data type in both dataframes
housing_data['Zipcode'] = housing_data['Zipcode'].astype(str)
census_data['GEOGRAPHY'] = census_data['GEOGRAPHY'].astype(str)

# Merge datasets on 'zipcode' and 'Geography'
merged_data = pd.merge(housing_data, census_data, left_on='Zipcode', right_on='GEOGRAPHY', how='inner')

# Optional: Drop the 'Geography' column if it's redundant after merging
merged_data.drop('GEOGRAPHY', axis=1, inplace=True)

# Save the merged data to a new CSV file, if needed
merged_data.to_csv('merged_dataset.csv', index=False)

# Display the first few rows of the merged dataset to verify
print(merged_data.head())
