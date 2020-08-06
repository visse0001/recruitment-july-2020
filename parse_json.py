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


def get_datetime_obj_from_str(a_string):
    date_obj = datetime.strptime(a_string, "%Y-%m-%dT%H:%M:%S.%fZ")
    return date_obj


def is_leap_year(str_year):
    """
    Leap year is a year that compiles requirements:
    - is divisible by 4
    - is not divisible by 100
    - is divisable by 400
    Each leap year has 366 days instead of 365,
    by extending February to 29 days
    rather than the common 28.
    """
    int_year = int(str_year)
    if ((int_year % 4 == 0) and (int_year % 100 != 0)) or (int_year % 400 == 0):
        return True


def get_days_until_birthday(index: int, dob: str, date: str):
    now = datetime.now()
    year = now.year
    birthday_str = get_double_nested_table_data(index, dob, date)
    birthday_str = str(year) + birthday_str[4:]
    birthday = get_datetime_obj_from_str(birthday_str)
    delta = birthday - now
    delta_days = delta.days + 1
    if delta_days < 0:
        birthday_str_next_year = str(year + 1) + birthday_str[4:]
        birthday = get_datetime_obj_from_str(birthday_str_next_year)
        delta = birthday - now
        delta_days = delta.days
    return delta_days


def count_persons():
    result = get_json_dict()
    obj = result['results']
    return len(obj)
