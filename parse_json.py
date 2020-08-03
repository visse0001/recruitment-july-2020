import json

JSON_NAME = "persons.json"


def get_not_nested_table_data(json_name: str, index: int, table_name: str):
    json_file = open(json_name, 'r')
    json_data = json_file.read()
    obj = json.loads(json_data)
    obj = obj['results'][index][table_name]
    return obj


def get_double_nested_table_data(json_name: str, index: int, first_table: str, second_table: str):
    json_file = open(json_name, 'r')
    json_data = json_file.read()
    obj = json.loads(json_data)
    obj = obj['results'][index][first_table][second_table]
    return obj


def get_triple_nested_table_data(json_name: str, index: int, first_table: str, second_table: str, third_table: str):
    json_file = open(json_name, 'r')
    json_data = json_file.read()
    obj = json.loads(json_data)
    obj = obj['results'][index][first_table][second_table][third_table]
    return obj
