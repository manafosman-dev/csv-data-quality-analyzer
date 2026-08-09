import pandas as pd 


def remove_duplicate(dataframe):
    """ copy of dataframe with duplicates removed """
    cleaned_dataframe = dataframe.copy()
    cleaned_dataframe = dataframe.drop_duplicates()

    return cleaned_dataframe 


def missing_numeric_values(dataframe):
    """ return a copy of dataframe with missing values using median on numeric column"""
    cleaned_dataframe = dataframe.copy()
    numeric_columns = cleaned_dataframe.select_dtypes(include="number").columns

    for column in numeric_columns:
        median_value  = cleaned_dataframe[column].median()

        if not pd.isna(median_value):
            cleaned_dataframe[column] = (cleaned_dataframe[column].fillna(median_value))

    return cleaned_dataframe    


def missing_text_values(dataframe):
    """ return a copy of cleaned dataframe from df with  missing text values """
    cleaned_dataframe = dataframe.copy()
    text_columns = dataframe.select_dtypes(include=["object","string"]).columns

    for column in text_columns:
        mode_values = cleaned_dataframe[column].mode()

        if not mode_values.empty:
            most_freq_value = mode_values.iloc[0]
            cleaned_dataframe[column] = (cleaned_dataframe[column].fillna(most_freq_value))

    return cleaned_dataframe   


def columns_standardization(dataframe):
    """ return a standardize column naming """
    cleaned_dataframe = dataframe.copy()

    cleaned_dataframe.columns = (
        cleaned_dataframe.columns
        .str.strip()
        .str.lower()
        .str.replace(" ","_",regex=False)
        .str.replace("-","_",regex=False)
    )
    return cleaned_dataframe


def clean_dataframe(dataframe):
    """ clean dataframe in sequencial order"""
    clean_dataframe = missing_numeric_values(dataframe)
    clean_dataframe = missing_text_values(clean_dataframe)
    clean_dataframe = columns_standardization(clean_dataframe)
    clean_dataframe = remove_duplicate(clean_dataframe)

    return clean_dataframe