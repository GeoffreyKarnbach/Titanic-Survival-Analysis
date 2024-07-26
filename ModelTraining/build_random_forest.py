from sklearn import ensemble 
import joblib
import os
from shared import get_feature_and_labels_array_from_file, save_model

def build_random_forest():
    features, labels = get_feature_and_labels_array_from_file("DATA/titanic_dataset_for_random_forest.csv")

    random_forest_model = ensemble.RandomForestClassifier(random_state=2024, n_estimators=100)
    random_forest_model = random_forest_model.fit(features, labels)

    save_model(random_forest_model, "titanic_random_forest_model")

if __name__ == "__main__":
    print("-" * 50)
    build_random_forest()
    print("-" * 50)