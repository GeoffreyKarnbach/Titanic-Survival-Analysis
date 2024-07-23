import joblib
import csv
import os

def safe_to_float(value):
    try:
        return float(value)
    except:
        return 0.0

def safe_to_int(value):
    try:
        return int(value)
    except:
        return 0

def get_int_for_age(value):
    # df_decision_tree_2['Age'] = pd.cut(df_decision_tree_2['Age'], bins=[0, 13, 18, 60, 100], labels=[0, 1, 2, 3])
    value = safe_to_int(value)

    if value <= 13:
        return 0
    elif value <= 18:
        return 1
    elif value <= 60:
        return 2
    return 3

def get_int_for_fare(value):
    # df_decision_tree_2['Fare'] = pd.cut(df_decision_tree_2['Fare'], bins=[0, 50, 100, 200, 1000], labels=[0, 1, 2, 3])
    value = safe_to_int(value)

    if value <= 50:
        return 0
    elif value <= 100:
        return 1
    elif value <= 200:
        return 2
    return 3
    
def get_int_for_gender(value):
    return {"male":0, "female": 1}[value]

def get_int_for_port(value):
    return {"S":0, "C": 1, "Q": 2}[value]

def get_adapted_features_for_decision_tree_v1(row):
    feature = []

    feature.append(safe_to_float(row[1]))
    feature.append(get_int_for_gender(row[3]))
    feature.append(safe_to_float(row[4]))
    feature.append(safe_to_float(row[5]) + safe_to_float(row[6]))
    feature.append(round(safe_to_float(row[8])))
    feature.append(get_int_for_port(row[10]))

    return feature

def get_adapted_features_for_decision_tree_v2_v3(row):
    feature = []

    feature.append(safe_to_int(row[1]))
    feature.append(get_int_for_gender(row[3]))
    feature.append(get_int_for_age(row[4]))
    feature.append(safe_to_int(row[5]) + safe_to_int(row[6]))
    feature.append(get_int_for_fare(row[8]))
    feature.append(get_int_for_port(row[10]))

    return feature

def get_adapted_features_for_decision_tree_from_request_v1(request):
    feature = []

    feature.append(int(request.pclass))
    feature.append(get_int_for_gender(request.sex))
    feature.append(float(request.age))
    feature.append(int(request.sibsp) + int(request.parch))
    feature.append(float(request.fare))
    feature.append(get_int_for_port(request.embarked))

    return feature

def evaluate_test_csv_for_decision_tree_v1():
    loaded_decision_tree = joblib.load("Models/titanic_decision_tree_model_v1.joblib")

    with open("Data/test.csv", "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        content = [row for row in reader]

    features = []
    passenger_ids = []
    results = []

    for row in content:
        passenger_ids.append(row[0])
        features.append(get_adapted_features_for_decision_tree_v1(row))

    results = loaded_decision_tree.predict(features)

    if not os.path.exists("Predictions"):
        os.mkdir("Predictions")

    with open("Predictions/decision_tree_v1.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["PassengerId", "Survived"])
        writer.writerows(zip(passenger_ids, results))

    print("Predictions have been saved to Predictions/decision_tree_v1.csv")


def evaluate_test_csv_for_decision_tree_v2():
    loaded_decision_tree = joblib.load("Models/titanic_decision_tree_model_v2.joblib")

    with open("Data/test.csv", "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        content = [row for row in reader]

    features = []
    passenger_ids = []
    results = []

    for row in content:
        passenger_ids.append(row[0])
        features.append(get_adapted_features_for_decision_tree_v2_v3(row))

    results = loaded_decision_tree.predict(features)

    if not os.path.exists("Predictions"):
        os.mkdir("Predictions")

    with open("Predictions/decision_tree_v2.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["PassengerId", "Survived"])
        writer.writerows(zip(passenger_ids, results))

    print("Predictions have been saved to Predictions/decision_tree_v2.csv")

def evaluate_test_csv_for_decision_tree_v3():
    loaded_decision_tree = joblib.load("Models/titanic_decision_tree_model_v3.joblib")

    with open("Data/test.csv", "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        content = [row for row in reader]

    features = []
    passenger_ids = []
    results = []

    for row in content:
        passenger_ids.append(row[0])
        features.append(get_adapted_features_for_decision_tree_v2_v3(row))

    results = loaded_decision_tree.predict(features)

    if not os.path.exists("Predictions"):
        os.mkdir("Predictions")

    with open("Predictions/decision_tree_v3.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["PassengerId", "Survived"])
        writer.writerows(zip(passenger_ids, results))

    print("Predictions have been saved to Predictions/decision_tree_v3.csv")

def evaluate_passenger_request_v1(request):
    feature = get_adapted_features_for_decision_tree_from_request_v1(request)
    loaded_decision_tree = joblib.load("Models/titanic_decision_tree_model_v1.joblib")
    result = loaded_decision_tree.predict([feature])

    return result[0]

if __name__ == "__main__":
    print("-" * 50)
    evaluate_test_csv_for_decision_tree_v1()
    evaluate_test_csv_for_decision_tree_v2()
    evaluate_test_csv_for_decision_tree_v3()
    print("-" * 50)
