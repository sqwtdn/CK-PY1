import json

INPUT_FILE = "input_task4.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    with open(filename) as inp:
        pizza = []
        for ind, l in enumerate(inp):
            filling = l.strip(new_line).split(delimiter)
            if ind == 0:
                crust = filling
                continue

            pizza.append({})

            for i, _ in enumerate(crust):
                pizza[-1][crust[i]] = filling[i]
    return pizza


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
