from sklearn import tree
import joblib
import os

def get_int_for_gender(value):
    return {"male":0, "female": 1}[value]

def get_int_for_port(value):
    return {"S":0, "C": 1, "Q": 2}[value]

def build_model_v1():
    with open("DATA/titanic_dataset_for_decision_tree_v1.csv", "r") as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        content = [x.split(";") for x in content]
        headers = content[0]

        content = content[1:]

    labels = [row[0] for row in content]
    features = []

    for row in content:
        feature = []

        feature.append(float(row[1]))
        feature.append(get_int_for_gender(row[2]))
        feature.append(float(row[3]))
        feature.append(float(row[4]))
        feature.append(float(row[5]))
        feature.append(get_int_for_port(row[6]))

        features.append(feature)

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features, labels)

    if not os.path.exists("Models"):
        os.mkdir("Models")

    joblib.dump(clf, "Models/titanic_decision_tree_model_v1.joblib")

    print("Decision tree version 1 - Model has been built and saved to Models/titanic_decision_tree_model_v1.joblib")

def build_model_v2():
    with open("DATA/titanic_dataset_for_decision_tree_v2.csv", "r") as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        content = [x.split(";") for x in content]
        headers = content[0]

        content = content[1:]

    labels = [row[0] for row in content]
    features = []

    for row in content:
        feature = []

        feature.append(int(row[1]))
        feature.append(int(row[2]))
        feature.append(int(row[3]))
        feature.append(int(row[4]))
        feature.append(int(row[5]))
        feature.append(int(row[6]))

        features.append(feature)

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features, labels)

    if not os.path.exists("Models"):
        os.mkdir("Models")

    joblib.dump(clf, "Models/titanic_decision_tree_model_v2.joblib")

    print("Decision tree version 2 - Model has been built and saved to Models/titanic_decision_tree_model_v2.joblib")

def build_model_v3():
    with open("DATA/titanic_dataset_for_decision_tree_v3.csv", "r") as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        content = [x.split(";") for x in content]
        headers = content[0]

        content = content[1:]

    labels = [row[0] for row in content]
    features = []

    for row in content:
        feature = []

        feature.append(int(row[1]))
        feature.append(int(row[2]))
        feature.append(int(row[3]))
        feature.append(int(row[4]))
        feature.append(int(row[5]))
        feature.append(int(row[6]))

        features.append(feature)

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features, labels)

    if not os.path.exists("Models"):
        os.mkdir("Models")

    joblib.dump(clf, "Models/titanic_decision_tree_model_v3.joblib")

    print("Decision tree version 3 - Model has been built and saved to Models/titanic_decision_tree_model_v3.joblib")

if __name__ == "__main__":
    print("-" * 50)
    build_model_v1()
    build_model_v2()
    build_model_v3()
    print("-" * 50)
