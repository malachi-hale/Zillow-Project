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

#Library for dealing with NA values
from sklearn.impute import SimpleImputer

#First we establish a connection to the SQL server
def get_connection(db, user=env.user, host=env.host, password=env.password):
    '''
     We establish a connection to the SQL database, using my information stored in the env file.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

#Now we will make our DataFrame with the relevant Zillow data
def get_zillow_data():
    '''
    We will read a SQL query and create a file based on this query. I have also included a line to eliminate duplicate columns because value_counts() does not work if there are duplicate columns in the DataFrame.
    '''
    filename = "zillow.csv"
    ##We will write a SQL query to obtain the data
    sql = ''' 
    SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet,
         taxvaluedollarcnt, yearbuilt, taxamount, fips from properties_2017
    JOIN propertylandusetype
    ON propertylandusetype.propertylandusetypeid = properties_2017.propertylandusetypeid
    AND (propertylandusetype.propertylandusetypeid = 261 
    OR propertylandusetype.propertylandusetypeid = 262 
    OR propertylandusetype.propertylandusetypeid = 263
    OR propertylandusetype.propertylandusetypeid = 264
    OR propertylandusetype.propertylandusetypeid = 265
    OR propertylandusetype.propertylandusetypeid = 266
    OR propertylandusetype.propertylandusetypeid = 268
    OR propertylandusetype.propertylandusetypeid = 273
    OR propertylandusetype.propertylandusetypeid = 275
    OR propertylandusetype.propertylandusetypeid = 276
    OR propertylandusetype.propertylandusetypeid = 279)
    JOIN predictions_2017
    ON predictions_2017.parcelid = properties_2017.parcelid 
    AND predictions_2017.transactiondate BETWEEN '2017-05-01' AND '2017-08-31'
    '''
    df = pd.read_sql(sql, get_connection('zillow'))
    return df


#Now we will replace the null values with the mean value of each column
def impute_null_values(df):
    '''
    We will use SimpleImputer to impute the mean value into the null values into each column.
    '''
    #We will use the mean imputer function.
    imputer = SimpleImputer(strategy='mean')

    #We will create a for loop that will impute all the null values in each one of our columns.
    for col in df.columns:
        df[[col]] = imputer.fit_transform(df[[col]])
    
    return df

#This function removes extreme outliers from our DataFrame
def remove_outliers(df, k, col_list):
    ''' remove outliers from a list of columns in a dataframe 
        and return that dataframe
    '''
    
    for col in col_list:

        q1, q3 = df[col].quantile([.25, .75])  # get quartiles
        
        iqr = q3 - q1   # calculate interquartile range
        
        upper_bound = q3 + k * iqr   # get upper bound
        lower_bound = q1 - k * iqr   # get lower bound

        # return dataframe without outliers
        
        df = df[(df[col] > lower_bound) & (df[col] < upper_bound)]
        
    return df

def wrangle_zillow():
    '''
    We will call the other functions from the file in our wrangle_zillow function.
    '''
    #Acquire data
    df = get_zillow_data()

    #Clean data
    df = impute_null_values(df)

    #Remove outliers
    df = remove_outliers(df, 3, df.columns)

    #Return final DataFrame
    return df

