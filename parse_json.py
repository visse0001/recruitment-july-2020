import json
import datetime
from datetime import datetime, date

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
    birth = get_double_nested_table_data(index, first_table, second_table)
    month = int(birth[5:7])
    day = int(birth[8:10])

    today = date.today()

    birthday = date(today.year, month, day)
    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)
    time_to_birthday = abs(birthday - today)
    time_to_birthday = str(time_to_birthday)[0:3]
    time_to_birthday = int(time_to_birthday)

    return time_to_birthday


def delete_zero_from_str_if_first(a_string):
    if a_string[0] == 0:
        a_string = int(a_string[1])
    return a_string


def count_persons():
    result = get_json_dict()
    obj = result['results']
    return len(obj)


def get_not_nested_table_data_from_all_indexes(table_name: str):
    result = get_json_dict()
    results_list = []
    index = 0
    for element in range(count_persons()):
        obj = result['results'][index][table_name]
        index += 1
        str_obj = str(obj)
        results_list.append(str_obj)
    return results_list


def get_double_nested_table_data_from_all_indexes(first_table: str, second_table: str):
    result = get_json_dict()
    results_list = []
    index = 0
    for element in range(count_persons()):
        obj = result['results'][index][first_table][second_table]
        index += 1
        str_obj = str(obj)
        results_list.append(str_obj)
    return results_list


def get_triple_nested_table_data_from_all_indexes(first_table: str, second_table: str, third_table: str):
    result = get_json_dict()
    results_list = []
    index = 0
    for element in range(count_persons()):
        obj = result['results'][index][first_table][second_table][third_table]
        index += 1
        str_obj = str(obj)
        results_list.append(str_obj)
    return results_list


def list_wihout_spec_char(seq):
    new_list = []
    for element in seq:
        result = remove_special_characters_from_string(element)
        new_list.append(result)
    return new_list

# get_days_until_birthday(0, "dob", "date")
