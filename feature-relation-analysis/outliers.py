import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('Datasets/combined/normalized_growth_rates.csv')

# check GrowthRate
sns.boxplot(x=data['GrowthRate'])
plt.show()

# calculating Z-score for the GrowthRate
data['GrowthRate_Zscore'] = (data['GrowthRate'] - data['GrowthRate'].mean()) / data['GrowthRate'].std()

# choose outliers based on Z-score
outliers = data[abs(data['GrowthRate_Zscore']) > 3]

# or IQR to find outliers
Q1 = data['GrowthRate'].quantile(0.25)
Q3 = data['GrowthRate'].quantile(0.75)
IQR = Q3 - Q1
outliers_iqr = data[(data['GrowthRate'] < (Q1 - 1.5 * IQR)) | (data['GrowthRate'] > (Q3 + 1.5 * IQR))]

print("Outliers based on Z-score:")
print(outliers)
print("Outliers based on IQR:")
print(outliers_iqr)

cleaned_data = data[abs(data['GrowthRate_Zscore']) <= 3]  # This removes outliers based on Z-score
