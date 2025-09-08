import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open('../model/model.pkl', 'rb'))

st.title("💰 Ecommerce Customer Spending Predictor")

st.write("Enter customer details below to predict their **Yearly Amount Spent**")

# Input fields
avg_session = st.number_input("Average Session Length", min_value=0.0, step=0.1)
time_on_app = st.number_input("Time on App (minutes)", min_value=0.0, format="%.2f")
time_on_website = st.number_input("Time on Website (minutes)", min_value=0.0, format="%.2f")
membership_length = st.number_input("Length of Membership (years)", min_value=0.0, format="%.2f")

if st.button("Predict Spending"):
    # Convert input to array
    input_data = np.array([[avg_session,time_on_app, time_on_website, membership_length]])
    prediction = model.predict(input_data)
    st.success(f"💵 Predicted Yearly Amount Spent: **${prediction[0]:.2f}**")
