import json

def least_expensive(file_path: str) -> str:
    """
    get least expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: least expensive item
    """
    f = open(file_path)
    x = f.read()
    jason_data = json.loads(x)
    
    re =  list(jason_data.items())
    min = re[0]
    for i in re:
        if min[1]>i[1]:
            min = i

    return min[0]

# test
file_path = "data.json"
least_expensive_item = least_expensive(file_path)
print(least_expensive_item)
