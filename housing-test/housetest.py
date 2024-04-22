import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

# Load the dataset
data_path = 'Datasets\housing\housing_data_trimmed.csv'  # Replace this with the path to your cleaned dataset
data = pd.read_csv(data_path, low_memory=False)

# Convert any remaining categorical columns to numeric (specifically checking for 'State' or similar columns)
categorical_cols = data.select_dtypes(include=['object']).columns
label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col].astype(str))  # Make sure data is string
    label_encoders[col] = le

# Define the features and target variable
X = data.drop(['2023 AVG.'], axis=1)  # Include all other columns as features except the target
y = data['2023 AVG.']  # Target variable

# Split the data into training and testing sets (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Random Forest Regressor
forest_model = RandomForestRegressor(n_estimators=100, random_state=42)  # 100 trees in the forest

# Fit the model on the training data
forest_model.fit(X_train, y_train)

# Predict on the test data
y_pred = forest_model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R^2 Score:", r2)

# Feature importance - Optional to understand which features are influencing the housing prices most
feature_importances = pd.Series(forest_model.feature_importances_, index=X.columns)
print("Feature Importances:\n", feature_importances.sort_values(ascending=False))
