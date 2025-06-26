import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Background image using HTML/CSS
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://img.freepik.com/free-photo/health-still-life-with-copy-space_23-2148854031.jpg?semt=ais_hybrid&w=740");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    .main-title {
        font-weight: bold;
        font-size: 36px;
        color: #ffffff;
        text-shadow: 1px 1px 4px black;
    }
    .disclaimer {
        color: #f5f5f5;
        background-color: rgba(0,0,0,0.4);
        padding: 10px;
        border-radius: 10px;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">💓 Heart Disease Prediction</div>', unsafe_allow_html=True)

st.markdown("""
<div class="disclaimer">
<b>Disclaimer:</b> This model showed only <b>78% accuracy</b> on a small dataset. It is not a substitute for professional medical advice.
</div>
""", unsafe_allow_html=True)

st.markdown("#### 📝 Input patient data below:")

cp = st.selectbox(
    "**Chest pain type:**\n\n0 = Typical angina\n1 = Atypical angina\n2 = Non-anginal pain\n3 = Asymptomatic",
    [0, 1, 2, 3]
)
thalach = st.number_input("**Maximum Heart Rate (thalach):**", min_value=60, max_value=250, value=150)
oldpeak = st.number_input("**ST depression (oldpeak):**", min_value=0.0, max_value=6.0, value=1.0, step=0.1)
exang = st.selectbox("**Exercise Induced Angina (exang):**  1 = Yes, 0 = No", [0, 1])
ca = st.selectbox("**Number of major vessels (ca):**", [0, 1, 2, 3])
thal = st.selectbox("**Thalassemia (thal):** 1 = Fixed defect, 2 = Normal, 3 = Reversible defect", [0, 1, 2, 3])
slope = st.selectbox("**Slope of ST segment (slope):** 0 = Upsloping, 1 = Flat, 2 = Downsloping", [0, 1, 2])
age = st.number_input("**Age:**", min_value=10, max_value=100, value=50)
sex = st.selectbox("**Sex:** 0 = Female, 1 = Male", [0, 1])

if st.button("🔍 Predict"):
    input_data =  pd.DataFrame([[cp, thalach, oldpeak, exang, ca, thal, slope, age, sex]],
                        columns=['cp', 'thalach', 'oldpeak', 'exang', 'ca', 'thal', 'slope', 'age', 'sex'])
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.markdown("""
<div style='background-color: #ffdddd; padding: 10px; border-radius: 5px; color: red; font-size: 18px; font-weight: bold;'>
🩺 The model predicts: Heart Disease Detected
</div>
""", unsafe_allow_html=True)
    else:
        st.markdown("""
<div style='background-color: #ffdddd; padding: 10px; border-radius: 5px; color: green; font-size: 18px; font-weight: bold;'>
"✅ The model predicts: No Heart Disease"
</div>
""", unsafe_allow_html=True)
        
