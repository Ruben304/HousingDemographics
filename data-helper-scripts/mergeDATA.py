import pandas as pd

# Load datasets (replace 'dataset1.csv' and 'dataset2.csv' with your actual file paths)
dataset1 = pd.read_csv('output.csv')  # The one with RegionName
dataset2 = pd.read_csv('Datasets\census\combined-datasets\census-drifts-final.csv')  # The one with GEOGRAPHY

# Convert 'RegionName' and 'GEOGRAPHY' columns to string type to ensure matching works correctly
dataset1['RegionName'] = dataset1['RegionName'].astype(str)
dataset2['GEOGRAPHY'] = dataset2['GEOGRAPHY'].astype(str)

# Also ensure the 'Year' columns in both datasets are of the same data type
dataset1['Year'] = dataset1['Year'].astype(int)
dataset2['YEAR'] = dataset2['YEAR'].astype(int)

# Merge the datasets on both 'RegionName'/'GEOGRAPHY' and 'Year'/'YEAR'
# Use 'inner' join to only keep rows that have matching values in both datasets
merged_data = pd.merge(dataset1, dataset2, left_on=['RegionName', 'Year'], right_on=['GEOGRAPHY', 'YEAR'], how='inner')

# You may want to drop one of the duplicate columns after the merge, for example:
merged_data.drop(columns=['GEOGRAPHY', 'YEAR'], inplace=True)

# Save the merged dataset to a new CSV
merged_data.to_csv('merged_data_renters.csv', index=False)

# Print the first few rows to check the result
print(merged_data.head())

