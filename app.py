import streamlit as st
import joblib
import pandas as pd

model = joblib.load('model.pkl')

st.title("Will I Get Placed?")
st.write("Enter your details to predict your placement chances.")

cgpa = st.slider("CGPA", 0.0, 10.0, 7.0)
aptitude = st.slider("Aptitude Test Score", 0, 100, 70)
hsc = st.slider("HSC Marks", 0, 100, 70)
ssc = st.slider("SSC Marks", 0, 100, 70)
soft_skills = st.slider("Soft Skills Rating", 0.0, 10.0, 6.0)
projects = st.number_input("Number of Projects", 0, 20, 2)
internships = st.number_input("Number of Internships", 0, 10, 1)
workshops = st.number_input("Workshops/Certifications", 0, 10, 1)
extracurricular = st.selectbox("Extracurricular Activities", ["Yes", "No"])
placement_training = st.selectbox("Placement Training", ["Yes", "No"])

if st.button("Predict"):
    input_df = pd.DataFrame([{
        'CGPA': cgpa,
        'Internships': internships,
        'Projects': projects,
        'Workshops/Certifications': workshops,
        'AptitudeTestScore': aptitude,
        'SoftSkillsRating': soft_skills,
        'ExtracurricularActivities': extracurricular,
        'PlacementTraining': placement_training,
        'SSC_Marks': ssc,
        'HSC_Marks': hsc
    }])

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if prediction == 'Placed':
        st.success(f"✅ Likely to be Placed! (Confidence: {probability:.0%})")
    else:
        st.error(f"❌ Unlikely to be Placed (Confidence: {1-probability:.0%})")