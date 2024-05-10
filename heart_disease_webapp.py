# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 14:12:52 2024

@author: satyam
"""

import numpy as np
import streamlit as st
import pickle

# loading the saved model
loaded_model = pickle.load(open('C:/Users/hp/OneDrive/Desktop/ML_project/trainedmodel1.sav', 'rb'))

# creating a function for prediction
def heart_prediction(input_data):
    # change the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)  # Convert input to float
    # reshaping the numpy array as we are only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    if prediction[0] == 0:
        return 'Person does not have heart disease'
    else:
        return 'Person has heart disease'


def main():
    # giving a Title
    st.title('Heart disease Prediction')
    
    # getting the data from user
    Age = st.text_input('Enter the age between 1 to 100')
    Sex = st.text_input('Enter sex (0 for female, 1 for male)')
    Chest = st.text_input('Enter the Chest pain type')
    BP = st.text_input('Enter the BP value between 1 to 300')
    Cholesterol = st.text_input('Enter your cholesterol value')
    FBS = st.text_input('Enter your FBS value')
    EKG = st.text_input('Enter the EKG value')
    MaxHR = st.text_input('Enter the Max HR ')
    Exerciseagina = st.text_input('Enter the Exercise angina value')
    STdepression = st.text_input('Enter the ST depression value')
    SlopeofST = st.text_input('Enter the Slope of ST value')
    Numberofvesselsfluro = st.text_input('Enter the Number of vessels fluro value')
    Thallium = st.text_input('Enter the Thallium value')
    
    # code for Prediction
    diagnosis = ''
    
    if st.button('Heart disease result'):
        diagnosis = heart_prediction([Age, Sex, Chest, BP, Cholesterol, FBS, EKG, MaxHR, Exerciseagina, STdepression, SlopeofST, Numberofvesselsfluro, Thallium])
        
    st.success(diagnosis)
        
if __name__ == '__main__':
    main()