import joblib
import csv
import os
from shared import *

def evaluate_test_csv_for_svm(model_name):
    loaded_svm = joblib.load(f"Models/{model_name}.joblib")

    with open("Data/test.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        content = [row for row in reader]

    features = []
    passenger_ids = []
    results = []

    for row in content:
        passenger_ids.append(row[0])
        features.append(get_adapted_features(row))

    results = loaded_svm.predict(features)

    if not os.path.exists("Predictions"):
        os.mkdir("Predictions")

    model_name = model_name.replace("titanic_", "")
    model_name = model_name.replace("_model", "")

    with open(f"Predictions/{model_name}.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["PassengerId", "Survived"])
        writer.writerows(zip(passenger_ids, results))

    print(f"Predictions have been saved to Predictions/{model_name}.csv")

def evaluate_passenger_request_svm(request, model_name):
    feature = get_adapted_features_from_request(request)
    loaded_svm = joblib.load(f"Models/{model_name}.joblib")
    result = loaded_svm.predict([feature])

    return result[0]

if __name__ == "__main__":
    print("-" * 50)

    models = [
        "titanic_svm_model",
        "titanic_svm_linear_model",
        "titanic_svm_poly_model",
        "titanic_svm_rbf_model",
        "titanic_svm_sigmoid_model"
    ]

    for model in models:
        evaluate_test_csv_for_svm(model)

    print("-" * 50)
