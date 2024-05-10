# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:12:15 2024

@author: satyam
"""
import pickle
import streamlit as st
import pandas as pd
import base64
from streamlit_option_menu import option_menu

# Loading the saved models
diabetes_model = pickle.load(open('C:/Users/hp/OneDrive/Desktop/ML_projec/trainedmodel2.sav', 'rb'))
heartdisease_model = pickle.load(open('C:/Users/hp/OneDrive/Desktop/ML_project/trainedmodel1.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Heart disease Prediction'],
                           icons=['activity', 'heart'],
                           default_index=0)

# Custom CSS for the main container to set background image and style the typewriter effect with rainbow color
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://www.bing.com/images/search?view=detailV2&ccid=YRIUUjhc&id=691359301239131BD2CCE4A4177E1EF3AC7C307F&thid=OIP.YRIUUjhcIMvBEf_bbOdpUwHaEU&mediaurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.61121452385c20cbc111ffdb6ce76953%3frik%3dfzB8rPMefhek5A%26riu%3dhttp%253a%252f%252fwww.freelargeimages.com%252fwp-content%252fuploads%252f2014%252f12%252fBlack_background-4.jpg%26ehk%3d1054B1Uk9XqjWaIg%252bctfR694YHnNp2bsVX6YLZRJEXk%253d%26risl%3d%26pid%3dImgRaw%26r%3d0&exph=3646&expw=6250&q=black+bg+image&simid=608009396662193246&FORM=IRPRST&ck=3255654E9983D334152E11B13638A534&selectedIndex=2&itb=0");
        background-size: cover;
    }}
    @keyframes typing {{
        0% {{ width: 0; color: red }}
        10% {{ color: orange }}
        
        30% {{ color: green }}
        
        50% {{ color: indigo }}
        
        70% {{ color: pink }}
        80% {{ color: cyan }}
        90% {{ color: magenta }}
        100% {{ width: 100%; color: red }}
    }}
    .typing-animation {{
        overflow: hidden;
        animation: typing 7s steps(40, end) infinite alternate;
        white-space: nowrap;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Function to save input and output data to CSV
def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

# Function to download CSV file
def download_csv(data, filename):
    csv = pd.DataFrame(data).to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">Download CSV File</a>'
    return href

# Diabetes prediction page
# if selected == 'Diabetes Prediction':
#     # Page title with typewriter effect and rainbow color
#     st.markdown('<h1 class="typing-animation">Diabetes Prediction using ML</h1>', unsafe_allow_html=True)
#
#     # Getting the input data from the user
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         Pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=17)
#         SkinThickness = st.number_input('Skin Thickness value', min_value=0, max_value=100)
#         DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0, max_value=2)
#     with col2:
#         Glucose = st.number_input('Glucose Level', min_value=0, max_value=200)
#         Insulin = st.number_input('Insulin Level', min_value=0, max_value=890)
#         BMI = st.number_input('BMI value', min_value=0, max_value=70)
#     with col3:
#         BloodPressure = st.number_input('Blood Pressure value', min_value=0, max_value=140)
#         Age = st.number_input('Age between 20 to 100', min_value=20, max_value=100)
#
#     # Code for Prediction
#     diab_diagnosis = ''
#     # Creating a button for Prediction
#     if st.button('Diabetes Test Result'):
#         user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
#                       BMI, DiabetesPedigreeFunction, Age]
#         user_input = [float(x) for x in user_input]
#         diab_prediction = diabetes_model.predict([user_input])
#         if diab_prediction[0] == 1:
#             diab_diagnosis = 'The person is diabetic'
#         else:
#             diab_diagnosis = 'The person is not diabetic'
#
#         # Save input and output to CSV
#         data = {'Pregnancies': [Pregnancies],
#                 'Glucose': [Glucose],
#                 'BloodPressure': [BloodPressure],
#                 'SkinThickness': [SkinThickness],
#                 'Insulin': [Insulin],
#                 'BMI': [BMI],
#                 'DiabetesPedigreeFunction': [DiabetesPedigreeFunction],
#                 'Age': [Age],
#                 'Diagnosis': [diab_diagnosis]}
#         save_to_csv(data, 'diabetes_prediction_output.csv')
#
#         # Download CSV button
#         st.markdown(download_csv(data, 'diabetes_prediction_output.csv'), unsafe_allow_html=True)
#     st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart disease Prediction':
    # Page title with typewriter effect and rainbow color
    st.markdown('<h1 class="typing-animation">Heart Disease Prediction using ML</h1>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Age between 1 to 100', min_value=1, max_value=100)
        trestbps = st.number_input('Resting Blood Pressure', min_value=90, max_value=200)
        restecg = st.number_input('Resting Electrocardiographic results', min_value=0, max_value=2)
    with col2:
        sex = st.number_input('Sex 1 = male 0=female', min_value=0, max_value=1)
        chol = st.number_input('Serum Cholestoral in mg/dl', min_value=110, max_value=570)
        thalach = st.number_input('Maximum Heart Rate achieved', min_value=60, max_value=210)
    with col3:
        cp = st.number_input('Chest Pain types', min_value=0, max_value=3)
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl', min_value=0, max_value=1)
        exang = st.number_input('Exercise Induced Angina', min_value=0, max_value=1)
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise', min_value=0, max_value=6)
        slope = st.number_input('Slope of the peak exercise ST segment', min_value=0, max_value=2)
    with col2:
        ca = st.number_input('Major vessels colored by flourosopy', min_value=0, max_value=4)
        thal = st.number_input('thal: 1 = normal; 2 = fixed defect; 3 = reversable defect', min_value=0, max_value=3)

    # Code for Prediction
    heart_diagnosis = ''
    # Creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heartdisease_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
        
        # Save input and output to CSV
        data = {'Age': [age],
                'Sex': [sex],
                'Chest Pain types': [cp],
                'Resting Blood Pressure': [trestbps],
                'Serum Cholestoral': [chol],
                'Fasting Blood Sugar': [fbs],
                'Resting Electrocardiographic results': [restecg],
                'Maximum Heart Rate achieved': [thalach],
                'Exercise Induced Angina': [exang],
                'ST depression induced by exercise': [oldpeak],
                'Slope of the peak exercise ST segment': [slope],
                'Major vessels colored by flourosopy': [ca],
                'Thal': [thal],
                'Diagnosis': [heart_diagnosis]}
        save_to_csv(data, 'heart_disease_prediction_output.csv')
        
        # Download CSV button
        st.markdown(download_csv(data, 'heart_disease_prediction_output.csv'), unsafe_allow_html=True)
    st.success(heart_diagnosis)


















