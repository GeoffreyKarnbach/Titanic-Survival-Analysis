import joblib
import csv
import os

def safe_to_float(value):
    try:
        return float(value)
    except:
        return 0.0
    
def get_int_for_gender(value):
    return {"male":0, "female": 1}[value]

def get_int_for_port(value):
    return {"S":0, "C": 1, "Q": 2}[value]

def get_adapted_features_for_decision_tree(row):
    feature = []

    feature.append(safe_to_float(row[1]))
    feature.append(get_int_for_gender(row[3]))
    feature.append(safe_to_float(row[4]))
    feature.append(safe_to_float(row[5]) + safe_to_float(row[6]))
    feature.append(round(safe_to_float(row[8])))
    feature.append(get_int_for_port(row[10]))

    return feature

loaded_decision_tree = joblib.load("Models/titanic_decision_tree_model.joblib")

with open("Data/test.csv", "r") as f:
    reader = csv.reader(f)
    headers = next(reader)
    content = [row for row in reader]

features = []
passenger_ids = []
results = []

for row in content:
    passenger_ids.append(row[0])
    features.append(get_adapted_features_for_decision_tree(row))

results = loaded_decision_tree.predict(features)

if not os.path.exists("Predictions"):
    os.mkdir("Predictions")

with open("Predictions/titanic_decision_tree_results.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["PassengerId", "Survived"])
    writer.writerows(zip(passenger_ids, results))