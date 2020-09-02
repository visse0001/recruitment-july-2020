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
    # create two datetime objects
    now = datetime.now()
    current_year = now.year
    next_year = current_year + 1
    birthday_str = get_double_nested_table_data(index, dob, date)
    birthday_datetime_obj = datetime.strptime(birthday_str, "%Y-%m-%dT%H:%M:%S.%fZ")

    # change birth year to current year
    obj_birthday_with_current_year = birthday_datetime_obj.replace(year=current_year)

    # check if bithday month and day is 29 February
    day = obj_birthday_with_current_year.day
    month = obj_birthday_with_current_year.month
    if day == 29 and month == 2:
        # change day 29 to 28. Then add 1 day to delta.days
        new_birthday = obj_birthday_with_current_year.replace(day=28)

        delta = new_birthday - now
        # Add missing 1 day to delta result
        delta_days = delta.days + 1

        # bithday was in this year. Need to use next year
        if delta_days < 0:
            new_birthday = new_birthday.replace(year=next_year)
            delta = new_birthday - now
            delta_days = delta.days
            return delta_days

        # if birthday will be in this year
        return delta_days

    # birthday month and day is not 29 February
    else:
        delta = obj_birthday_with_current_year - now
        delta_days = delta.days

        # birthday was in this year. Need to use next year
        if delta_days < 0:
            new_birthday = obj_birthday_with_current_year.replace(year=next_year)
            delta = new_birthday - now
            delta_days = delta.days
            return delta_days

        # if birthday will be in this year
        return delta_days
