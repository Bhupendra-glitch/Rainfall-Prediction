import streamlit as st
import numpy as np
import pickle

# Load your trained model
# model = pickle.load(open("rainfall_model.pkl", "rb"))

st.set_page_config(page_title="Rainfall Prediction", page_icon="🌧️")

st.title("🌦️ Rainfall Prediction System")
st.write("Fill in the weather details below and click **Predict** to estimate rainfall.")

# Input fields
day = st.number_input("Day of Month", 1, 31, 15)
pressure = st.number_input("Pressure (hPa)", 800, 1100, 1010)
maxtemp = st.number_input("Max Temperature (°C)", -10, 50, 30)
temperature = st.number_input("Average Temperature (°C)", -10, 50, 25)
mintemp = st.number_input("Min Temperature (°C)", -10, 50, 20)
dewpoint = st.number_input("Dew Point (°C)", -10, 35, 15)
humidity = st.slider("Humidity (%)", 0, 100, 70)
cloud = st.slider("Cloud Cover (%)", 0, 100, 50)
sunshine = st.number_input("Sunshine (hours)", 0.0, 12.0, 6.0, step=0.1)
winddirection = st.slider("Wind Direction (°)", 0, 360, 180)
windspeed = st.number_input("Wind Speed (km/h)", 0, 150, 10)

# Collect into numpy array
features = np.array([[day, pressure, maxtemp, temperature, mintemp,
                      dewpoint, humidity, cloud, sunshine,
                      winddirection, windspeed]])

# Prediction
if st.button("Predict"):
    prediction = model.predict(features)
    st.subheader(f"🌧️ Predicted Rainfall: {prediction[0]:.2f} mm")
