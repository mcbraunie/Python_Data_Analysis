# log.py
from datetime import datetime

# Filepath to store logs
logfile = './logs/code_log.txt'

def log(log_msg):
    timeformat = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timeformat)

    with open(logfile, 'a') as f:
        f.write(timestamp + ' : ' +log_msg + '\n')