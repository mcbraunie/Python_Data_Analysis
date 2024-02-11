# main.py

'''
Name: Micah
Date: 02/01/2024
file: main.py
Description: This is the entry-file for the ETL
             program. It calls entry_point.py
             to begin the ETL processes.
'''    
import traceback
import modules.run

if __name__ == "__main__":
    # start program
    try:
        print("Got here one")
        modules.run.main()
        print("Got here two")
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()