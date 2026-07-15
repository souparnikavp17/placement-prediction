# Student Placement Prediction

A machine learning project that predicts whether a student will be placed
based on their academic performance, skills, and extracurricular profile.

Live app: https://placement-prediction-nqkue8rpetkcmynz8kyf4c.streamlit.app/

---

## About

Built a Random Forest classifier on a dataset of 10,000 students achieving
73.5% accuracy. The project includes exploratory data analysis, a training
pipeline, and a Streamlit app where you can enter your own details and get
a prediction.

## Findings

Aptitude test score and HSC marks turned out to be the strongest predictors
of placement — stronger than CGPA, which is counterintuitive but backed by
the data. Placement training also had a meaningful positive impact.

## Stack

Python, pandas, scikit-learn, matplotlib, seaborn, streamlit

## Run Locally

```bash
git clone https://github.com/souparnikavp17/placement-prediction.git
cd placement-prediction
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```