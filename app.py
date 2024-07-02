import pandas as pd
import streamlit as st
import joblib

# Load the trained model
model = joblib.load('best_model.pkl')

st.title("PMI Estimator")

max_temp = st.number_input("Max Temperature")
min_temp = st.number_input("Min Temperature")
avg_temp = st.number_input("Average Temperature")
ambient_temp = st.number_input("Ambient Temperature")
humidity = st.number_input("Humidity")

if st.button("Predict PMI"):
    temp_range = max_temp - min_temp
    input_data = pd.DataFrame({
        'Max': [max_temp],
        'Min': [min_temp],
        'Average': [avg_temp],
        'Ambient ': [ambient_temp],
        'Humidity': [humidity],
        'Temp_Range': [temp_range]
    })
    prediction = model.predict(input_data)
    st.write(f"Estimated PMI: {prediction[0]}")