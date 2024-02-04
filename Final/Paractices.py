import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Step 1: Read and preprocess the data
# Assuming you have a dataset file (e.g., 'your_data.csv') and it has a column 'Y' representing the class
# Replace 'your_data.csv' with the actual file path and make sure the file is in the correct format
df = pd.read_csv('./w1.csv')  # Replace 'your_data.csv' with your actual file path

# Remove specified columns
columns_to_remove = ['X1', 'X11', 'X12', 'X20']
df = df.drop(columns=columns_to_remove)

# Step 2: Perform Train Test Split with equal class distribution
X = df.drop(columns=['Y'])
y = df['Y']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Step 3: Implement Distance (KNN model)
# Using k=5
knn_model_5 = KNeighborsClassifier(n_neighbors=5)
knn_model_5.fit(X_train, y_train)

# Using k=21
knn_model_21 = KNeighborsClassifier(n_neighbors=21)
knn_model_21.fit(X_train, y_train)

# Step 4: Perform Prediction using testing data at k=5 and k=21
y_pred_5 = knn_model_5.predict(X_test)
y_pred_21 = knn_model_21.predict(X_test)

# Step 5: Calculate Accuracy
accuracy_5 = accuracy_score(y_test, y_pred_5)
accuracy_21 = accuracy_score(y_test, y_pred_21)

print(f"Accuracy at k=5: {accuracy_5}")
print(f"Accuracy at k=21: {accuracy_21}")

# Step 6: Predict the given point with the model having better accuracy
# Assuming 'p' is a DataFrame with the given point
p = pd.DataFrame([0.1, 2.2, 0.03, 1.4, 0.05, 0.6, 0.07, 1.08, 1.9, 0.11, 8.012, 0.13, 0.014, 6.15, 0.016, 4.17, 0.018, 0.019]).T

# Predict with the model having better accuracy
if accuracy_5 > accuracy_21:
    prediction_p = knn_model_5.predict(p)
    print(f"Prediction using k=5: {prediction_p}")
else:
    prediction_p = knn_model_21.predict(p)
    print(f"Prediction using k=21: {prediction_p}")
