# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 23:32:46 2024
diabetes
@author: adity
"""

import numpy as np
import streamlit as st
import pickle

# loading the saved model
loaded_model = pickle.load(open('C:/Users/hp/OneDrive/Desktop/ML_project/trainedmodel2.sav', 'rb'))

# creating a function for prediction
def diabetes_prediction(input_data):
    # change the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)  # Convert input to float
    # reshaping the numpy array as we are only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    if prediction[0] == 0:
        return 'Person does not have diabetes'
    else:
        return 'Person has heart diabetes'


def main():
    
    
    # giving a title
    st.title('Diabetes Prediction Web App')
    
    
    # getting the input data from the user
    
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)
        
if __name__ == '__main__':
    main()