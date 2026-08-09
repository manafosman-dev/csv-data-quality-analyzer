import pandas as pd 
from src.cleaner import (
    remove_duplicate,missing_numeric_values,
    missing_text_values,clean_dataframe,columns_standardization
)

def test_remove_duplicate():
    dataframe = pd.DataFrame(
        {
            "name": ["Ama", "Kojo", "Ama"],
            "age": [25, 30, 25],
        }
    )

    cleaned_dataframe = remove_duplicate(dataframe)

    assert len(cleaned_dataframe) == 2
    assert cleaned_dataframe.duplicated().sum() == 0

    # Original DataFrame remains unchanged.
    assert len(dataframe) == 3


def test_fill_numeric_missing_values():
    dataframe = pd.DataFrame(
        {
            "age": [20, None, 40],
            "salary": [1000, 2000, None],
            "name": ["Ama", "Kojo", "Yaw"],
        }
    )

    cleaned_dataframe = missing_numeric_values(dataframe)

    assert cleaned_dataframe["age"].isna().sum() == 0
    assert cleaned_dataframe["salary"].isna().sum() == 0

    # Missing values should be replaced with each column's median.
    assert cleaned_dataframe.loc[1, "age"] == 30
    assert cleaned_dataframe.loc[2, "salary"] == 1500

    # Original DataFrame remains unchanged.
    assert dataframe["age"].isna().sum() == 1
    assert dataframe["salary"].isna().sum() == 1


def test_fill_text_missing_values():
    dataframe = pd.DataFrame(
        {
            "department": ["Sales", None, "Sales"],
            "city": ["Accra", "Kumasi", None],
        }
    )

    cleaned_dataframe = missing_text_values(dataframe)

    assert cleaned_dataframe.isna().sum().sum() == 0
    assert cleaned_dataframe.loc[1, "department"] == "Sales"
    assert cleaned_dataframe.loc[2, "city"] == "Accra"

    # Original DataFrame remains unchanged.
    assert dataframe.isna().sum().sum() == 2


def test_fill_text_all_missing_column():
    dataframe = pd.DataFrame(
        {
            "name": pd.Series([None, None], dtype="object"),
            "city": ["Accra", "Kumasi"],
        }
    )

    cleaned_dataframe = missing_text_values(dataframe)

    # A completely empty text column has no mode, so it remains missing.
    assert cleaned_dataframe["name"].isna().sum() == 2
    assert cleaned_dataframe["city"].isna().sum() == 0


def test_columns_standardization():
    dataframe = pd.DataFrame(
        {
            " Customer Name ": ["Ama"],
            "Department-Name": ["Sales"],
            "AGE": [25],
        }
    )

    cleaned_dataframe = columns_standardization(dataframe)

    assert cleaned_dataframe.columns.tolist() == [
        "customer_name",
        "department_name",
        "age",
    ]

    # Original column names remain unchanged.
    assert dataframe.columns.tolist() == [
        " Customer Name ",
        "Department-Name",
        "AGE",
    ]


def test_clean_dataframe_complete_pipeline():
    dataframe = pd.DataFrame(
        {
            " Customer Name ": ["Ama", "Kojo", "Ama"],
            "Age": [25, None, 25],
            "Department-Name": ["Sales", None, "Sales"],
        }
    )

    cleaned_dataframe = clean_dataframe(dataframe)

    assert cleaned_dataframe.isna().sum().sum() == 0
    assert cleaned_dataframe.duplicated().sum() == 0
    assert len(cleaned_dataframe) == 2

    assert cleaned_dataframe.columns.tolist() == [
        "customer_name",
        "age",
        "department_name",
    ]

    # Original DataFrame remains unchanged.
    assert dataframe.isna().sum().sum() == 2
    assert len(dataframe) == 3
    assert dataframe.columns.tolist() == [
        " Customer Name ",
        "Age",
        "Department-Name",
    ]