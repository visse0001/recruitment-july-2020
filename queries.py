from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from base import Person, Dob, Location

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
    tuple_elements = []
    for i in range(n):
        tuple_elements = [a_tuple[0] for a_tuple in sort_cities]
    list_n_cities = tuple_elements[0:n]
    return list_n_cities
