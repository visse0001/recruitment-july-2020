import json

JSON_NAME = "persons.json"


def get_not_nested_column_data(json_name, column_name):
    column_name = str(column_name)
    json_file = open(json_name, 'r')
    json_data = json_file.read()
    obj = json.loads(json_data)
    obj = obj['results'][0][column_name]
    return obj
