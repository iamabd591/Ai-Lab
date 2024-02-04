import csv
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
file_url = './data.csv'


def read_file(file_url):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File is not found at url{file_url}")
        return None
    except Exception as e:
        print(f"Error {e}")
        return None


file_path = file_url
file_content = read_file(file_url)
if file_content is not None:
    print(f"File Content at url{ file_url} is:\n {file_content}")
    print("\n")

dataset = pd.read_csv(file_url)
X = dataset.drop('Gender', axis=1)
y = dataset['Gender']

X_test, X_train, y_test, y_train = train_test_split(
    X, y, test_size=0.2, random_state=42)

nb_model = GaussianNB()
nb_model.fit(X_train, y_train)
nb_y_pred = nb_model.predict(X_test)


knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
knn_y_pred = knn.predict(X_test)


def evaluate_model(param1, param2):
    accuracy = accuracy_score(param1, param2)
    precision = precision_score(param1, param2, average='weighted')
    recall = recall_score(param1, param2, average='weighted')
    f1 = f1_score(param1, param2, average='weighted')

    print(f"Accuracy:{accuracy:.4f}")
    print(f"Precision:{precision:.4f}")
    print(f"Recall:{recall:.4f}")
    print(f"F1 Score:{f1:.4f}")


print("NB_Classifiers")
evaluate_model(nb_y_pred, y_test)

print("\n")

print("KNN_Classifiers")
evaluate_model(knn_y_pred, y_test)


dataset.head(n=10)
dataset.info()
dataset.isnull()
dataset.isnull().sum()
val = dataset.iloc[:, [3, 4]].values
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42, n_init=1)
    kmeans.fit(val)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Point Graph')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
