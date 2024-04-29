import pandas as pd

def filter_growth_rate(input_csv_path, output_csv_path, growth_rate_column='GrowthRate'):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_csv_path)
    
    # Filter the DataFrame where the growth rate is greater than 200
    df_filtered = df[df[growth_rate_column] < 0]
    
    # Save the filtered DataFrame to a new CSV file
    df_filtered.to_csv(output_csv_path, index=False)
    
    return output_csv_path

def normalize_growth_rate(input_csv_path, output_csv_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_csv_path)
    
    # Normalize the 'Growth Rate' column
    df['GrowthRate'] = (df['GrowthRate'] - df['GrowthRate'].min()) / (df['GrowthRate'].max() - df['GrowthRate'].min())
    
    # Save the DataFrame with the normalized 'Growth Rate' to a new CSV file
    df.to_csv(output_csv_path, index=False)
    
    return output_csv_path

# Define the input and output paths for normalization
input_csv_path_normalized = 'merged_data.csv'
output_csv_path_normalized = 'normalized_growth_rates.csv'

# Execute the normalization function
normalized_csv_path = normalize_growth_rate(input_csv_path_normalized, output_csv_path_normalized)

# Replace 'input_data.csv' with your actual input CSV file path
input_csv_path = 'merged_data.csv'
output_csv_path = 'lowgrowthdata.csv'

# Execute the function
# filter_growth_rate(input_csv_path, output_csv_path)

