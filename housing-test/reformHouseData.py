import pandas as pd

# Load your CSV file
df = pd.read_csv('../Datasets/housing/housing_data_growth.csv')

# "Melt" the dataframe to convert it from wide format to long format
# This will create two new columns, one for the year and one for the growth rate
# 'Zipcode', 'State', 'City', 'Metro', and 'CountyName' will remain as identifier columns
melted_df = pd.melt(df, id_vars=['Zipcode', 'State', 'City', 'Metro', 'CountyName'], 
                    var_name='Year', value_name='GrowthRate')

# Save the melted dataframe back to CSV
melted_df.to_csv('reshaped_file.csv', index=False)
