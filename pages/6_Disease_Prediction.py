import streamlit as st
import joblib
import numpy as np

st.title("🧠 Disease Prediction AI")

model = joblib.load("models/disease_prediction/model.pkl")

age = st.number_input("Age", 1, 100)
bmi = st.number_input("BMI")
bp = st.number_input("Blood Pressure")
glucose = st.number_input("Glucose Level")
cholesterol = st.number_input("Cholesterol")

if st.button("Predict Disease"):

    input_data = np.array([[age, bmi, bp, glucose, cholesterol]])

    prediction = model.predict(input_data)

    st.success(f"🧠 Predicted Condition: {prediction[0]}")