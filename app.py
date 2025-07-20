import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load model and column names
model = joblib.load("model/churn_model.pkl")
columns = joblib.load("model/columns.pkl")  # ✅ load feature column order

st.title("🔮 Customer Churn Prediction App")

# User Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72)
monthly = st.number_input("Monthly Charges", 0.0)
total = st.number_input("Total Charges", 0.0)
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])

# Encode inputs manually (as used in training)
gender = 1 if gender == "Male" else 0
senior = 1 if senior == "Yes" else 0

# Start with a base input row
input_dict = {
    'gender': gender,
    'SeniorCitizen': senior,
    'tenure': tenure,
    'MonthlyCharges': monthly,
    'TotalCharges': total,
    'Contract_Month-to-month': 0,
    'Contract_One year': 0,
    'Contract_Two year': 0,
    'InternetService_DSL': 0,
    'InternetService_Fiber optic': 0,
    'InternetService_No': 0,
    'PaymentMethod_Bank transfer (automatic)': 0,
    'PaymentMethod_Credit card (automatic)': 0,
    'PaymentMethod_Electronic check': 0,
    'PaymentMethod_Mailed check': 0,
    # Add other features here if needed
}

# Set the right one to 1
input_dict[f'Contract_{contract}'] = 1
input_dict[f'InternetService_{internet}'] = 1
input_dict[f'PaymentMethod_{payment}'] = 1

# Create full input vector with all expected columns
input_vector = []
for col in columns:
    value = input_dict.get(col, 0)  # get value or 0 if missing
    input_vector.append(value)

# Predict
if st.button("Predict Churn"):
    prediction = model.predict([input_vector])
    if prediction[0] == 1:
        st.error("⚠️ This customer is likely to CHURN.")
    else:
        st.success("✅ This customer is likely to STAY.")
