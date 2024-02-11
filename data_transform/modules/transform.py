# transform.py


def transform_data(data):
    '''
    '''
    try:
        # Convert inches to meters and round off to 2 decimal spaces
        data['height'] = round(data.height * 0.0254, 2)
        
        # Convert pounds to kg and round off to 2 decimal spaces
        data['weight'] = round(data.weight * 0.45359237, 2)
    except Exception as e:
        print(f"An error occured: {e}")
    return data

