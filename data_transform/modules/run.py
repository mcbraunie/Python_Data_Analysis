# entry_point.py
import xml.etree.ElementTree as ET
import traceback

from modules.extract import extract_data
from modules.transform import transform_data
from modules.load import load_data
from modules.log import log_progress

# Transformed data
csv_target_file = "transformed_data.csv"

# Make function call to start process
def main():
    '''
    Function presents user with options for
    selection to proceed through processes.
    '''
    print("Choose a function to run:")
    print("S Start")
    print("Q to exit")

    while True:
        try:
            choice = input("Enter your choice (S or Q): ")
            if choice.upper() == "Q":
                print("Quiting program.")
                break
            elif choice.upper() == 'S':
                # function name
                func_name = "Start"
                print(f"You chose the {func_name} function.")
                start_process()
            else:
                print("Invalid choice. Please enter S or Q.")
        except Exception as e:
            print(f"An error was encountered: {e}")
            traceback.print_exc()



def start_process():
    '''
    Function runs if user selects "Start" from main()
    '''
    try:
        print("ETL Job Started.")
        
        # 
        log_progress("Extract process initiated.")
        ed = extract_data()
        log_progress("Extrace process complete.")
        
        # 
        log_progress("Transform process initiated.")
        td = transform_data(ed)
        log_progress("Transform process complete.")

        # 
        log_progress("Load process begun.")
        load_data(td, csv_target_file)
        log_progress("Load process complete.")

    except Exception as e:
        print(f"An error occured: {e}")
        log_progress(f"An error occured: {e}")
        traceback.print_exc()

    finally:
        log_progress("All ETL processes have completed.")
        print("Processes complete.")