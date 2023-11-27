from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb+srv://Gurunathan:Gurunathan11@cluster0.aeeridr.mongodb.net/serverData')
db = client['patient_register']
patients_collection = db['patients']

# API Endpoint to add a new patient
@app.route('/api/patient/register', methods=['POST'])
def add_patient():
    data = request.get_json()
    # Assuming the JSON contains 'name', 'age', 'gender' fields
    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')
    problem = data.get('problem')
    alergy = data.get('alergy')

    if name and age and gender and problem and alergy:
        new_patient = {
            'name': name,
            'age': age,
            'gender': gender,
            'problem' : problem,
            'alergy' : alergy
        }
        # Insert the new patient into MongoDB
        result = patients_collection.insert_one(new_patient)
        return jsonify({'message': 'Patient added successfully', "patientData":data}), 201
    else:
        return jsonify({'message': 'Incomplete data provided'}), 400

@app.route('/api/patient/register', methods=['GET'])
def get_all_patients():
    try:
        patients = list(patients_collection.find())
        return jsonify({'patients': patients}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
