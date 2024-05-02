import pandas as pd
import numpy as np
from covarience_functions import calculate_covariance_matrices
from covarience_functions import plot_covariance_matrix

# load & clean data
df = pd.read_csv('Datasets\combined\merged_data_LATEST.csv')
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

# get cov. matrix
covariance_matrices = calculate_covariance_matrices(df)

# plot specific county
if 'Plumas County' in covariance_matrices and covariance_matrices['Plumas County'] is not None:
    plot_covariance_matrix(covariance_matrices['Plumas County'], 'Plumas County')
else:
    print("No sufficient data available for Plumas County to plot a covariance matrix.")
