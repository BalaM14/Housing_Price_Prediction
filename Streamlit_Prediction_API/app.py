import streamlit as st
import pandas as pd
import pickle
import os


def get_latest_model_path(model_dir):
        folder_name = list(map(int, os.listdir(model_dir)))
        latest_model_dir = os.path.join(model_dir, f"{max(folder_name)}")
        file_name = os.listdir(latest_model_dir)[0]
        latest_model_path = os.path.join(latest_model_dir, file_name)
        return latest_model_path



latest_model_file_path = get_latest_model_path("..\saved_models")


model = pickle.load(open(latest_model_file_path,"rb"))
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