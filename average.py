import json

def average_expenses(file_path: str) -> float:
    """
    get average expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: average expenses
    """
    f = open(file_path)
    x = f.read()
    jason_data = json.loads(x)
    c = list(jason_data.values())
    #print(len(c))
    u = 0
    for i in c:
        u+=i
    return u/len(c)




# test
file_path = "data.json"
average = average_expenses(file_path)
print(average)
