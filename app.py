import streamlit as st   
import pandas as pd   
import numpy as np   
import joblib   

st.set_page_config(page_title="Diabetes Prediction", layout="wide")   

st.markdown(
    "<h1 style='text-align:center; color:white; font-size:48px;'>🩺 Diabetes Risk Predictor</h1>", 
    unsafe_allow_html=True
)   
st.markdown("---")   

model = joblib.load("xgb_model.joblib") 

st.subheader("Enter Patient Data")   
   
def user_input_features():   
    pregnancies = st.number_input("Pregnancies", 0, 15, 1)   
    glucose = st.number_input("Glucose", 50, 250, 120)   
    blood_pressure = st.number_input("BloodPressure", 40, 120, 70)   
    skin_thickness = st.number_input("SkinThickness", 10, 60, 20)   
    insulin = st.number_input("Insulin", 15, 600, 80)   
    bmi = st.number_input("BMI", 10.0, 50.0, 25.0)   
    dpf = st.number_input("DiabetesPedigreeFunction", 0.0, 3.0, 0.5)   
    age = st.number_input("Age", 10, 100, 30)   
   
    data = {   
        "Pregnancies": pregnancies,   
        "Glucose": glucose,   
        "BloodPressure": blood_pressure,   
        "SkinThickness": skin_thickness,   
        "Insulin": insulin,   
        "BMI": bmi,   
        "DiabetesPedigreeFunction": dpf,   
        "Age": age,   
        "Glucose_BMI": glucose*bmi,   
        "Pregnancy_per_Age": pregnancies/age if age > 0 else 0,   
        "Glucose_Insulin_ratio": glucose/insulin if insulin > 0 else 0,   
        "Age_group_Young": int(age < 30),   
        "Age_group_Middle": int(30 <= age < 50),   
        "Age_group_Old": int(age >= 50),   
        "BMI_group_Underweight": int(bmi < 18.5),   
        "BMI_group_Normal": int(18.5 <= bmi < 25),   
        "BMI_group_Overweight": int(25 <= bmi < 30),   
        "BMI_group_Obese": int(bmi >= 30)   
    }   
    features = pd.DataFrame(data, index=[0])   
    return features   
   
input_df = user_input_features()   

if st.button("🔮 Predict"):   
    y_proba = model.predict_proba(input_df)[0]   
    y_pred = model.predict(input_df)[0]   
    prob = y_proba[1]  # probability of being diabetic 
   
    st.subheader("Prediction Results")   
       
    st.markdown(
        f"<h2 style='color:#FFD700;'>Predicted Class: {'Diabetic 🧬' if y_pred==1 else 'Non-Diabetic ✅'}</h2>", 
        unsafe_allow_html=True
    )   
    st.markdown(
        f"<h3 style='color:#87CEEB;'>Probability of Diabetes: {prob*100:.2f}%</h3>", 
        unsafe_allow_html=True
    )   

    # Explanation 
    if y_pred == 1: 
        st.error("⚠️ The model suggests a **high risk of diabetes**. Please consult a doctor for further checkup.") 
    else: 
        st.success("✅ The model suggests **low risk of diabetes**. Keep maintaining a healthy lifestyle.") 
