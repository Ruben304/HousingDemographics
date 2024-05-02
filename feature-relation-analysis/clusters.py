from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from covarience_functions import calculate_covariance_matrices


# load & clean data
df = pd.read_csv('Datasets\combined\merged_data_LATEST.csv')
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

# get cov. matrix
covariance_matrices = calculate_covariance_matrices(df)

# list to hold our data for clustering
data_for_clustering = []
labels = []

# get every covariance matrices and prepare the data
for county, matrix in covariance_matrices.items():
    if matrix is not None and matrix.size > 0:
        # flatten each covariance matrix into a 1D array and append to our data list
        data_for_clustering.append(matrix.values.flatten())
        labels.append(county)

# convert the list to a numpy array
data_for_clustering = np.array(data_for_clustering)

# perform hierarchical clustering
linked = linkage(data_for_clustering, method='ward')

# plot dendrogram
plt.figure(figsize=(10, 7))
dendrogram(linked,
            orientation='top',
            labels=labels,
            distance_sort='descending',
            show_leaf_counts=True)

plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('County')
plt.ylabel('Distance')
plt.show()