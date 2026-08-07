import streamlit as st 
from src.loader import load_csv
from src.validator import (
    missing_values_count, duplicate_values_count,
    count_numeric_outliers
)
from src.scoring import calc_quality_score


# Configuring brower tab for streamlit app

st.set_page_config(
    page_title = "CSV Data quality Analyzer",
    page_icon = "📊",
    layout = "wide",
    )

st.title("CSV Data Quality Analyzer ")
st.write("Upload a CSV to check data issues and generate a cleaned version")


uploaded_file = st.file_uploader("Upload a CSV file",type=["csv"],)

if uploaded_file is not None:
    try:
        data_frame = load_csv(uploaded_file)
        st.success("CSV file sucessfully uploaded !")

        st.write("Filename:",uploaded_file.name)
        st.write("Number of rows:",data_frame.shape[0])
        st.write("Number of columns:",data_frame.shape[1])

        st.subheader("Data Preview")
        st.dataframe(data_frame.head())
    except (ValueError,TypeError) as error:
        st.error(str(error))

        
