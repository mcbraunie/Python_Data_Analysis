# extract.py

import requests
from bs4 import BeautifulSoup
import pandas as pd


def extract(url, table_attributes):
    # Get website url content assign to variable page using requests.get()
    page = requests.get(url).text
    # Create empty dataframe df with columns = to table_attributes
    df = pd.DataFrame(columns = table_attributes)
    # Parse data from page with 'html.parser' and assign to data
    data = BeautifulSoup(page, 'html.parser')
    # Using parsed data from bs4, create variable 'tables' that stores all <tbody> element(s) from the first encountered table
    tables = data.find_all('tbody')[0]
    # Create variable 'rows' to store all <tr> elements within tables variable
    rows = tables.find_all('tr')
    # Create loop to search through values stores in 'rows'
    for row in rows:
        # Create var 'col' to find all <td> elements within 'rows'
        col = row.find_all('td')
        # Check if value is not empty
        if len(col) != 0:
            # Create variable 'a_tag' to store first value in table (ignores headers by starting at cell[1]) that containes <a> tag
            a_tag = col[1].find_all('a')[1]
            # Loop over 'a_tag' elements, and if it is not empty, do something
            if a_tag is not None:
                # Create dictionary using data from table (used for df, this creates 1 row of 2 columns 'Name' 'MC_USD_Billio')
                data_dict = {'Name': a_tag.contents[0],
                             'MC_USD_Billion': col[2].contents[0]}
                # Create dataframe and add dictionary items
                df1 = pd.DataFrame(data_dict, index = [0])
                # Assign df1 to created df, appending the values to the table
                df = pd.concat([df, df1], ignore_index = True)
    # Return the created df to caller
    return df