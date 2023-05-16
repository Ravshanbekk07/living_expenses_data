import json

def most_expensive(file_path: str) -> str:
    """
    get most expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: most expensive item
    """
    f = open(file_path)
    x = f.read()
    jason_data = json.loads(x)
    
    re =  list(jason_data.items())
    min = re[0]
    for i in re:
        if min[1]<i[1]:
            min = i

    return min[0]


# test
file_path = "data.json"
most_expensive_item = most_expensive(file_path)
print(most_expensive_item)