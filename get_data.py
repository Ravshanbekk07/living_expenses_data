import json

def get_data(file_path: str) -> dict:
    """
    get data from json file as dictionary
    
    Args:
        file_path (str): path to json file

    Returns:
        dict: dictionary of data
    """
    f = open(file_path)
    x = f.read()
    jason_data = json.loads(x)
    return type(jason_data)


# test
file_path = "data.json"
data = get_data(file_path)
print(data)
