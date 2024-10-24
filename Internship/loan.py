# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:18:55 2024

@author: HP
"""

import pickle
import streamlit as st
import numpy as np  # Ensure numpy is imported

# Load the model
load_model = pickle.load(open('Internship.sav','rb'))

def loan_prediction(input_data):
    # Convert input data to numpy array and reshape
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    
    # Make prediction
    prediction = load_model.predict(input_data_reshaped)
    
    # Return the prediction result
    if prediction[0] == ' Rejected':
        return "Your approval is rejected"
    elif prediction[0] == ' Approved':
        return "Your approval is accepted"

def main():
    # Giving a title
    st.title("Hypnosis's Prediction")
    
      
    
    # Getting the input data from the user
    no_of_dependents = st.text_input("Enter the no. of dependents")
    education = st.text_input("Enter your education")
    self_employed = st.text_input("Enter your employment status")
    income_annum = st.text_input("Enter your income per annum")
    loan_amount = st.text_input("Enter your loan amount")
    loan_term = st.text_input("Enter your loan term")
    cibil_score = st.text_input("Enter your cibil score")
    residential_assets_value = st.text_input("Enter your residential assets value")
    commercial_assets_value = st.text_input("Enter your commercial assets value")
    luxury_assets_value = st.text_input("Enter your luxury assets value")
    bank_asset_value = st.text_input("Enter your bank asset value")
    
    # Code for prediction
    sanctioned = " "
    
    # Creating a button
    if st.button("Press for result :>"):
        sanctioned = loan_prediction([no_of_dependents, education, self_employed, income_annum, loan_amount, loan_term, cibil_score, residential_assets_value, commercial_assets_value, luxury_assets_value, bank_asset_value])
        
    st.success(sanctioned)

if __name__ == "__main__":
    main()
