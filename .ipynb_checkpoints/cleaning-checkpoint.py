import pandas as pd

from helper.data_check_preparation import read_and_check_data
from helper.feature_engineering import feature_engineering
from helper.constant import PATH, ENCODING_TYPE, NEW_COLUMN_NAME

def clean_data():
    # read and check data
    df = read_and_check_data(PATH, ENCODING_TYPE)
    
    # feature engineering
    print('Start claning data')
    cars_transformed = feature_engineering(df)
    print('Done cleaning data\nStart saving result cleaning data')
    cars_transformed.to_csv('artifacts/cars_transformed.csv', index=False)
    
if __name__=="__main__":
    print('START RUNNING PIPELINE!')
    clean_data()
    print('FINISH RUNNING PIPELINE!')