import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('fraud_model.pkl')

# Define feature names
feature_names = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
                 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
                 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']

st.title("Credit Card Fraud Detection")

# Single input box for all features
csv_input = st.text_input("Enter 29 comma-separated values (V1–V28 and Amount)", "")

if st.button("Predict"):
    try:
        # Convert CSV string to list of floats
        user_input = [float(x.strip()) for x in csv_input.split(",")]
        
        if len(user_input) != 29:
            st.error("Please enter exactly 29 comma-separated values.")
        else:
            input_df = pd.DataFrame([user_input], columns=feature_names)
            prediction = model.predict(input_df)
            result = "🔴 Fraudulent Transaction" if prediction[0] == 1 else "🟢 Normal Transaction"
            st.success(f"Prediction: {result}")
    except ValueError:
        st.error("Invalid input. Please make sure all values are numbers.")
