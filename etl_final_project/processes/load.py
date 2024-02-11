# load.py


import pandas as pd


def load_to_csv(df, output_path):
    '''
    Function takes dataframe and saves in csv format to specified filepath
    '''
    df.to_csv(output_path)


def load_to_db(df, sql_connection, table_name):
    '''
    Creates/Replaces database connection using established connection and table details
    '''
    df.to_sql(table_name, sql_connection, if_exists = 'replace', index = False)

def run_query(query_statements, conn):
    '''
    Prints and runs SQL queries against database
    '''
    for query in query_statements:
        print(query)
        print(pd.read_sql(query, conn), '\n')