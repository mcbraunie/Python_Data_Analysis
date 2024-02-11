# transform.py
import pandas as pd
import numpy as np


def transform(df, exchange_rate_path):
    '''
    Function formats data from df to be able to perform calculations.
    Performs currency exchange calculations using exchange rate file.
    '''
    # Create list of data elements from df column 'MC_USD_Billion'
    format_currency = list(df['MC_USD_Billion'])
    # Apply float data type to each element in the list, remove newlines
    format_currency = [float(''.join(x.split('\n'))) for x in format_currency]
    # Append the new changes as the new values to df
    df['MC_USD_Billion'] = format_currency
    # Read-in exchange rate data, save to new dataframe: 'csv_file'
    csv_file = pd.read_csv(exchange_rate_path)
    # Converts the dataframe to a dictionary, where index is the 'Currency' df element, and value is the 'Rate' element
    dict = csv_file.set_index('Currency').to_dict()['Rate']
    # Create dataframes columns for each currency, apply exchange rate calculations for each currency and round to 2 decimals
    df['MC_GBP_Billion'] = [np.round(x * dict['GBP'],2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x * dict['INR'],2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x * dict['EUR'],2) for x in df['MC_USD_Billion']]
    # Return dataframe to caller
    return df