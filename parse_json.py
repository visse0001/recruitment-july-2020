import datetime
from dataclasses import dataclass

from api import DataAPI


class ParseData:
    def __init__(self, data):
        self.data = data

    def get_not_nested_table_data(self, index: int, table_name: str):
        obj = self.data['results'][index][table_name]
        return obj

    def get_double_nested_table_data(self, index: int, first_table: str, second_table: str):
        obj = self.data['results'][index][first_table][second_table]
        return obj

    def get_triple_nested_table_data(self, index: int, first_table: str, second_table: str, third_table: str):
        obj = self.data['results'][index][first_table][second_table][third_table]
        return obj

    def get_datetime_obj_from_str(a_string):
        date_obj = datetime.datetime.strptime(a_string, "%Y-%m-%dT%H:%M:%S.%fZ")
        return date_obj

    def get_sum_persons(self):
        obj = self.data['results']
        return len(obj)

    def get_days_until_birthday(self, index: int, dob: str, bday: str):
        is_leap_year = False
        today = datetime.datetime.today()
        birthday = self.get_double_nested_table_data(index, dob, bday)
        birthday = datetime.datetime.strptime(birthday, "%Y-%m-%dT%H:%M:%S.%fZ")
        if self.__is_leap_year(birthday):
            is_leap_year = True
            birthday = self.__substract_day(birthday)
        birthday.replace(year=today.year)
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
        days_to_birthday = abs(birthday - today)
        if is_leap_year:
            days_to_birthday.days += 1
        return days_to_birthday.days

    def __is_leap_year(self, birthday):
        if (birthday.year % 4 == 0) and (birthday.year % 100 != 0):
            return True

    def __substract_day(self, birthday):
        return birthday.replace(day=28)
