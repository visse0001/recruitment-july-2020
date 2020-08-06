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


def count_persons():
    result = get_json_dict()
    obj = result['results']
    return len(obj)


def is_leap_year(year: int, month, day: int):
    """
    Leap year is a year that compiles requirements:
    - is divisible by 4
    - is not divisible by 100
    - is divisable by 400
    Each leap year has 366 days instead of 365,
    by extending February to 29 days
    rather than the common 28.
    """
    if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)) and month == 2 and day == 29:
        return True


def get_days_until_birthday(index: int, dob: str, date: str):
    # create two datetime objects
    now = datetime.now()
    current_year = now.year
    birthday_str = get_double_nested_table_data(index, dob, date)
    birthday_datetime_obj = datetime.strptime(birthday_str, "%Y-%m-%dT%H:%M:%S.%fZ")

    # change birth year to current year
    obj_birthday_with_current_year = birthday_datetime_obj.replace(year=current_year)

    # delta time
    delta = obj_birthday_with_current_year - now

    delta_days = delta.days

    month = obj_birthday_with_current_year.month
    day = obj_birthday_with_current_year.day
    # check if the delta is a negative number
    if delta_days < 0:
        # it means that the birthday was already this year

        # need to look at the next year
        next_year = int(current_year + 1)
        obj_birthday_with_current_year.replace(year=next_year)

        # get bithday month and day
        month = obj_birthday_with_current_year.month
        day = obj_birthday_with_current_year.day

        # check if this date is in a leap year
        if is_leap_year(current_year, month, day):
            # then change day from 29 to 28 and add to delta.days + 1 missing day
            birthday_with_eariel_day = obj_birthday_with_current_year.replace(day=28)
            delta = birthday_with_eariel_day - now
            delta_days = delta.days + 1
            return delta_days

        # delta
        delta = obj_birthday_with_current_year - now
        delta_days = delta.days
        return delta_days
    else:
        # birthday will be in this year

        # check if this date is in a leap year
        if is_leap_year(current_year, month, day):
            # then change day from 29 to 28 and add to delta.days + 1 missing day
            birthday_with_eariel_day = obj_birthday_with_current_year.replace(day=28)

            # delta
            delta = now - birthday_with_eariel_day
            delta_days = delta.days + 1
            return delta_days
        else:
            # delta
            delta = now - obj_birthday_with_current_year
            delta_days = delta.days
            return delta_days


g = get_days_until_birthday(398, "dob", "date")
# g = get_double_nested_table_data(398, "dob", "date")
print(g)
