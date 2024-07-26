def get_feature_and_labels_array_from_file(file_path):
    with open(file_path, "r") as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        content = [x.split(";") for x in content]

        content = content[1:]

    labels = [row[0] for row in content]
    features = []

    for row in content:
        feature = []

        for i in range(1, 9):
            feature.append(int(row[i]))

        features.append(feature)
    
    return features, labels

def save_model(model, model_name):
    import os
    import joblib

    if not os.path.exists("Models"):
        os.mkdir("Models")

    joblib.dump(model, f"Models/{model_name}.joblib")

    print(f"{model_name} has been built and saved to Models/{model_name}.joblib")

############
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

def get_adapted_features_for_decision_tree_from_request_v_n(request):
    feature = []

    feature.append(safe_to_int(request.pclass))
    feature.append(get_int_for_gender(request.sex))
    feature.append(get_int_for_age(request.age))
    feature.append(safe_to_int(request.sibsp) + safe_to_int(request.parch))
    feature.append(get_int_for_fare(request.fare))
    feature.append(get_int_for_port(request.embarked))

    return feature

def get_adapted_features_from_request(request):

    feature = get_adapted_features_for_decision_tree_from_request_v_n(request)
    feature.append(1 if feature[4] == 0 else 0)

    try:
        title = request.name.split(',')[1].split('.')[0].strip()
    except:
        title = "None"
    title = title if title in ['Mr', 'Mrs', 'Miss', 'Master', 'None'] else 'Other'
    feature.append({"Mr": 1, "Mrs": 2, "Miss": 3, "Master": 4, "Other": 5, "None": 6}[title])

    return feature

def get_adapted_features_for_decision_tree_v_n(row):
    feature = []

    feature.append(safe_to_int(row[1]))
    feature.append(get_int_for_gender(row[3]))
    feature.append(get_int_for_age(row[4]))
    feature.append(safe_to_int(row[5]) + safe_to_int(row[6]))
    feature.append(get_int_for_fare(row[8]))
    feature.append(get_int_for_port(row[10]))

    return feature

def get_adapted_features(row):
    feature = get_adapted_features_for_decision_tree_v_n(row)

    feature.append(1 if feature[4] == 0 else 0)

    title = row[2].split(',')[1].split('.')[0].strip()
    title = title if title in ['Mr', 'Mrs', 'Miss', 'Master', 'None'] else 'Other'
    feature.append({"Mr": 1, "Mrs": 2, "Miss": 3, "Master": 4, "Other": 5, "None": 6}[title])

    return feature