from pathlib import path 
import pandas as pd 


def load_csv(file):
    """ function to confirm if a file was uploaded """
    if file is None:
        raise ValueError("No file was uploaded!")

    file_name = getattr(file,"name",str(file))

    if path(file_name).suffix.lower()!= ".csv":
        raise ValueError("A csv file has to be uploaded")

    try:
        dataframe = pd.read_csv(file)
    except pd.errors.EmptyDataError:
        raise ValueError("The CSV file is empty") from None 
    except pd.errors.ParserError:
        raise ValueError("The CSV file could'nt be parsed") from None
    except UnicodeDecodeError:
        raise ValueError("The CSV file has an unsupported text encoding") from None 
    
    if dataframe.empty:
        raise ValueError("The CSV file is empty")
    return dataframe