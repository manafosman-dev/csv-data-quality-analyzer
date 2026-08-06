import pandas as pd 


def missing_values_count(dataframe):
    """ function to count missing values in uploaded CSV"""
    missing_count = dataframe.isnull().sum()
    return missing_count 


def duplicate_values_count(dataframe):
    """ Count of duplicate values in an uploaded CSV file """
    duplicated_values = dataframe.duplicated().sum()
    return duplicated_values


def count_numeric_outliers(dataframe):
    """ Count numeric outliers """
    numeric_columns = dataframe.select_dtypes(include="number")
    outlier_counts = {}

    for column in numeric_columns:
        q1 = numeric_columns[column].quantile(0.25)
        q3 = numeric_columns[column].quantile(0.75)
        iqr = q3 - q1

        lower_bound = q1 - (1.5 * iqr)
        upper_bound = q3 + (1.5 * iqr)
        outliers = ((numeric_columns[column] < lower_bound) |
                     (numeric_columns[column] > upper_bound))   

        outlier_counts[column] = int(outliers.sum())
    return outlier_counts    