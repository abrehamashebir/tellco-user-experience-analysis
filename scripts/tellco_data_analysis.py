
import pandas as pd
import numpy as np


def fill_data_by_mean(data):
    data.fillna(data.mean(numeric_only =True), inplace = True)

    return data

def drop_duplicate_data(data):
    data =data.drop_duplicates()
    

def format_data(data):

    data = data.rename(columns={
        'Start':'Start Date',
        'End':'End Date'
    })

    if 'date_column' in data.columns:
        data['date_column'] = pd.to_datetime(data['date_column'], errors='coerce')

    return data

def treat_outlier_with_mean(data, column):
    
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR =Q3-Q1
    lower_bound = Q1- 1.5*IQR 
    upper_bound = Q3 + 1.5*IQR

    data = data[(data[column] > lower_bound) | (data[column]) < upper_bound]
    # data.drop(data[(data[column] < lower_bound) | (data[column] > upper_bound)].index, inplace=True)
    
    return data

    return data