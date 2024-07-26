from sklearn import svm
import joblib
import os
from shared import get_feature_and_labels_array_from_file, save_model

def build_svm():
    features, labels = get_feature_and_labels_array_from_file("DATA/titanic_dataset_for_svm.csv")
    
    kernels = ["linear", "poly", "rbf", "sigmoid"]

    svm_model = svm.SVC()
    svm_model = svm_model.fit(features, labels)

    save_model(svm_model, "titanic_svm_model")

    svm_model_linear = svm.SVC(kernel="linear", C=1)
    svm_model_linear = svm_model_linear.fit(features, labels)

    save_model(svm_model_linear, "titanic_svm_linear_model")

    svm_model_poly = svm.SVC(kernel="poly", degree=3, coef0=0)
    svm_model_poly = svm_model_poly.fit(features, labels)

    save_model(svm_model_poly, "titanic_svm_poly_model")

    svm_model_rbf = svm.SVC(kernel="rbf", C=0.5, gamma=0.3)
    svm_model_rbf = svm_model_rbf.fit(features, labels)

    save_model(svm_model_rbf, "titanic_svm_rbf_model")

    svm_model_sigmoid = svm.SVC(kernel="sigmoid", gamma="scale")
    svm_model_sigmoid = svm_model_sigmoid.fit(features, labels)

    save_model(svm_model_sigmoid, "titanic_svm_sigmoid_model")

if __name__ == "__main__":
    print("-" * 50)
    build_svm()
    print("-" * 50)