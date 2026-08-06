from src.validator import (missing_values_count,
duplicate_values_count,count_numeric_outliers)


def calc_quality_score(dataframe):
    """ Calculating data quality score from 0 to 100 """
    total_cells = dataframe.shape[0] * dataframe.shape[1]
    if total_cells == 0:
        raise ValueError("quality score cannot be calculated with an empty Dataframe")

    missing_values = missing_values_count(dataframe)
    total_missing = int(missing_values.sum())

    missing_rate = total_missing / total_cells
    completeness_score = (1 - missing_rate) * 50 

    total_rows = dataframe.shape[0]
    duplicate_rows = duplicate_values_count(dataframe)

    duplicate_rate = duplicate_rows / total_rows
    uniqueness_score = (1- duplicate_rate) * 30

    outliers_column = count_numeric_outliers(dataframe)
    total_outliers = sum(outliers_column.values())

    numeric_df = dataframe.select_dtypes(include="number")
    total_numeric_values = int(numeric_df.count().sum())

    if total_numeric_values == 0:
        validity_score = 20
    else:
        outlier_rate = total_outliers / total_numeric_values
        validity_score = (1 - outlier_rate) * 20    

    total_score = completeness_score + uniqueness_score + validity_score

    return round(total_score,2)    