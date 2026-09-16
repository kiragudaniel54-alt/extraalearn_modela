
# Import necessary libraries
import numpy as np
import joblib  # For loading the serialized model
import pandas as pd  # For data manipulation
from flask import Flask, request, jsonify  # For creating the Flask API

# Initialize the Flask app with a name
learn_api = Flask("ExtraaLearn")

# Load the trained lead-conversion model pipeline (preprocessing + model)
model = joblib.load("learn_model.joblib")

# Home route - simple welcome / health-check message
@learn_api.get('/')
def home():
    return "Welcome to the Lead Prediction System"

# Endpoint to predict conversion for a single lead
@learn_api.post('/v1/predict')
def predict_lead():
    # Get the JSON payload from the request
    data = request.get_json()

    # Extract the lead's features from the input data
    sample = {
        'age': data['age'],
        'current_occupation': data['current_occupation'],
        'first_interaction': data['first_interaction'],
        'profile_completed': data['profile_completed'],
        'website_visits': data['website_visits'],
        'time_spent_on_website': data['time_spent_on_website'],
        'page_views_per_visit': data['page_views_per_visit'],
        'last_activity': data['last_activity'],
        'print_media_type1': data['print_media_type1'],
        'print_media_type2': data['print_media_type2'],
        'digital_media': data['digital_media'],
        'educational_channels': data['educational_channels'],
        'referral': data['referral']
    }

    # Convert the single record into a DataFrame (the pipeline expects tabular input)
    input_data = pd.DataFrame([sample])

    # Make a prediction (0 = not converted, 1 = converted)
    prediction = model.predict(input_data).tolist()[0]

    # Return the prediction as a JSON response
    return jsonify({'Lead': prediction})


# Run the Flask app in debug mode when executed directly
if __name__ == '__main__':
    learn_api.run(debug=True)
