import datetime


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

    def get_sum_persons(self):
        obj = self.data['results']
        return len(obj)

    def get_days_until_birthday(self, index: int, dob: str, bday: str):
        today = datetime.datetime.today()
        birthday = self.get_double_nested_table_data(index, dob, bday)
        birthday = datetime.datetime.strptime(birthday, "%Y-%m-%dT%H:%M:%S.%fZ")
        birthday.replace(year=today.year)
        if birthday < today:
            try:
                birthday = birthday.replace(year=today.year + 1)
            except ValueError:
                birthday = birthday.replace(year=today.year + 4)
        days_to_birthday = abs(birthday - today)
        return days_to_birthday.days
