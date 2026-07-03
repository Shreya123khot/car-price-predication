#streamlit run app.py
import streamlit as st
import pickle as pkl
import numpy as np
import pandas as pd

import streamlit as st
import pickle as pkl
import pandas as pd

# Page settings
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Hide the left sidebar completely
st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

# Load model
model = pkl.load(open("model.pkl", "rb"))

# Title
st.title("🚗 Car Price Predictor")

# Inputs
company = st.text_input("Enter Company")
name = st.text_input("Enter Car Name")

year = st.number_input(
    "Enter Year",
    min_value=2000,
    max_value=2024,
    step=1
)

kms_driven = st.number_input(
    "Enter Kilometers Driven",
    min_value=10000,
    max_value=400000,
    step=5000
)

fuel_type = st.selectbox(
    "Select Fuel Type",
    ["Petrol", "Diesel", "LPG"]
)

# Predict
if st.button("Predict Price"):

    df = pd.DataFrame({
        "company": [company],
        "name": [name],
        "year": [year],
        "kms_driven": [kms_driven],
        "fuel_type": [fuel_type]
    })

    prediction = model.predict(df)

    st.write("### Entered Details")
    st.dataframe(df)

    st.success(f"Predicted Price: ₹{prediction[0]:,.0f}")
