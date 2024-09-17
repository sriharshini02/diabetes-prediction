import streamlit as st
import joblib
import numpy as np

# Load the best model
model = joblib.load("best_logistic_regression_model.pkl")


# Define the function to predict outcome
def predict(features):
    prediction = model.predict([features])
    return prediction[0]


# Define the Streamlit app
st.title("Diabetes Prediction App")

# Input fields for features
pregnancies = st.number_input(
    "Number of Pregnancies", min_value=0, max_value=20, value=0
)
glucose = st.number_input("Glucose Level", min_value=0, max_value=200, value=0)
blood_pressure = st.number_input(
    "Blood Pressure (mm Hg)", min_value=0, max_value=200, value=0
)
insulin = st.number_input("Insulin (IU)", min_value=0, max_value=1000, value=0)
bmi = st.number_input("BMI", min_value=0.0, max_value=100.0, value=0.0)
diabetes_pedigree = st.number_input(
    "Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.0
)
age = st.number_input("Age", min_value=0, max_value=120, value=0)

# Collect features
features = np.array(
    [
        pregnancies,
        glucose,
        blood_pressure,
        insulin,
        bmi,
        diabetes_pedigree,
        age,
    ]
)

# Predict button
if st.button("Predict"):
    result = predict(features)
    if result == 1:
        st.write("Prediction: Diabetes")
    else:
        st.write("Prediction: No Diabetes")
