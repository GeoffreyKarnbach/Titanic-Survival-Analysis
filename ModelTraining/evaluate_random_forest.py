import joblib
import csv
import os
from shared import *

def evaluate_test_csv_for_random_forest():
    loaded_random_forest = joblib.load("Models/titanic_random_forest_model.joblib")

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

    results = loaded_random_forest.predict(features)

    if not os.path.exists("Predictions"):
        os.mkdir("Predictions")

    with open("Predictions/random_forest.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["PassengerId", "Survived"])
        writer.writerows(zip(passenger_ids, results))

    print("Predictions have been saved to Predictions/random_forest.csv")

def evaluate_passenger_request_random_forest(request):
    feature = get_adapted_features_from_request(request)
    loaded_random_forest = joblib.load("Models/titanic_random_forest_model.joblib")
    result = loaded_random_forest.predict([feature])

    return result[0]

if __name__ == "__main__":
    print("-" * 50)
    
    evaluate_test_csv_for_random_forest()

    print("-" * 50)
