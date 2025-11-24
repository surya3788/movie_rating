import streamlit as st
import pandas as pd
import joblib

st.title("🎬 Movie Rating Prediction App")

# Load model safely (no success message)
try:
    model = joblib.load("movie_rating_model.pkl")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Input fields
movie_name = st.text_input("Enter Movie Name")

year = st.number_input("Enter Movie Year", min_value=1900, max_value=2030, value=2020)
runtime = st.number_input("Enter Runtime (minutes)", min_value=30, max_value=300, value=120)
total_gross = st.number_input("Enter Total Gross (in Millions)", min_value=0.0, value=10.0)

# Prediction button
if st.button("Predict Rating"):

    # Check movie name filled
    if not movie_name.strip():
        st.error("⚠ Please enter a movie name before predicting.")
        st.stop()

    # Input features (must match model)
    input_data = pd.DataFrame({
        "Year": [year],
        "Runtime(Mins)": [runtime]
    })

    try:
        prediction = model.predict(input_data)[0]
        st.success(f"⭐ Predicted Rating for '{movie_name}': {round(prediction, 2)}")
        st.info(f"Total Gross Entered: {total_gross} Million")
    except Exception as e:
        st.error(f"Model prediction failed: {e}")



