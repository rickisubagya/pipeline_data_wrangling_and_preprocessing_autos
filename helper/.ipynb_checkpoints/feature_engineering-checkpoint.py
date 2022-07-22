import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import normalize
from helper.constant import NEW_COLUMN_NAME


def feature_engineering(df):
    # Rename column name based on dictionary in contant file assign to variable cars_data
    cars_data = df.rename(columns=NEW_COLUMN_NAME)
    
    # Change value type from some columns to datetime format
    cars_data[['ad_created', 'date_crawled', 'last_seen']] = cars_data[['ad_created', 'date_crawled', 'last_seen']].apply(pd.to_datetime)
    
    # Change value type to integer format
    cars_data['price'] = cars_data['price'].str.replace('\D+', '', regex=True).astype(int)
    cars_data['odometer'] = cars_data['odometer'].str.replace('\D+', '', regex=True).astype(int)
    
    # Drop column seller and offer_type
    cars_data = cars_data.drop(columns=['seller', 'offer_type'])
    
    # Drop column num_of_pictures and assign to variable called cars_data
    cars_data = cars_data.drop(columns=['num_of_pictures'])
    
    # Drop column name and postal_code and assign to variable called cars_data
    cars_data = cars_data.drop(columns=['name', 'postal_code'])
    
    # Filter data has price value more than equal to 500 and below than equal to 40,000
    cars_data = cars_data[(cars_data['price'] >= 500) & (cars_data['price'] <= 40000)]
    
    # Fill missing value with mode if column type = object, with median if column type = number
    for col in cars_data.columns:
        if cars_data[col].dtypes == 'object':
            mode_per_column = cars_data[col].mode()[0]
            cars_data[col] = cars_data[col].fillna(mode_per_column)
        elif cars_data[col].dtypes == 'int' or cars_data[col].dtypes == 'float':
            median_per_column = cars_data[col].median()
            cars_data[col] = cars_data[col].fillna(median_per_column)
    
    # Reset index and assign to variable called df_transformed
    cars_transformed = cars_data.copy()
    cars_transformed = cars_transformed.reset_index(drop=True)
    
    # Perform the normalization process for columns with numeric data type, except the price column
    cars_transformed[cars_transformed.select_dtypes('number').drop('price', axis=1).columns] = pd.DataFrame(normalize(X=cars_transformed.select_dtypes('number').drop('price', axis=1), norm='l2', axis=1), columns=cars_transformed.select_dtypes('number').drop('price', axis=1).columns)
    
    # Perform the encoding process for columns of categorical data type using get dummies
    cars_transformed = pd.get_dummies(cars_transformed, columns=cars_transformed.select_dtypes('object').columns)
    cars_transformed

    return cars_transformed