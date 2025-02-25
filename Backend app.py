from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
from database import init_db, insert_application, get_user_progress
from utils.helpers import calculate_monthly_payment, generate_recommendations, assess_borrowing_risk
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# Initialize the database
init_db()

# Load ML Model
model_path = os.path.join(os.path.dirname(__file__), 'models', 'loan_model.pkl')
try:
    with open(model_path, 'rb') as model_file:
        loan_model = pickle.load(model_file)
    print("✅ Loan model loaded successfully!")
except FileNotFoundError:
    print(f"❌ Error: Model file not found at {model_path}")
    loan_model = None

@app.route('/predict', methods=['POST'])
def predict_loan():
    try:
        if loan_model is None:
            print("❌ Loan model is not loaded. Returning error.")
            return jsonify({'error': 'Loan model not loaded', 'eligible': False, 'probability': 0.0}), 500

        # Get request data
        data = request.json
        required_fields = ['income', 'credit_score', 'loan_amount', 'loan_term', 'debt_to_income']

        # Validate input data
        for field in required_fields:
            if field not in data:
                print(f"❌ Missing field: {field}")
                return jsonify({'error': f'Missing field: {field}', 'eligible': False, 'probability': 0.0}), 400

        # Prepare feature array
        features = np.array([
            data['income'], data['credit_score'], data['loan_amount'], data['loan_term'], data['debt_to_income']
        ]).reshape(1, -1)

        # Make prediction
        prediction = loan_model.predict(features)[0]
        probability = loan_model.predict_proba(features)[0][1] if hasattr(loan_model, 'predict_proba') else 0.0

        # Compute monthly payment
        monthly_payment = calculate_monthly_payment(data['loan_amount'], data['loan_term'], 0.04)
        status = 'approved' if prediction == 1 else 'rejected'

        # Store application data
        application_data = {
            'user_id': data.get('user_id', 'anonymous'),
            'income': data['income'],
            'credit_score': data['credit_score'],
            'loan_amount': data['loan_amount'],
            'loan_term': data['loan_term'],
            'debt_to_income': data['debt_to_income'],
            'status': status,
            'probability': probability,
            'monthly_payment': monthly_payment,
            'timestamp': datetime.now().isoformat()
        }

        insert_application(application_data)

        # Generate recommendations & risk assessment
        recommendations = generate_recommendations(data, probability)
        risk_factors = assess_borrowing_risk(data, monthly_payment)

        # Ensure response includes all expected fields
        return jsonify({
            'eligible': bool(prediction),
            'probability': float(probability),  # Always include 'probability'
            'monthly_payment': monthly_payment,
            'recommendations': recommendations,
            'risk_factors': risk_factors
        })

    except Exception as e:
        print(f"❌ Error in /predict: {str(e)}")  # Log error
        return jsonify({
            'error': str(e),
            'eligible': False,
            'probability': 0.0,  # Ensure 'probability' key exists
            'monthly_payment': 0.0,
            'recommendations': [],
            'risk_factors': []
        }), 500

@app.route('/track_progress', methods=['GET'])
def track_progress():
    try:
        user_id = request.args.get('user_id', 'anonymous')
        applications = get_user_progress(user_id)

        return jsonify({
            'user_id': user_id,
            'applications': applications
        })

    except Exception as e:
        print(f"❌ Error in /track_progress: {str(e)}")  # Log error
        return jsonify({'error': str(e)}), 500
    
@app.route('/')
def home():
    return "Welcome to the Smart Loan Assistant API!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
