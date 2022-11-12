import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename) -> list[dict]:
    ...  # TODO реализовать конвертер из csv в json
    list_ = []
    with open(filename) as input_f:
        for line in input_f:
            line = line.strip().split(',')
            list_.append(line)

    js_list = []
    dict_ = {}

    for j in range(1, len(list_)):
        for i in range(len(list_[0])):
            dict_[list_[0][i]] = list_[j][i]
        js_list.append(dict_)
        dict_ = {}

    return js_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

