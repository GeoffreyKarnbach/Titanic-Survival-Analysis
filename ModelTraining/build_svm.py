from sklearn import svm
import joblib
import os

def build_svm():
    with open(f"DATA/titanic_dataset_for_svm.csv", "r") as f:
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
    
    svm_model = svm.SVC()
    svm_model = svm_model.fit(features, labels)

    if not os.path.exists("Models"):
        os.mkdir("Models")
    
    joblib.dump(svm_model, "Models/titanic_svm_model.joblib")

    print("SVM Model has been built and saved to Models/titanic_svm_model.joblib")

if __name__ == "__main__":
    print("-" * 50)
    build_svm()
    print("-" * 50)