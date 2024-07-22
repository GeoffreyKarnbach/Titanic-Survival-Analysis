from flask import Flask, request, jsonify

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

ALLOWED_MODELS = ['decision_tree']

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
    
    # For demonstration, let's just return the received data as a confirmation
    response_data = {
        'pclass': prediction_request.pclass,
        'name': prediction_request.name,
        'sex': prediction_request.sex,
        'age': prediction_request.age,
        'sibsp': prediction_request.sibsp,
        'parch': prediction_request.parch,
        'ticket': prediction_request.ticket,
        'fare': prediction_request.fare,
        'cabin': prediction_request.cabin,
        'embarked': prediction_request.embarked,
        'model': prediction_request.model
    }
    
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=True)