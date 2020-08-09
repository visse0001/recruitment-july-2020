from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from datetime import datetime

from base import Person, Dob, Location, Login

engine = create_engine('sqlite:///persons.db', echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


def sum_all():
    sum_all = session.query(Person).count()
    return sum_all


def perc_women():
    sum_women = session.query(Person).filter_by(gender='female').count()
    perc_women = (sum_women * 100) / sum_all()
    return perc_women


def perc_man():
    sum_men = session.query(Person).filter_by(gender='male').count()
    perc_men = (sum_men * 100) / sum_all()
    return perc_men


def average_age_overall():
    sum_age = session.query(func.sum(Dob.age)).scalar()
    av_age = sum_age / sum_all()
    return av_age


def most_common_cities(n):
    cities = session.query(Location.city).all()
    list_cities = list(map(''.join, cities))
    count_cities_dict = {i: list_cities.count(i) for i in list_cities}
    sorted_dict = {k: v for k, v in sorted(count_cities_dict.items(), key=lambda x: x[1])}
    sort_cities = sorted(sorted_dict.items(), key=lambda x: x[1], reverse=True)

    for i in range(n):
        list_elements = [a_tuple[0] for a_tuple in sort_cities]

    list_n_cities = list_elements[0:n]

    return list_n_cities


def most_common_passwords(n):
    passwords = session.query(Login.password).all()
    list_passwords = list(map(''.join, passwords))
    count_passwords_dict = {i: list_passwords.count(i) for i in list_passwords}
    sorted_dict = {k: v for k, v in sorted(count_passwords_dict.items(), key=lambda x: x[1])}
    list_by_value = sorted(sorted_dict.items(), key=lambda x: x[1], reverse=True)

    for i in range(n):
        list_elements = [a_tuple for a_tuple in list_by_value]

    list_n_passwords = list_elements[0:n]

    return list_n_passwords


def is_born_in_date_range():
    start_date = "1988-08-11"
    end_date = "2010-08-11"
    obj_start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    obj_end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    # obj_end_date returns <class 'datetime.date'> 2020-08-11

    list_tuples_birthday_dates = session.query(Dob.date).all()
    list_bithday_dates = [item for t in list_tuples_birthday_dates for item in t]

    birthday_persons = []

    for str_date in list_bithday_dates:
        birthday_datetime_obj = datetime.strptime(str_date, "%Y-%m-%dT%H:%M:%S.%fZ").date()

        if (birthday_datetime_obj > obj_start_date) and (birthday_datetime_obj < obj_end_date):
            birthday_persons.append(str_date)



is_born_in_date_range()
