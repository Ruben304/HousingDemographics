import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
from covarience_functions import calculate_covariance_matrices
from covarience_functions import count_negative_correlations
from covarience_functions import count_positive_correlations

# load & clean data
df = pd.read_csv('Datasets\combined\merged_data_renters.csv')
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

# get cov. matrix
covariance_matrices = calculate_covariance_matrices(df)

# count for that column (if pos. correlation w/ GrowthRate then +1)
positive_correlations_count = count_positive_correlations(covariance_matrices, 'GrowthRate')
# count for that column  (if neg. correlation w/ GrowthRate then +1)
negative_correlations_count = count_negative_correlations(covariance_matrices, 'GrowthRate')

# print results
print("Positive Correlations with Housing Growth Rate:")
for demographic, count in positive_correlations_count.items():
    print(f"{demographic}: {count}")

print("========================================")

print("Negative Correlations with Housing Growth Rate:")
for demographic, count in negative_correlations_count.items():
    print(f"{demographic}: {count}")


# combine positive and negative counts into a DataFrame
correlation_counts = pd.DataFrame({
    'Positive': positive_correlations_count,
    'Negative': negative_correlations_count
}).T

# plot the summary heatmap
sns.set(style="white")
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_counts, annot=True, fmt="d", cmap="viridis")
plt.title('Summary of Positive and Negative Correlations with GrowthRate by Demographic')
plt.show()