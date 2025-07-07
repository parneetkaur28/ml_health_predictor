import streamlit as st
import numpy as np
import joblib
import os

# Load saved components
model = joblib.load(os.path.join("models", "cirrhosis_model.pkl"))
scaler = joblib.load(os.path.join("models", "scaler.pkl"))
poly = joblib.load(os.path.join("models", "poly.pkl"))
minmax_scaler = joblib.load(os.path.join("models", "minmax_scaler.pkl"))

# UI
st.set_page_config(page_title="Liver Cirrhosis")
st.title("LIVER CIRRHOSIS")
st.image(os.path.join("images", "liverimg.png"), width=400)

if st.button("LEARN ABOUT LIVER CIRRHOSIS"):
    st.write("Cirrhosis is scarring (fibrosis) of the liver caused by long-term liver damage. The scar tissue prevents the liver working properly. Cirrhosis is sometimes called end-stage liver disease because it happens after other stages of damage from conditions that affect the liver, such as hepatitis.")

st.write("Kindly fill below to get results:")

with st.form(key='input_form'):
    age = st.number_input("Age", step=1, value=0, format="%d")
    gen = st.number_input("Gender (M(1) or F(0))", step=1, value=0, format="%d")
    TB = st.number_input("Total bilirubin")
    DB = st.number_input("Direct bilirubin")
    AAP = st.number_input("Alkphos Alkaline Phosphotase", step=1, value=0, format="%d")
    Sgpt = st.number_input("Sgpt Alamine Aminotransferase", step=1, value=0, format="%d")
    sgot = st.number_input("Sgot Aspartate Aminotransferase", step=1, value=0, format="%d")
    tp = st.number_input("Total Proteins")
    alb = st.number_input("Albumin")
    ratio = st.number_input("A/G Ratio")
    cb = st.checkbox("I agree to provide my test results")

    submit_button = st.form_submit_button(label='Submit')

if submit_button and cb:
    user_input = np.array([age, gen, TB, DB, AAP, Sgpt, sgot, tp, alb, ratio]).reshape(1, -1)
    user_input_minmax = minmax_scaler.transform(user_input)
    user_input_poly = poly.transform(user_input_minmax)
    user_input_scaled = scaler.transform(user_input_poly)

    probability = model.predict_proba(user_input_scaled)[0][1]
    st.write(f'The probability of having liver cirrhosis is: {probability * 100:.2f}%')
