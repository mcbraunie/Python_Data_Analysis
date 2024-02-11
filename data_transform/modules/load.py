# load.py


def load_data(transformed_data, target_file):
    '''
    Function takes data from main.py and writes it
    to .csv file.
    '''
    transformed_data.to_csv(target_file) 