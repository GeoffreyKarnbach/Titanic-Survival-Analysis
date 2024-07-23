from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from DecisionTree.evaluate_decision_tree import evaluate_passenger_request_v1

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

ALLOWED_MODELS = ['decision_tree_v1']

@app.route('/', methods=['GET'])
def index():
    return 'Welcome to Titanic Prediction Service!'

@app.route('/prediction', methods=['POST'])
def prediction():
    data = request.get_json()
    
    # Validate the required fields
    required_fields = ['pclass', 'name', 'sex', 'age', 'sibsp', 'parch', 'ticket', 'fare', 'cabin', 'embarked', 'model']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400
    
    # Validate the model field4
    if data['model'] not in ALLOWED_MODELS:
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
        response = {"Survived":predict_decision_tree(prediction_request)}

    print(response)
    return jsonify(response), 200

def predict_decision_tree(request_data):
    return evaluate_passenger_request_v1(request_data)
    

if __name__ == '__main__':
    app.run(debug=True, port=8000)