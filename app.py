import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("movie_rating_model.pkl")

st.title("🎬 Movie Rating Prediction App")

# Input fields
movie_name = st.text_input("Enter Movie Name")

year = st.number_input("Enter Movie Year", min_value=1900, max_value=2030, value=2020)

runtime = st.number_input("Enter Runtime (minutes)", min_value=30, max_value=300, value=120)

total_gross = st.number_input("Enter Total Gross (in Millions)", min_value=0.0, value=10.0)

# Predict button
if st.button("Predict Rating"):
    
    # Prepare input (using only features the model was trained on)
    input_data = pd.DataFrame({
        "Year": [year],
        "Runtime(Mins)": [runtime]
    })

    prediction = model.predict(input_data)[0]
    st.success(f"⭐ Predicted Rating for '{movie_name}': {round(prediction, 2)}")

    st.info(f"Total Gross Entered: {total_gross} Million")
