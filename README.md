# HousingDemographics
## Collaborators 
- Ruben F. Carbajal
- Axel S. Toro Vega

## Context 
- Across the United States, gentrification has emerged as a significant topic of discussion, particularly concerning its effects on various communities
- Media predominantly focuses on how specific demographic groups, particularly low-income and minority populations, are disproportionately impacted

## Objective 
- Exploring Relationships: Analyzing the correlation between growth rates in the Housing and Renting Markets and demographic shifts in various counties across the United States
- Predictive Modeling: Utilizing binary classification and regression models to forecast growth rates in the Housing Market based on demographic changes in respective counties

## Conclusion
- Our analysis using correlation and covariance matrices revealed minimal relationships between demographic shifts and growth rates across various counties
- The binary classification and regression models, while partially effective, indicated that predicting housing rates based solely on demographic changes might be challenging

## Datasets Used
### Sourced Datasets 

- [Zillow Housing and Renting Data](https://www.zillow.com/research/data/) 
- [U.S. Census](https://www.census.gov/data.html)

### Processing the Datasets
Most of our methods in preprocessing our data is located in the `data-helper-scripts` and `census-preprocess`directory or done in excel  directly

### Created Datasets 
Our unique merged dataset for 
- Housing data found in `Datasets/combined/merged_data_housing.csv`
- Renting data found in `Datasets/combined/merged_data_renting.csv`

Final features for these datasets are:

| County   | GrowthRate    | White    | Black or African American  | American Indian or Alaskan Native  | Asian    | Hispanic or Latino | Native Hawaiian and Islander |
| -------- |:-------------:|:--------:|:--------------------------:|:----------------------------------:|:--------:|:------------------:| ----------------------------:|

Our binarized data based on the combined housing data, can be found in `binary\binary_dataset.csv`

Final features for this datasets are:

| GrowthRate    | White    | Black or African American  | American Indian or Alaskan Native  | Asian    | Hispanic or Latino | Native Hawaiian and Islander |
| ------------- |:--------:|:--------------------------:|:----------------------------------:|:--------:|:------------------:| ----------------------------:|

### Data Analysis
#### Covariance 
- `feature-relation-analysis/plot_one.py` plots one covariance matrix based on user
- `feature-relation-analysis/dashboard.py` creates a dashboard that lets user see a covarience matrix of any respective county

#### Correlation
- `feature-relation-analysis/correlations.py` plot the overall correlation matrix of the dataset
- `feature-relation-analysis/summary_heatmap.py` creates a postivie and negative relationship counter in respect to growthrate

#### Hierarchical Clustering
- `feature-relation-analysis/clusters.py` illustrates a dendogram to see similar counties and identify any outliers

#### Binary Classification
- `binary/plots/binary-results-plotting.ipynb` visualizes the results of our binary classification model
- `binary/binary-autogluon.ipynb` creation of the binary classificaiton using autogluon
- `binary/binary-sklearn.ipynb` creation of the binary classificaiton using sklearn

#### Regression Models
- ``

### Activate vierual enviornment 
- Run this in the root directory `./venv/Scripts/activate`

### Libraries used
- pandas
- numpy
- sklearn
- seaborn
- dash
- matplotlib
- autogluon

### Presentation Slides
- A pdf of our presentation slide can be found in `presentation-slides/EC503 Final Presentation.pdf`


