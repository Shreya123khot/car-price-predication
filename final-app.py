#streamlit run app.py
import streamlit as st
import pickle as pkl
import numpy as np
import pandas as pd

st.title("Car Price Predictor")

company = st.text_input("Enter company")
name = st.text_input("Enter car name")
year = st.number_input("Enter year", min_value=2000, max_value=2024, 
                       step=1)
kms_driven = st.number_input("Enter kilometers driven", 
                             min_value=10000, max_value=400000, 
                             step = 5000)
fuel_type = st.selectbox("Select fuel type", ["Petrol", "Diesel", "LPG"])

if st.button("Predict Price"):
    model = pkl.load(open("model.pkl", "rb+"))
    data = [[company, name, year, kms_driven, fuel_type]]
    columns = ['company', 'name', 'year', 'kms_driven', 'fuel_type']
    df = pd.DataFrame(data, columns=columns)
    st.write(df)
    result = model.predict(df)
    st.write("Predicted price:", round(result[0][0]))

