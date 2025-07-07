import streamlit as st
import numpy as np
import pickle
import csv
import os

model_path = os.path.join("models", "finalized_model.sav")
with open(model_path, "rb") as file:
    model = pickle.load(file)

scaler_path = os.path.join("models", "scalercdk.pkl")
with open(scaler_path, "rb") as file:
    scaler = pickle.load(file)

st.title("CHRONIC KIDNEY DISEASE")
st.image(os.path.join("images", "kidneymain.png"), width=400)

if st.button("LEARN ABOUT Chronic Kidney Disease"):
    st.write("Chronic kidney disease (CKD) means your kidneys are damaged and can't filter blood the way they should. "
             "The main risk factors for developing kidney disease are diabetes, high blood pressure, heart disease, "
             "and a family history of kidney failure.")

st.write("Kindly fill the below form to get results:")

# Form to take input
with st.form(key='form2'):
    age = st.number_input("Age", 1.00, 100.00, step=1.00)
    BP = st.number_input("Blood Pressure (BP)")
    SG = st.number_input("Specific Gravity")
    AB = st.number_input("Albumin")
    Sgr = st.number_input("Sugar")
    RBC = st.radio("Red Blood Cell Status", options=["Normal", "Abnormal"], index=0, help="Normal or Abnormal")
    PC = st.radio("Pus Cell Status", options=["Normal", "Abnormal"], index=0, help="Normal or Abnormal")
    PCC = st.radio("Pus Cell Clumps", options=["Not Present", "Present"], index=0, help="Not Present or Present")
    bacteria = st.radio("Bacteria", options=["Not Present", "Present"], index=0, help="Not Present or Present")
    BGR = st.number_input("Blood Glucose Random")
    BU = st.number_input("Blood Urea")
    SC = st.number_input("Serum Creatinine")
    sodium = st.number_input("Sodium")
    potassium = st.number_input("Potassium")
    HB = st.number_input("Haemoglobin")
    PCV = st.number_input("Packed Cell Volume")
    WBC = st.number_input("White Blood Cell Count")
    RBC_count = st.number_input("Red Blood Cell Count")
    hypertension = st.radio("Hypertension", options=["Yes", "No"], help="Yes or No")
    diabetes = st.radio("Diabetes Mellitus", options=["Yes", "No"], help="Yes or No")
    CAD = st.radio("Coronary Artery Disease", options=["Yes", "No"], help="Yes or No")
    appetite = st.radio("Appetite", options=["Good", "Poor"], help="Good or Poor")
    pedal_edema = st.radio("Pedal Edema", options=["Yes", "No"], help="Yes or No")
    anemia = st.radio("Anemia", options=["Yes", "No"], help="Yes or No")
    
    cb = st.checkbox("I agree to provide my test results")
    sub = st.form_submit_button('Submit & Predict')

# Preprocess the inputs and predict when form is submitted
if sub and cb:
    # Convert radio button selections back to binary values
    RBC = 1 if RBC == "Normal" else 0
    PC = 1 if PC == "Normal" else 0
    PCC = 1 if PCC == "Not Present" else 0
    bacteria = 1 if bacteria == "Present" else 0
    hypertension = 1 if hypertension == "Yes" else 0
    diabetes = 1 if diabetes == "Yes" else 0
    CAD = 1 if CAD == "Yes" else 0
    appetite = 0 if appetite == "Good" else 1
    pedal_edema = 1 if pedal_edema == "Yes" else 0
    anemia = 1 if anemia == "Yes" else 0
    
    # Collect the user inputs into a tuple (same order as your model expects)
    user_input = (age, BP, SG, AB, Sgr, RBC, PC, PCC, bacteria, 
                  BGR, BU, SC, sodium, potassium, HB, PCV, WBC, 
                  RBC_count, hypertension, diabetes, CAD, appetite, 
                  pedal_edema, anemia)
    
    # Convert to NumPy array
    user_input_np = np.asarray(user_input)
    
    # Reshape input for the model
    res_input_unsc = user_input_np.reshape(1, -1)
    
    # Scale the input using the pre-trained scaler
    res_input = scaler.transform(res_input_unsc)
    
    # Predict using the loaded model
    probability_of_ckd = model.predict_proba(res_input)[:, 0]  # Probability of having CKD
    prediction = model.predict(res_input)  # Prediction (0 or 1)

    # Calculate percentage probability
    percentage_probability = probability_of_ckd * 100

    # Save results to a CSV file
    #with open('results.csv', 'a') as f:
        #csv_writer = csv.writer(f)
        #csv_writer.writerow([probability_of_ckd[0], prediction[0]])

    # Display the results
    st.write(f"Prediction: {'CKD' if prediction[0] == 1 else 'No CKD'}")
    st.write(f"The probability of having Chronic Kidney Disease (CKD) is: {percentage_probability[0]:.2f}%")
