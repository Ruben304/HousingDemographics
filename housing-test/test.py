import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# Generate synthetic data
np.random.seed(0)
data_size = 1000

average_income = np.random.normal(50000, 10000, data_size)  # Mean income in dollars
percentage_ethnic_group = np.random.normal(30, 10, data_size)  # Percentage of a particular ethnic group
unemployment_rate = np.random.normal(5, 2, data_size)  # Unemployment rate in percentage

# Simulating housing prices; assume they are affected by the above features
housing_prices = (average_income * 0.3) + (percentage_ethnic_group * -150) + (unemployment_rate * -1000) + np.random.normal(0, 25000, data_size)

# Create a DataFrame
df = pd.DataFrame({
    'Average Income': average_income,
    'Percentage Ethnic Group': percentage_ethnic_group,
    'Unemployment Rate': unemployment_rate,
    'Housing Prices': housing_prices
})

# Display the first few rows of the DataFrame
print(df.head())

# Define features and target variable
X = df[['Average Income', 'Percentage Ethnic Group', 'Unemployment Rate']]
y = df['Housing Prices']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Initialize Ridge Regression model
# ridge_model = Ridge(alpha=1.0)  # Alpha is the regularization strength; larger values specify stronger regularization.

# # Fit the model
# ridge_model.fit(X_train, y_train)

# # Predict on the testing set
# y_pred = ridge_model.predict(X_test)

# Initialize Decision Tree Regressor
tree_model = DecisionTreeRegressor(max_depth=5, random_state=42)  # Max depth is chosen to prevent overfitting

# Fit model to training data
tree_model.fit(X_train, y_train)

# Predict on the test data
y_pred = tree_model.predict(X_test)


# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

