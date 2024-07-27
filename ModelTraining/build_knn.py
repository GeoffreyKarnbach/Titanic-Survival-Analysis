from sklearn import neighbors 
import joblib
import os
from shared import get_feature_and_labels_array_from_file, save_model

def build_knn():
    features, labels = get_feature_and_labels_array_from_file("DATA/titanic_dataset_for_knn.csv")

    knn_model = neighbors.KNeighborsClassifier(n_neighbors=20)
    knn_model = knn_model.fit(features, labels)

    save_model(knn_model, "titanic_knn_model")

if __name__ == "__main__":
    print("-" * 50)
    build_knn()
    print("-" * 50)