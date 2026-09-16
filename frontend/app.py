
import streamlit as st
import requests

# Base URL of the Flask backend.
# For a docker-compose setup this is the backend service name; for two separate
# Hugging Face Spaces, replace it with the backend Space's public URL.
BACKEND_URL = "http://backend:7860"

# Page title
st.title("Lead Prediction System")
st.write(
    "Enter the lead details below to predict whether the lead will convert."
)

# Input fields for each feature the model expects
age = st.number_input("Age", min_value=0, value=25)
current_occupation = st.selectbox("Current Occupation", ["Professional", "Unemployed", "Student"])
first_interaction = st.selectbox("First Interaction Platform", ["Website", "Mobile App"])
profile_completed = st.selectbox("Profile Completion Level", ["Low", "Medium", "High"])
website_visits = st.number_input("Number of Website Visits", min_value=0, value=3)
time_spent_on_website = st.number_input("Time Spent on Website (in seconds)", min_value=0.0, value=180.0)
page_views_per_visit = st.number_input("Page Views per Visit", min_value=0.0, value=4.5)
last_activity = st.selectbox("Last Activity Type", ["Email Activity", "Phone Activity", "Website Activity"])
print_media_type1 = st.selectbox("Seen Newspaper Ad?", ["Yes", "No"])
print_media_type2 = st.selectbox("Seen Magazine Ad?", ["Yes", "No"])
digital_media = st.selectbox("Seen Digital Media Ad?", ["Yes", "No"])
educational_channels = st.selectbox("Heard via Educational Channels?", ["Yes", "No"])
referral = st.selectbox("Heard via Referral?", ["Yes", "No"])


# Assemble the inputs into the JSON payload the API expects
lead_data = {
    "age": age,
    "current_occupation": current_occupation,
    "first_interaction": first_interaction,
    "profile_completed": profile_completed,
    "website_visits": website_visits,
    "time_spent_on_website": time_spent_on_website,
    "page_views_per_visit": page_views_per_visit,
    "last_activity": last_activity,
    "print_media_type1": print_media_type1,
    "print_media_type2": print_media_type2,
    "digital_media": digital_media,
    "educational_channels": educational_channels,
    "referral": referral
}


# On button click, send the request to the backend and display the result
if st.button("Predict", type='primary'):

    response = requests.post(
        f"{BACKEND_URL}/v1/predict",
        json=lead_data
    )

    if response.status_code == 200:
        result = response.json()
        predicted_value = result["Lead"]
        st.success(f"Predicted Lead Conversion: {predicted_value}")
    else:
        st.error("Unable to connect to the prediction API.")
