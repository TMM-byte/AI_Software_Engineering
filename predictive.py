import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.preprocessing import LabelEncoder

# Step 1: Load and inspect data
# Replace 'your_data.csv' with the path to your dataset
data = pd.read_csv('your_data.csv')

# Display first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Step 2: Data preprocessing
# Assume the dataset has a 'priority' column with values 'high', 'medium', 'low'
# and other feature columns

# Encode the target variable (priority) to numerical values
le = LabelEncoder()
data['priority'] = le.fit_transform(data['priority'])

# Drop any rows with missing values
data = data.dropna()

# Assume the features are all columns except 'priority'
X = data.drop('priority', axis=1)
y = data['priority']

# Step 3: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Evaluate the model
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Calculate F1-score (macro average for multi-class classification)
f1 = f1_score(y_test, y_pred, average='macro')

# Print results
print(f"\nModel Performance Metrics:")
print(f"Accuracy: {accuracy:.2f}")
print(f"F1-score (macro): {f1:.2f}")