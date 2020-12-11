import datetime

from api import get_data_from_api

data = get_data_from_api()


def get_not_nested_table_data(index: int, table_name: str):
    obj = data['results'][index][table_name]
    return obj


def get_double_nested_table_data(index: int, first_table: str, second_table: str):
    obj = data['results'][index][first_table][second_table]
    return obj


def get_triple_nested_table_data(index: int, first_table: str, second_table: str, third_table: str):
    obj = data['results'][index][first_table][second_table][third_table]
    return obj


def remove_special_characters_from_string(a_string: str):
    alpha_numeric = ""
    for character in a_string:
        if character.isalnum():
            alpha_numeric += character
    return alpha_numeric


def get_datetime_obj_from_str(a_string):
    date_obj = datetime.datetime.strptime(a_string, "%Y-%m-%dT%H:%M:%S.%fZ")
    return date_obj


def count_persons():
    obj = data['results']
    return len(obj)


def get_days_until_birthday(index: int, dob: str, bday: str):
    today = datetime.datetime.today()
    birthday = get_double_nested_table_data(index, dob, bday)
    birthday = datetime.datetime.strptime(birthday, "%Y-%m-%dT%H:%M:%S.%fZ")
    birthday.replace(year=today.year)
    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)
    days_to_birthday = abs(birthday - today)
    return days_to_birthday.days


