import streamlit as st
import joblib
model = joblib.load('heart_disease_model.pkl')
st.title('Heart Disease Risk Screening')
age = st.number_input('Age', 1, 120)
sex = st.selectbox('Sex', ['Male', 'Female'])
cp = st.selectbox('Chest Pain Type (0-3)', [0, 1, 2, 3])
trestbps = st.number_input('Resting Blood Pressure', 80, 220)
chol = st.number_input('Cholesterol (mg/dl)', 100, 600)
thalach = st.number_input('Max Heart Rate Achieved', 60, 220)
if st.button('Check Risk'):
  sex_val = 1 if sex == 'Male' else 0
  # Remaining fields filled with dataset medians for demo simplicity
  row = [age, sex_val, cp, trestbps, chol, 0, 1, thalach, 0, 1.0, 1, 0, 2]
  pred = model.predict([row])[0]
  st.warning('High Risk of Heart Disease') if pred == 1 else st.success('Low Risk')
