#Disable warnings
import warnings
warnings.filterwarnings("ignore")

#Libraries for processing data
import pandas as pd
import numpy as np

#Import libraries for graphing
import matplotlib.pyplot as plt
import seaborn as sns

#Libraries for obtaining data from SQL databse
import env
import os

from sklearn.model_selection import train_test_split

#Library needed for scaling the data
import sklearn.preprocessing

def split_data(df):
    '''
    Splits data into train, validate, and test.
    '''
    #split data in train_and_validate_and_test
    train_and_validate, test = train_test_split(df, test_size=.12, random_state=123)
    #split train and validate datasets
    train, validate = train_test_split(train_and_validate, test_size=.12, random_state=123)

    return train, validate, test

def add_scaled_columns(train, validate, test):
    '''
    Scales columns using min-max scaler.
    '''
    columns_to_scale = ['calculatedfinishedsquarefeet', 'bedroomcnt', 'bathroomcnt']
    # new column names
    new_column_names = [c + '_scaled' for c in columns_to_scale]
    
    #Define scaler
    scaler_min_max = sklearn.preprocessing.MinMaxScaler()
    
    # Fit the scaler on the train
    scaler_min_max.fit(train[columns_to_scale])
    
    # transform train validate and test
    train = pd.concat([
        train,
        pd.DataFrame(scaler_min_max.transform(train[columns_to_scale]), columns=new_column_names, index=train.index),
    ], axis=1)
    
    validate = pd.concat([
        validate,
        pd.DataFrame(scaler_min_max.transform(validate[columns_to_scale]), columns=new_column_names, index=validate.index),
    ], axis=1)
    
    
    test = pd.concat([
        test,
        pd.DataFrame(scaler_min_max.transform(test[columns_to_scale]), columns=new_column_names, index=test.index),
    ], axis=1)
    
    return train, validate, test

def clean_data(df):
    '''
    splits and scaled data
    '''
    #split data
    train, validate, test = split_data(df)
    
    #add scaled columns
    train, validate, test = add_scaled_columns(train, validate, test)
    
    return train, validate, test


def get_dict():
    '''
    We will create a pandas DataFrame dictionary of our features.
    '''
    dictionary = {
        'Feature' : [
                    'bedroomcnt',
                    'bathroomcnt',
                    'calculatedfinishedsquarefeet',
                    'taxvaluedollarnct',
                    'yearbuilt',
                    'taxamount',
                    'fips',
                    'calculatedfinishedsquarefeet_scaled',
                    'bedroomcnt_scaled',
                    'bathroomcnt_scaled',
                ],
        'Dataype' : [
                
                    'float64',
                    'float64',
                    'float64',
                    'float64',
                    'float64',
                    'float64',
                    'float64',
                    'float64',
                    'float64',
                    'float64',
                
                ],
        'Definition' : [
                        'Total number of bedrooms in the property',
                        'Total number of bathrooms in the property',
                        'Calculated square feet of the property',
                        'Assessed dollar value of the property',
                        'Year the property was originally built',
                        'Total amount of properties taxes per year in dollars',
                        'FIPS code, indicating the county the property is located in',
                        'Square feet, scaled so that all values are between 0 and 1',
                        'Bedroom count, scaled so that all values are between 0 and 1',
                        'Bathroom count, scaled so that all values are betwween 0 and 1',
                        ],
    }
    return pd.DataFrame(dictionary)

def get_tax_rate():
    '''
    We will create a separate DataFrame for our tax rate.
    '''
    tax_rate = {
        'Feature' : [
            'tax_rate',
            ],
        'Datatype' : [
            'float64',
            ],
        'Definition' : [
            'tax amount divided by the tax value of a home.', 
            ],
    }
    return pd.DataFrame(tax_rate)
    