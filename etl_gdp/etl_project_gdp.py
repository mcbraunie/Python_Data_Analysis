# csv_file = Countries_by_GDP.csv
# table = Countries_by_GDP
# database = World_Economies.db
# db_attributes Country, GDP_USD_billion
# log_file = etl_project_log.txt

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime

url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
table_attributes = ["Country", "GDP_USD_millions"]
db_name = 'World_Economies.db'
table_name = 'Countries_by_GDP'
csv_path = './Countries_by_GDP.csv'


# Functions for project
def extract(url, table_attributes):
    '''
    This function extracts the required
    information from the website and saves it to a dataframe. The
    function returns the dataframe for further processing. 
    '''
    # extract webpage data as text
    page = requests.get(url).text
    # Parse text into HTML objects using bs4 with 'html.parser'
    data = BeautifulSoup(page, 'html.parser')
    # Create empty pandas DataFrame with columns as the table_attributes
    df = pd.DataFrame(columns = table_attributes)
    # Extract all 'tbody' attributes of the HTML object
    tables = data.find_all('tbody')
    # Extract all the rows of index[2] using the 'tr' attribute
    rows = tables[2].find_all('tr')
    # Check th eonctents of each row
    for row in rows:
        # Search within the attribute 'td'
        col = row.find_all('td')
        # Verify that the 'td' element is not empty
        if len(col) != 0:
            # Verify that the data in column index[0] contains a hyperlink
            # Verify that the data in column index[2] is not '-'
            if col[0].find('a') is not None and '—' not in col[2]:
                # Store all elements found in verification within a dictionary with keys the same as the table_attributes
                data_dict = {"Country": col[0].a.contents[0],
                             "GDP_USD_millions": col[2].contents[0]}
                # Append dictionaries 1-by-1 to DataFrame
                df1 = pd.DataFrame(data_dict, index = [0])
                df = pd.concat([df, df1], ignore_index=True)
    return df

def transform(df):
    ''' 
    This function converts the GDP information from Currency
    format to float value, transforms the information of GDP from
    USD (Millions) to USD (Billions) rounding to 2 decimal places.
    The function returns the transformed dataframe.
    '''
    # Create list of df elements
    GDP_list = df["GDP_USD_millions"].tolist()
    # Convert elements in df to float using list comprehension, join() and split()
    GDP_list = [float("".join(x.split(','))) for x in GDP_list]
    # Divide all values by 1000 and round to 2 decimal spaces
    GDP_list = [np.round(x/1000,2) for x in GDP_list]
    # Assign df to list of created values
    df["GDP_USD_millions"] = GDP_list
    # Rename df from millions to billions
    df = df.rename(columns = {"GDP_USD_millions": "GDP_USD_billions"})
    # Return values
    return df


def load_to_csv(df, csv_path):
    '''
    This function saves the final dataframe as a `CSV` file 
    in the provided path. Function returns nothing.
    '''
    # Load df to .csv file destionation
    df.to_csv(csv_path)


def load_to_db(df, sql_connection, table_name):
    '''
    This function saves the final dataframe as a database table
    with the provided name. Function returns nothing.
    '''
    # Load df using to_sql() function 
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)


def run_query(query_statement, sql_connection):
    '''
    This function runs the stated query on the database table and
    prints the output on the terminal. Function returns nothing.
    '''
    # Print the query being run
    print(query_statement)
    # Assign values of pandas read_sql() statement to var query_output
    query_output = pd.read_sql(query_statement, sql_connection)
    # Print out results
    print(query_output)


def log_progress(message):
    '''
    This function logs the mentioned message at a given stage of the code execution to a log file. Function returns nothing
    '''
    # Assign timestamp format to logging results
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year Monthname Day Hour Minute Second
    # Get the current time using now() function to use in the log message
    now = datetime.now()
    # Apply timestamp_format formatting to current time and store as timestamp
    timestamp = now.strftime(timestamp_format)
    # Write log to file
    with open("./etl_project_log.txt", "a") as f:
        f.write(timestamp + ' : ' + message + '\n')

'''
Here, you define the required entities and call the relevant 
functions in the correct order to complete the project. Note that this
portion is not inside any function.
'''
if __name__ == '__main__':

    log_progress('Start ETL process')

    df = extract(url, table_attributes)

    log_progress('Data extraction complete. Beginning Transform process')

    df = transform(df)

    log_progress('Data transformed. Beginning load processes')

    load_to_csv(df, csv_path)

    log_progress('Data saved to csv')

    sql_connection = sqlite3.connect('World_Economies.db')

    log_progress('Established connection to SQL db')

    load_to_db(df, sql_connection, table_name)

    log_progress('Data loaded to Database. Running query...')

    query_statement = f"SELECT * FROM {table_name} WHERE GDP_USD_billions >= 100"

    run_query(query_statement, sql_connection)

    log_progress('All processes have completed.')

    sql_connection.close()