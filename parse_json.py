import json
from datetime import datetime

JSON_NAME = "persons.json"


def get_json_dict():
    with open(JSON_NAME, encoding='utf-8') as f:
        json_content = json.load(f)
    return json_content


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


def get_datetime_obj_from_str(a_string):
    date_obj = datetime.strptime(a_string, "%Y-%m-%dT%H:%M:%S.%fZ")
    return date_obj


def count_persons():
    result = get_json_dict()
    obj = result['results']
    return len(obj)


def get_days_until_birthday(index: int, dob: str, date: str):
    birthday = get_double_nested_table_data(index, dob, date)
    today = datetime.now()
    birthday = datetime.strptime(birthday, "%Y-%m-%dT%H:%M:%S.%fZ")
    is_leap = False
    if birthday.month == 2 and birthday.day == 29:
        birthday = birthday.replace(day=28)
        is_leap = True
    birthday = birthday.replace(year=today.year)
    if birthday < today:
        if not is_leap:
            birthday = birthday.replace(year=today.year + 1)
        else:
            birthday = birthday.replace(year=today.year + 4)
    days_to_birthday = abs(birthday - today)
    if is_leap:
        return days_to_birthday.days + 1
    return days_to_birthday.days
