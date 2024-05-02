import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have already loaded your dataset into a DataFrame called 'data'
# If not, you can load it using:
data = pd.read_csv('Datasets\combined\merged_data_renters.csv', dtype={'CountyName': str})

numerical_cols = ['WHITE', 'BLACK_OR_AFRICAN_AMERICAN', 'AMERICAN_INDIAN_AND_ALASKA_NATIVE', 'ASIAN', 'NATIVE_HAWAIIAN_AND_OTHER_PACIFIC_ISLANDER', 'HISPANIC_OR_LATINO', 'GrowthRate']
numerical_data = data[numerical_cols]

# Compute the correlation matrix
corr_matrix = numerical_data.corr()

# Plotting the correlation matrix as a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".6f", vmin=0, vmax=0.05)
plt.title('Correlation Matrix')
plt.show()

# JUST DO A 6x6 CORRELATION MATRIX
# ALL THE DEMOGRAPHIC GROUPS AND THEN THE GROWTH RATE
# GROUP DATA BY COUNTIES, GO 3D TO THE COUNTIES
# SEE THAT ROW ACCROSS THE 3RD DIMENSION FOR EACH DEMOGRAPHIC AND SEE HOW THE CORRELATIONS VARY AROUND THE COUNTIES
# SET THE DATA AS +1 0 -1 FOR MOST OF THE GROWTH RATES AND DEMOGRAPHIC PERCENTAGE DRIFTS
# IGNORE YEAR ON THE CORRELATION THING