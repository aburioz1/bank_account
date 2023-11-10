import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import sklearn
import pickle

Financial_inclusion_model = pickle.load(open("Financial_inclusion_model.pkl", "rb"))
st.title("Bank Account Prediction App")
image = Image.open('pexels-karolina-grabowska-4386158.jpg')
st.image(image, width= 400)
def user_report():
    year = st.number_input('year: ',min_value=0)
    status = st.selectbox("location_type: ", ['Rural', 'Urban'])
    if (status == 'Rural'):
        location_type = 0
    else:
        location_type = 1
    status = st.selectbox("cellphone_access: ", ['Yes', 'No'])
    if (status == 'Yes'):
        cellphone_access = 1
    else:
        cellphone_access = 0
    age_of_respondent = st.number_input('age_of_respondent: ', min_value=0)
    status = st.selectbox("gender_of_respondent: ", ['Female', 'Male'])
    if (status == 'Female'):
        gender_of_respondent = 0
    else:
        gender_of_respondent = 1
    status = st.selectbox("education_level: ", ['No formal education','Other/Dont know/RTA','Primary education','Secondary education', 'Tertiary education','Vocational/Specialised training'])
    if (status == 'No formal education'):
        education_level = 0
    elif (status == 'Other/Dont know/RTA'):
        education_level = 1
    elif (status == 'Primary education'):
        education_level = 2
    elif (status == 'Secondary education'):
        education_level = 3
    elif (status == 'Tertiary education'):
        education_level = 4
    else:
        education_level = 5
    data_report = {
        'year': year,
        'location_type': location_type,
        'cellphone_access': cellphone_access,
        'age_of_respondent': age_of_respondent,
        'gender_of_respondent': gender_of_respondent,
        'education_level': education_level
    }
    data = pd.DataFrame(data_report, index=[0])
    return data
user_data = user_report()
st.write(user_data)
prediction = Financial_inclusion_model.predict(user_data)
st.success(prediction)
