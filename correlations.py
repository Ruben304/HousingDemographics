import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have already loaded your dataset into a DataFrame called 'data'
# If not, you can load it using:
data = pd.read_csv('merged_data.csv', dtype={'Zipcode': str})

numerical_cols = ['Year', 'WHITE', 'BLACK_OR_AFRICAN_AMERICAN', 'AMERICAN_INDIAN_AND_ALASKA_NATIVE', 'ASIAN', 'NATIVE_HAWAIIAN_AND_OTHER_PACIFIC_ISLANDER', 'HISPANIC_OR_LATINO', 'GrowthRate']
numerical_data = data[numerical_cols]

# Compute the correlation matrix
corr_matrix = numerical_data.corr()

# Plotting the correlation matrix as a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".6f", vmin=0, vmax=0.05)
plt.title('Correlation Matrix')
plt.show()