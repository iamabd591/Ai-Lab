import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

file_path = './DataSet/IRIS.csv'


def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = file_path
read_csv_file(file_path)

dataset = pd.read_csv(file_path)
X = dataset.drop('species', axis=1)
y = dataset['species']

# dataset = dataset.dropna(axis=1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# label_encoder = LabelEncoder()
# y_train_encoded = label_encoder.fit_transform(y_train)
# X_train_encoded = X_train.apply(label_encoder.fit_transform)
# X_test_encoded = X_test.apply(label_encoder.transform)

# knn_model
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)
knn_y_pred = knn_model.predict(X_test)

# K_mean
# kmeans_model = KMeans(n_clusters=2)
# kmeans_model.fit(X_train)
# kmeans_predictions = kmeans_model.predict(X_test)

# Naive_bayes_model
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)
nb_y_pred = nb_model.predict(X_test)


def evaluate_model(predictions, actual):
    accuracy = accuracy_score(actual, predictions)
    precision = precision_score(actual, predictions, average='weighted')
    recall = recall_score(actual, predictions, average='weighted')
    f1 = f1_score(actual, predictions, average='weighted')
    print(f'Accuracy: {accuracy:.4f}')
    print(f'Precision: {precision:.4f}')
    print(f'Recall: {recall:.4f}')
    print(f'F1 Score: {f1:.4f}')


# Evaluate Naive Bayes model
print("\nNaive Bayes Model Evaluation:")
evaluate_model(nb_y_pred, y_test)
print("\n")

# Evaluate KNN model
print("KNN Model Evaluation:")
evaluate_model(knn_y_pred, y_test)

# K_mean
# cluster_labels = kmeans.labels_
# plt.scatter(X_train[:, 0], X_train[:, 1], c=cluster_labels)
# plt.xlabel("species")
# plt.ylabel("species")
# plt.title("K-Means Clustering")
# plt.show()
