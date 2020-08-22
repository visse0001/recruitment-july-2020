from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from datetime import datetime

from base import Person, Dob, Location, Login, Name

engine = create_engine('sqlite:///persons.db', echo=False)

Base = declarative_base()

Session = sessionmaker(bind=engine)
Session = sessionmaker()
Session.configure(bind=engine)


def dbconnect(func):
    def inner(*args, **kwargs):
        session = Session()
        func(*args, session=session, **kwargs)
        session.close()

    return inner


@dbconnect
def sum_all(session):
    sum_all = session.query(Person).count()
    return sum_all


@dbconnect
def perc_women(session):
    sum_women = session.query(Person).filter_by(gender='female').count()
    perc_women = (sum_women * 100) / sum_all()
    return perc_women


@dbconnect
def perc_man(session):
    sum_men = session.query(Person).filter_by(gender='male').count()
    perc_men = (sum_men * 100) / sum_all()
    return perc_men


@dbconnect
def average_age_overall(session):
    sum_age = session.query(func.sum(Dob.age)).scalar()
    av_age = sum_age / sum_all()
    return int(av_age)


@dbconnect
def average_age_female_or_man(gender: str, session):
    sum_age = session.query(func.sum(Dob.age)).join(Person).filter_by(gender=f'{gender}').scalar()
    if gender == "female":
        query = session.query(Person).filter_by(gender='female').count()
        av_age = sum_age / query

    if gender == "male":
        query = session.query(Person).filter_by(gender='male').count()
        av_age = sum_age / query

    return int(av_age)


@dbconnect
def most_common_cities(n, session):
    cities = session.query(Location.city).all()
    list_cities = list(map(''.join, cities))
    count_cities_dict = {i: list_cities.count(i) for i in list_cities}
    sorted_dict = {k: v for k, v in sorted(count_cities_dict.items(), key=lambda x: x[1], reverse=True)}

    for i in range(n):
        list_elements = [a_tuple for a_tuple in sorted_dict]

    list_n_cities = list_elements[0:n]

    return list_n_cities


@dbconnect
def most_common_passwords(n: int, session):
    passwords = session.query(Login.password).all()
    list_passwords = list(map(''.join, passwords))
    count_passwords_dict = {i: list_passwords.count(i) for i in list_passwords}
    sorted_dict = {k: v for k, v in sorted(count_passwords_dict.items(), key=lambda x: x[1], reverse=True)}

    for i in range(n):
        list_elements = [a_tuple for a_tuple in sorted_dict]

    list_n_passwords = list_elements[0:n]

    return list_n_passwords


@dbconnect
def is_born_in_date_range(start_date: str, end_date: str, session):
    start_date = start_date
    end_date = end_date
    obj_start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    obj_end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

    list_tuples_birthday_dates = session.query(Dob.date).all()
    list_bithday_dates = [item for t in list_tuples_birthday_dates for item in t]

    # Create list of bithdays between two dates
    birthday_persons = []

    ids_list = []

    for str_date in list_bithday_dates:
        birthday_datetime_obj = datetime.strptime(str_date, "%Y-%m-%dT%H:%M:%S.%fZ").date()

        # Check if date is between start and end dates and append list
        if (birthday_datetime_obj > obj_start_date) and (birthday_datetime_obj < obj_end_date):
            birthday_persons.append(str_date)

            # Get dates and id numbers
            dates_ids = session.query(Dob.date, Dob.person_id).all()

            # Covert this list of tuples into a dict
            dates_ids = dict(dates_ids)

            # Create list of ids
            ids_list = [dates_ids[x] for x in birthday_persons if dates_ids.get(x)]

    # Find persons names by id
    list_of_tuples_names = []
    for i in ids_list:
        query = session.query(Name).get(i)
        list_of_tuples_names.append(query)
    return list_of_tuples_names


@dbconnect
def most_safety_password(session):
    # Get all passwords into a list
    passwords = session.query(Login.password).all()
    passwords_list = [item for t in passwords for item in t]

    # Get unique passwords
    unique_passwords = list(set(passwords_list))

    def count(a_string: str):
        points = 0
        if any(c for c in a_string if c.islower()):
            points += 1

        if any(c for c in a_string if c.isupper()):
            points += 2

        if any(c for c in a_string if c.isdigit()):
            points += 1

        if len(a_string) >= 8:
            points += 5

        if any(c for c in a_string if c.isalnum()):
            points += 3

        return points

    points_list = []
    for element in unique_passwords:
        points = count(element)
        points_list.append(points)

    # Create a dict from two lists
    zip_iterator = zip(unique_passwords, points_list)
    a_dictionary = dict(zip_iterator)

    sorted_by_value = sorted(a_dictionary.items(), key=lambda t: t[1], reverse=True)

    return sorted_by_value[0]
