from sklearn import ensemble 
from shared import get_feature_and_labels_array_from_file, save_model

def build_gradient_boosting():
    features, labels = get_feature_and_labels_array_from_file("DATA/titanic_dataset_for_gradient_boosting.csv")

    gradient_boosting_model = ensemble.GradientBoostingClassifier(random_state=2024, n_estimators=100)
    gradient_boosting_model = gradient_boosting_model.fit(features, labels)

    save_model(gradient_boosting_model, "titanic_gradient_boosting_model")

if __name__ == "__main__":
    print("-" * 50)
    build_gradient_boosting()
    print("-" * 50)