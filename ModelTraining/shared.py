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