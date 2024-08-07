import numpy as np
import pickle
import pandas as pd
import streamlit as st 

"""
### Created By : Bala Murugan
#### LinkedIn : https://www.linkedin.com/in/balamurugan14/

# House Price Prediction
"""

pickle_in = open("Streamlit_Prediction_API/model.pkl","rb")
regressor=pickle.load(pickle_in)


def main():
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit House Price Predictor ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    longitude = st.text_input("longitude","")
    latitude = st.text_input("latitude","")
    housing_median_age = st.text_input("housing_median_age","")
    total_rooms = st.text_input("total_rooms","")
    total_bedrooms = st.text_input("total_bedrooms","")
    population = st.text_input("population","")
    households = st.text_input("households","")
    median_income = st.text_input("median_income","")
    ocean_proximity = st.selectbox("ocean_proximity",("<1H OCEAN","INLAND","ISLAND","NEAR BAY","NEAR OCEAN"))
    result=""

    input_data = {"longitude": [longitude], "latitude": [latitude], "housing_median_age": [housing_median_age],
                  "total_rooms": [total_rooms], "total_bedrooms": [total_bedrooms], "population":[population],
                  "households": [households], "median_income":[median_income], "ocean_proximity": [ocean_proximity]}
    
    dataframe = pd.DataFrame(input_data)

    if st.button("Predict"):
        result=regressor.predict(dataframe)
    st.success('The output is {}'.format(result))

    st.write("")
    st.write(f"{'=='*17}   BATCH PREDICTION   {'=='*18}")
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("Input Features: limited to 5 rows")
        st.dataframe(data.head())

        if st.button("Run"):
            data['Predicted_Price'] = regressor.predict(data)
            st.write("Output Predicted Features: limited to 5 rows")
            st.dataframe(data.head())

            @st.cache_data
            def convert_df(df):
                return df.to_csv(index=False).encode('utf-8')


            csv = convert_df(data)

            st.download_button(
            "Download Predicted Output File",
            csv,
            "file.csv",
            "text/csv",
            key='download-csv'
            )

if __name__=='__main__':
    main()