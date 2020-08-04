import json
import datetime

JSON_NAME = "persons.json"


def get_json_dict(json_name):
    json_file = open(json_name, 'r')
    json_data = json_file.read()
    obj = json.loads(json_data)
    return obj


def get_not_nested_table_data(index: int, table_name: str):
    result = get_json_dict(JSON_NAME)
    obj = result['results'][index][table_name]
    return obj


def get_double_nested_table_data(index: int, first_table: str, second_table: str):
    result = get_json_dict(JSON_NAME)
    obj = result['results'][index][first_table][second_table]
    return obj


def get_triple_nested_table_data(index: int, first_table: str, second_table: str, third_table: str):
    result = get_json_dict(JSON_NAME)
    obj = result['results'][index][first_table][second_table][third_table]
    return obj


def remove_special_characters_from_string(a_string: str):
    alpha_numeric = ""
    for character in a_string:
        if character.isalnum():
            alpha_numeric += character
    return alpha_numeric

def get_days_until_birthday(index: int, first_table: str, second_table: str):
    tday = datetime.datetime.now(tz=None)
    current_year = int(str(tday)[0:4])
    current_month = int(str(tday)[5:7])
    current_day = int(str(tday)[8:10])
    str_birthday_date = get_double_nested_table_data(index, first_table, second_table)[0:10]

    list_birthday_date = str_birthday_date.split('-')

    person_month = list_birthday_date[1]
    person_month = int(delete_zero_from_str_if_first(person_month))
    person_day = list_birthday_date[2]
    person_day = int(delete_zero_from_str_if_first(person_day))


    current_date = datetime.date(year=current_year, month=current_month, day=current_day)
    birthday = datetime.date(year=current_year, month=person_month, day=person_day)

    days_until_birthday = birthday - current_date

    str_days_until_birthday = str(days_until_birthday)[1:3]
    int_days_until_birthday = int(str_days_until_birthday)

    if int_days_until_birthday < 0:
        days_until_birthday = current_date - birthday
    else:
        days_until_birthday = birthday - current_date
    only_days_int = int(str(days_until_birthday)[1:3])

    return only_days_int

def delete_zero_from_str_if_first(a_string):
    if a_string[0] == 0:
        a_string = int(a_string[1])
    return a_string

def count_indexes():
    result = get_json_dict(JSON_NAME)
    obj = result['results']
    return len(obj)

def get_not_nested_table_data_from_all_indexes(table_name: str):
    result = get_json_dict(JSON_NAME)
    results_list = []
    index = 0
    for element in range(count_indexes()):
        obj = result['results'][index][table_name]
        index += 1
        str_obj = str(obj)
        results_list.append(str_obj)
    return results_list

def list_wihout_spec_char(seq: list):
    new_list = []
    for element in seq:
        result = remove_special_characters_from_string(element)
        new_list.append(result)
    return new_list

all_genders = get_not_nested_table_data_from_all_indexes("gender")
all_emails = get_not_nested_table_data_from_all_indexes("email")
all_phones = get_not_nested_table_data_from_all_indexes("phone")
all_phones = list_wihout_spec_char(all_phones)
all_cells = get_not_nested_table_data_from_all_indexes("cell")
all_cells = list_wihout_spec_char(all_cells)
all_nat = get_not_nested_table_data_from_all_indexes("nat")

