import json

JSON_NAME = "persons.json"


def get_not_nested_column_data(json_name, column_name):
    column_name = str(column_name)
    json_file = open(json_name, 'r')
    json_data = json_file.read()
    obj = json.loads(json_data)
    obj = obj['results'][0][column_name]
    return obj


def get_title_nested_column_data(json_name):
    json_file = open(json_name, 'r')
    json_data = json_file.read()
    obj = json.loads(json_data)
    obj = obj['results'][0]['name']['title']
    return obj


def get_street_name_or_number(json_name, column_name):
    column_name = str(column_name)
    json_file = open(json_name, 'r')
    json_data = json_file.read()
    obj = json.loads(json_data)
    obj = obj['results'][0]['location']['street'][column_name]
    return obj
