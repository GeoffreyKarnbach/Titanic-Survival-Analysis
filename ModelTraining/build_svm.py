from sklearn import svm
import joblib
import os
from shared import get_feature_and_labels_array_from_file, save_model

def build_svm():
    features, labels = get_feature_and_labels_array_from_file("DATA/titanic_dataset_for_svm.csv")
    
    svm_model = svm.SVC()
    svm_model = svm_model.fit(features, labels)

    save_model(svm_model, "titanic_svm_model")

if __name__ == "__main__":
    print("-" * 50)
    build_svm()
    print("-" * 50)