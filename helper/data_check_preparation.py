import numpy as np
import pandas as pd

def read_data(PATH, ENCODING_TYPE):
    '''
    Read data from dataset from path with encoding type
    
    Parameters
    ----------
    PATH : str
        path source of cleaning data, csv.
        
    ENCODING_TYPE : str
        encoding type
    
    Returns
    -------
    data : pd.DataFrame
        Data to cleaning
    '''
    data = pd.read_csv(PATH, encoding=ENCODING_TYPE)
    
    return data

def read_and_check_data(path, encoding_type):
    '''
    Read data
    '''
    print('Start import data')
    df = read_data(path, encoding_type)
    print('Done import data')
    
    return df