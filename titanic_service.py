from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import joblib
import sys
import os
import csv

sys.path.append(os.path.join(os.path.dirname(__file__), 'ModelTraining'))

from ModelTraining.evaluate_decision_tree import evaluate_passenger_request_v1, evaluate_passenger_request_v_n, evaluate_passenger_request_v7
from ModelTraining.evaluate_svm import evaluate_passenger_request_svm
from ModelTraining.evaluate_gradient_boosting import evaluate_passenger_request_gradient_boosting
from ModelTraining.evaluate_knn import evaluate_passenger_request_knn
from ModelTraining.evaluate_log_reg import evaluate_passenger_request_log_reg
from ModelTraining.evaluate_random_forest import evaluate_passenger_request_random_forest

class PredictionRequest:
    def __init__(self, pclass, name, sex, age, sibsp, parch, ticket, fare, cabin, embarked, model):
        self.pclass = pclass
        self.name = name
        self.sex = sex
        self.age = age
        self.sibsp = sibsp
        self.parch = parch
        self.ticket = ticket
        self.fare = fare
        self.cabin = cabin
        self.embarked = embarked

        self.model = model

app = Flask(__name__)
CORS(app)

ALLOWED_MODELS = [
    'decision_tree_v1',
    'decision_tree_v2',
    'decision_tree_v3',
    'decision_tree_v4',
    'decision_tree_v5',
    'decision_tree_v6',
    'decision_tree_v7',
    'gradient_boosting',
    'knn',
    'log_reg',
    'random_forest',
    'svm',
    'svm_linear',
    'svm_poly',
    'svm_rbf',
    'svm_sigmoid'
]


@app.route('/', methods=['GET'])
def index():
    return 'Welcome to Titanic Prediction Service!'

@app.route('/models', methods=['GET'])
def models():
    return jsonify({'models': ALLOWED_MODELS}), 200

@app.route('/benchmark', methods=['GET'])
def benchmark():
    return jsonify(benchmark_for_models()), 200

@app.route('/dataset', methods=['GET'])
def get_dataset_file():
    return send_file('Data/titanic_dataset_for_decision_tree_v7.csv', as_attachment=True, download_name='processed_dataset.csv')

@app.route('/prediction', methods=['POST'])
def prediction():
    data = request.get_json()
    
    # Validate the required fields
    required_fields = ['pclass', 'name', 'sex', 'age', 'sibsp', 'parch', 'ticket', 'fare', 'cabin', 'embarked', 'model']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400
    
    # Validate the model field4
    if data['model'] not in ALLOWED_MODELS and data['model'] != '*':
        return jsonify({'error': f"Invalid model. Allowed models are: {', '.join(ALLOWED_MODELS)}"}), 400
    
    # Create an instance of PredictionRequest
    prediction_request = PredictionRequest(
        pclass=data['pclass'],
        name=data['name'],
        sex=data['sex'],
        age=data['age'],
        sibsp=data['sibsp'],
        parch=data['parch'],
        ticket=data['ticket'],
        fare=data['fare'],
        cabin=data['cabin'],
        embarked=data['embarked'],
        model=data['model']
    )

    response = None

    if prediction_request.model == 'decision_tree_v1':
        response = {"Survived":evaluate_passenger_request_v1(prediction_request), "model": prediction_request.model}
    elif prediction_request.model[0:15] == 'decision_tree_v' and prediction_request.model[-1] in ['2', '3', '4', '5', '6']:
        response = {"Survived":evaluate_passenger_request_v_n(prediction_request, int(prediction_request.model[-1])), "model": prediction_request.model}
    elif prediction_request.model == 'decision_tree_v7':
        response = {"Survived":evaluate_passenger_request_v7(prediction_request), "model": prediction_request.model}
    elif prediction_request.model == '*':
        response = {"Survived":predict_all_models(prediction_request), "model": prediction_request.model}
    elif prediction_request.model == 'gradient_boosting':
        response = {"Survived":evaluate_passenger_request_gradient_boosting(prediction_request), "model": prediction_request.model}
    elif prediction_request.model == 'knn':
        response = {"Survived":evaluate_passenger_request_knn(prediction_request), "model": prediction_request.model}
    elif prediction_request.model == 'log_reg':
        response = {"Survived":evaluate_passenger_request_log_reg(prediction_request), "model": prediction_request.model}
    elif prediction_request.model == 'random_forest':
        response = {"Survived":evaluate_passenger_request_random_forest(prediction_request), "model": prediction_request.model}
    elif prediction_request.model.startswith('svm'):
        response = {"Survived":evaluate_passenger_request_svm(prediction_request, prediction_request.model), "model": prediction_request.model}
    else:
        return jsonify({'error': 'Model prediction not implemented yet.'}), 501
    
    return jsonify(response), 200

def predict_all_models(request_data):
    temp = {}

    temp["decision_tree_v1"] = evaluate_passenger_request_v1(request_data)

    for model_version in range(2, 7):
        temp[f"decision_tree_v{model_version}"] = evaluate_passenger_request_v_n(request_data, model_version)

    temp["decision_tree_v7"] = evaluate_passenger_request_v7(request_data)

    temp["gradient_boosting"] = evaluate_passenger_request_gradient_boosting(request_data)
    temp["knn"] = evaluate_passenger_request_knn(request_data)
    temp["log_reg"] = evaluate_passenger_request_log_reg(request_data)
    temp["random_forest"] = evaluate_passenger_request_random_forest(request_data)

    for svm_model in ['svm', 'svm_linear', 'svm_poly', 'svm_rbf', 'svm_sigmoid']:
        temp[svm_model] = evaluate_passenger_request_svm(request_data, svm_model)
    
    
    return temp

def benchmark_for_models():
    result = {}

    for model in ALLOWED_MODELS:
        result[model] = None

    with open("evaluation.csv","r") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            result[row[0].split(".")[0]] = float(row[1])
    
    return result

if __name__ == '__main__':
    app.run(debug=True, port=8000)