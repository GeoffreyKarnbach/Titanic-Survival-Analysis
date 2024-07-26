import joblib
import csv
import os
from evaluate_decision_tree import *

def get_adapted_features_for_svm(row):
    return get_adapted_features_for_decision_tree_v7(row)

def get_adapted_features_for_svm_from_request(request):
    return get_adapted_features_for_decision_tree_from_request_v7(request)

def evaluate_test_csv_for_svm():
    loaded_svm = joblib.load("Models/titanic_svm_model.joblib")

    with open("Data/test.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        content = [row for row in reader]

    features = []
    passenger_ids = []
    results = []

    for row in content:
        passenger_ids.append(row[0])
        features.append(get_adapted_features_for_svm(row))

    results = loaded_svm.predict(features)

    if not os.path.exists("Predictions"):
        os.mkdir("Predictions")

    with open("Predictions/svm.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["PassengerId", "Survived"])
        writer.writerows(zip(passenger_ids, results))

    print("Predictions have been saved to Predictions/svm.csv")

def evaluate_passenger_request_svm(request):
    feature = get_adapted_features_for_svm_from_request(request)
    loaded_svm = joblib.load("Models/titanic_svm_model.joblib")
    result = loaded_svm.predict([feature])

    return result[0]

if __name__ == "__main__":
    print("-" * 50)
    
    evaluate_test_csv_for_svm()

    print("-" * 50)
