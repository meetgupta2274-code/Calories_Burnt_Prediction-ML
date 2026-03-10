import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("models/model.pkl", "rb"))

st.title("🔥 Calories Burnt Prediction")
st.write("Predict calories burnt based on exercise details")


gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=10, max_value=100)
height = st.number_input("Height (cm)")
weight = st.number_input("Weight (kg)")
duration = st.number_input("Exercise Duration (minutes)")
heart_rate = st.number_input("Heart Rate")
body_temp = st.number_input("Body Temperature")

gender_value = 0 if gender == "Male" else 1


if st.button("Predict Calories"):

    input_data = np.array([
        gender_value,
        age,
        height,
        weight,
        duration,
        heart_rate,
        body_temp
    ]).reshape(1, -1)

    prediction = model.predict(input_data)

    st.success(f"Estimated Calories Burnt: {prediction[0]:.2f}")