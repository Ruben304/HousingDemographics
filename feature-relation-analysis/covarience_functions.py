import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# calculate covariance matrices
def calculate_covariance_matrices(dataframe):
    covariance_matrices = {}
    grouped = dataframe.groupby('CountyName')
    
    for county, group in grouped:
        if group.shape[0] > 1:
            numerical_data = group.drop('CountyName', axis=1)
            cov_matrix = numerical_data.cov()
            covariance_matrices[county] = cov_matrix
        else:
            covariance_matrices[county] = None

    return covariance_matrices


# count positive correlations
def count_positive_correlations(cov_matrices, target_variable):
    # check if target variable exist in the DataFrame columns 
    if target_variable not in next(iter(cov_matrices.values())).columns:
        raise ValueError(f"{target_variable} not found in the covariance matrix columns.")

    # initialize the count dictionary with demographic names excluding the target variable
    positive_correlations_count = {variable: 0 for variable in next(iter(cov_matrices.values())).columns if variable != target_variable}

    for county, cov_matrix in cov_matrices.items():
        if cov_matrix is not None:
            # get the covariances values with the target variable
            growth_rate_covariances = cov_matrix.loc[target_variable]
            for demographic, covariance in growth_rate_covariances.items():
                # skip the target variable itself
                if demographic == target_variable:
                    continue
                
                # check if the positive covariance and update the count
                if covariance > 0:
                    positive_correlations_count[demographic] += 1

    return positive_correlations_count

# count negative correlations
def count_negative_correlations(cov_matrices, target_variable):
    # check if target variable exist in the DataFrame columns
    if target_variable not in next(iter(cov_matrices.values())).columns:
        raise ValueError(f"{target_variable} not found in the covariance matrix columns.")

    # initialize the count dictionary with demographic names excluding the target variable
    negative_correlations_count = {variable: 0 for variable in next(iter(cov_matrices.values())).columns if variable != target_variable}

    for county, cov_matrix in cov_matrices.items():
        if cov_matrix is not None:
            # get the covariances values with the target variable
            growth_rate_covariances = cov_matrix.loc[target_variable]
            for demographic, covariance in growth_rate_covariances.items():
                # skip the target variable itself
                if demographic == target_variable:
                    continue
                
                # check if the negative covariance and update the count
                if covariance < 0:
                    negative_correlations_count[demographic] += 1

    return negative_correlations_count


# plot a covariance matrix
def plot_covariance_matrix(cov_matrix, county_name):
    sns.set(style="white")

    # generate a mask for the upper triangle
    mask = np.triu(np.ones_like(cov_matrix, dtype=bool))

    # set up matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))

    # generate a custom diverging colormap
    cmap = sns.diverging_palette(230, 20, as_cmap=True)

    # draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(cov_matrix, mask=mask, cmap=cmap, vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True, fmt=".2f")

    plt.title(f'Covariance Matrix for {county_name}')
    plt.show()