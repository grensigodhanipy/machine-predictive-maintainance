import streamlit as st
import joblib
import numpy as np
model=joblib.load('gb_classifier.pkl')
def predict(df):
    prediction=model.predict(df)
    return prediction
st.title('machine predictive maiteinance')
air=st.number_input('Enter Air temperature [K]: ')
pro=st.number_input('Enter Process temperature [K]: ')
ro=st.number_input('Enter Rotational speed [rpm]: ')
tr=st.number_input('Enter Torque [Nm]: ')
tw=st.number_input('Enter Tool wear [min]: ')
arr=np.array([[air,pro,ro,tr,tw]])
if st.button('predict'):
    result=predict(arr)
    st.success(f'Prediction:{result}')
       
