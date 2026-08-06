import pandas as pd 

def get_column_data_types(dataframe):
    """ Getting the data types of each column  """
    column_data_type = dataframe.dtypes.astype(str)
    return column_data_type


def get_unique_values(dataframe):
    """ count unique values from CSV file """
    count_unique = dataframe.nunique()
    return count_unique