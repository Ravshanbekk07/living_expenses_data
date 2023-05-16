import json

def total_expenses(file_path: str) -> float:
    """
    get total expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: total expenses
    """
    f = open(file_path)
    x = f.read()
    jason_data = json.loads(x)
    c = list(jason_data.values())
    #print(len(c))
    u = 0
    for i in c:
        u+=i
    return u


# test
file_path = "data.json"
total = total_expenses(file_path)
print(total)
