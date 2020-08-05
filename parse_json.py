import json
from datetime import datetime

JSON_NAME = "persons.json"


def get_json_dict():
    json_file = open(JSON_NAME, 'r')
    json_data = json_file.read()
    obj = json.loads(json_data)
    return obj


def get_not_nested_table_data(index: int, table_name: str):
    result = get_json_dict()
    obj = result['results'][index][table_name]
    return obj


def get_double_nested_table_data(index: int, first_table: str, second_table: str):
    result = get_json_dict()
    obj = result['results'][index][first_table][second_table]
    return obj


def get_triple_nested_table_data(index: int, first_table: str, second_table: str, third_table: str):
    result = get_json_dict()
    obj = result['results'][index][first_table][second_table][third_table]
    return obj


def remove_special_characters_from_string(a_string: str):
    alpha_numeric = ""
    for character in a_string:
        if character.isalnum():
            alpha_numeric += character
    return alpha_numeric


def get_days_until_birthday(index: int, first_table: str, second_table: str):
    now = datetime.now()
    year = now.year
    birthday_str = get_double_nested_table_data(index, first_table, second_table)
    birthday_str = str(year) + birthday_str[4:]
    birthday = datetime.strptime(birthday_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    now = datetime.now()
    delta = now - birthday
    return delta.days


def count_persons():
    result = get_json_dict()
    obj = result['results']
    return len(obj)
