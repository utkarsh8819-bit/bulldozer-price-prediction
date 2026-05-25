import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Bulldozer Price Predictor",
                   page_icon="🚜",
                   layout="centered")

st.title("🚜 Bulldozer Price Prediction")

st.markdown("### Enter Bulldozer Details")

# Inputs
year = st.number_input("Year Made", 1950, 2025, 2010)

hours = st.number_input("Machine Hours", 0, 100000, 5000)

product_size = st.selectbox(
    "Product Size",
    ["Mini", "Small", "Medium", "Large"]
)

enclosure = st.selectbox(
    "Enclosure Type",
    ["OROPS", "EROPS", "EROPS w AC"]
)

drive_system = st.selectbox(
    "Drive System",
    ["Two Wheel Drive", "Four Wheel Drive"]
)

hydraulics = st.selectbox(
    "Hydraulics",
    ["Standard", "Auxiliary"]
)

# Predict button
if st.button("Predict Price"):

    # Dummy logic
    prediction = (
        50000
        + (year * 10)
        - (hours * 2)
    )

    st.success(f"💰 Predicted Price: ${prediction:,.2f}")

    st.balloons()