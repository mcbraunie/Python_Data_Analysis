#  log.py
from datetime import datetime
from pathlib import Path

# get current directory for filepath
current_directory = str(Path.cwd())
log_file = "/log_file.txt"
log_fp = current_directory + log_file

def log_progress(message):
    '''
    Function logs process that is run and the date and time
    the function ran.
    '''
    try:
        # Formatting for date and time
        timestamp_format = '%Y-%h-%d-%H:%M:%S'
        # Get current date and time
        now = datetime.now()
        # Combines formatting with current date and time
        timestamp = now.strftime(timestamp_format)
        # Write log to log_file with message
        with open(log_fp, "a+") as f:
            f.write(timestamp + ',' + message + '\n')

    except Exception as e:
        print(f"An error occured: {e}")