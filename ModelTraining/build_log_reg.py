from sklearn import linear_model 
import joblib
import os
from shared import get_feature_and_labels_array_from_file, save_model

def build_log_reg():
    features, labels = get_feature_and_labels_array_from_file("DATA/titanic_dataset_for_log_reg.csv")

    log_reg_model = linear_model.LogisticRegression()
    log_reg_model = log_reg_model.fit(features, labels)

    save_model(log_reg_model, "titanic_log_reg_model")

if __name__ == "__main__":
    print("-" * 50)
    build_log_reg()
    print("-" * 50)