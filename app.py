import streamlit as st 
from src.loader import load_csv
from src.validator import (
    missing_values_count, duplicate_values_count,
    count_numeric_outliers
)
from src.scoring import calc_quality_score
from src.cleaner import clean_dataframe


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


        missing_by_column = missing_values_count(data_frame)
        total_missing = int(missing_by_column.sum())

        duplicate_rows = duplicate_values_count(data_frame)

        outliers_by_column = count_numeric_outliers(data_frame)
        total_outliers = sum(outliers_by_column.values())

        quality_score = calc_quality_score(data_frame)



        st.success("CSV file sucessfully uploaded !")

        st.write("Filename:",uploaded_file.name)
        st.write("Number of rows:",data_frame.shape[0])
        st.write("Number of columns:",data_frame.shape[1])

        st.subheader("Data Preview")
        st.dataframe(data_frame.head())

        st.subheader("Data Quality Overview")

        #Metric card to show the an overview of the quality score .
        score_column,missing_column,duplicate_column,outlier_column = st.columns(4)

        score_column.metric(
            label = "Quality Score",
            value = f"{quality_score}/100"
        )

        missing_column.metric(
            label = "Missing Values",
            value = total_missing
        )

        duplicate_column.metric(
            label = "Duplicated Rows",
            value = duplicate_rows
        )

        outlier_column.metric(
            label = "Numeric Outliers ",
            value = total_outliers
        )



        st.subheader("Detailed Quality Report")

        st.write("Missing Value by Column")
        missing_report = [
            {
                "column":column,
                "missing_count":count,
            }
            for column,count in missing_by_column.items()
        ]
        st.dataframe(missing_report)
        

        st.write("Numeric Outliers by Column")

        outlier_report = [
            {
                "column":column,
                "outlier_count":count,
            }
            for column,count in outliers_by_column.items()
        ]
        st.dataframe(outlier_report)


        st.subheader("Clean Dataset")

        if st.button("Clean Data"):
            clean_dataframe = clean_dataframe(data_frame)
            cleaned_quality_score = calc_quality_score(clean_dataframe)

            st.success("Data cleaned successfully!")

            original_column,cleaned_column = st.columns(2)

            original_column.metric(
                "Original Quality Score",
                f"{quality_score}/100",
            )

            cleaned_column.metric(
                "Cleaned Quality Score",
                f"{cleaned_quality_score}/100",
                delta = round(cleaned_quality_score - quality_score,2),
            )
        



    except (ValueError,TypeError) as error:
        st.error(str(error))


