# extract.py
import warnings
import glob
import pandas as pd
import xml.etree.ElementTree as ET


# suppress Pandas warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


def extract_from_csv(file_to_process):
    '''
    Function extracts data from .csv files found
    in folder.
    '''
    dataframe = pd.read_csv(file_to_process)
    return dataframe


def extract_from_json(file_to_process):
    '''
    Function extracts data from .json files found
    in folder.
    '''
    dataframe = pd.read_json(file_to_process, lines=True)
    return dataframe


def extract_from_xml(file_to_process):
    '''
    Function extracts data from .xml files found
    in folder.
    '''
    try:
        dataframe = pd.DataFrame(columns=["name", "height", "weight"])
        tree = ET.parse(file_to_process)
        root = tree.getroot()
        for person in root:
            name = person.find("name").text
            height = float(person.find("height").text)
            weight = float(person.find("weight").text)
            dataframe = pd.concat([dataframe, pd.DataFrame([{"name":name, "height":height, "weight":weight}])], ignore_index=True)
    except Exception as e:
        print(f"An error was encountered: {e}")
    return dataframe


def extract_data():
    '''
    Entry function for respective (.csv, .json, .xml)
    data files in folder.
    '''
    try:
        # Empty dataframe to hold extracted data
        extracted_data = pd.DataFrame(columns=['name', 'height', 'weight'])

        # search files in folder which match .csv, process with csv function
        for csvfile in glob.glob("raw_data/*.csv"):
            extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True)
        #
        for jsonfile in glob.glob("raw_data/*.json"):
            extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True)
        #
        for xmlfile in glob.glob( "raw_data/*.xml"):
            extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True)
    except Exception as e:
        print(f"An error occured: {e}")
    return extracted_data