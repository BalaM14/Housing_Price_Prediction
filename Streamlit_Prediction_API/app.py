import streamlit as st
import pandas as pd
import pickle
import os
import joblib

from pathlib import Path
st.text(os.getcwd()) 

#latest_model_file_path = "Streamlit_Prediction_API/model.pkl"


#model = pickle.load(open(latest_model_file_path,"rb"))
model = joblib.load('Streamlit_Prediction_API/model.pkl')
print(model)
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Input Features:")
    st.dataframe(data.head())


    data['Predicted_Price'] = model.predict(data)

    st.write("Output Predicted Features:")
    st.dataframe(data.head())

    @st.cache_data
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')


    csv = convert_df(data)

    st.download_button(
    "Press to Download",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv'
    )