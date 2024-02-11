# function_calls.py


import sqlite3
from processes.log import log
from processes.extract import extract
from processes.transform import transform
from processes.load import load_to_csv, load_to_db, run_query


# URL to pull table data from
url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
# Data for calculating the exchange rate from USD
exchange_rate_filepath = './csv_files/exchange_rate.csv'
# The column headers of the new table
table_attributes = ['Name', 'MC_USD_Billion']
# The name of the db file
db_name = './database_files/Banks.db'
# Name for the table on final output
table_name = 'Largest_banks'
# Connection information
conn = sqlite3.connect(db_name)
# SQL query statements to run on connection to db
query_statements = [
        'SELECT * FROM Largest_banks',
        'SELECT AVG(MC_GBP_Billion) FROM Largest_banks',
        'SELECT Name from Largest_banks LIMIT 5'
    ]
# Filepath to store final .csv
output_csv_path = './csv_files/Largest_banks_data.csv'

def main():
    '''
    Function serves as the entry file to run function calls through ETL process
    '''
    try:
        log('Initiating ETL process')
        log('Extracting data from website')
        # Create dataframe variable to be sent to extract() function
        df = extract(url, table_attributes)
        log('Data extraction complete. Transformation process started...')
        # Using extracted data stored in 'df' send to transform() along with filepath for exchange rate information
        df = transform(df, exchange_rate_filepath)
        log('Data transformation complete. Loading process started...')
        # Using transformed data, send results to csv_load() function
        load_to_csv(df, output_csv_path)
        log('Data saved to CSV file')
        log('SQL Connection initiated')
        # Establish database, connection, and run SQL queries. Return values to db
        load_to_db(df, conn, table_name)
        run_query(query_statements, conn)
        log('Data loaded to Database as table. Running queries...')
        conn.close()
        log('Processes Complete')
    except Exception as e:
        print(f"An error was encountered: {e}")