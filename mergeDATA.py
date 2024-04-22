import pandas as pd

# Load datasets
housing_data = pd.read_csv('Datasets/housing/final_housing_data.csv')
census_data = pd.read_csv('Datasets/census/combined-datasets/census-drifts-final.csv')

# Before merging, ensure that the 'Zipcode' and 'GEOGRAPHY' columns are of the same data type
housing_data['Zipcode'] = housing_data['Zipcode'].astype(str).str.zfill(5)
census_data['GEOGRAPHY'] = census_data['GEOGRAPHY'].astype(str).str.zfill(5)

# Also ensure the 'Year' columns in both datasets are of the same data type
housing_data['Year'] = housing_data['Year'].astype(int)
census_data['YEAR'] = census_data['YEAR'].astype(int)

# Merge the datasets on both 'Zipcode'/'GEOGRAPHY' and 'Year'/'YEAR'
merged_data = pd.merge(housing_data, census_data, left_on=['Zipcode', 'Year'], right_on=['GEOGRAPHY', 'YEAR'])

# Drop the extra columns
merged_data = merged_data.drop(['GEOGRAPHY', 'YEAR'], axis=1)

# Save the merged dataset to a new CSV
merged_data.to_csv('merged_data.csv', index=False)

# Verify the merged data
print(merged_data.head())
