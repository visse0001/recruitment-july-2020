from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from base import Person, Dob
from parse_json import count_persons
engine = create_engine('sqlite:///persons.db', echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

def perc_women():
    sum_women = session.query(Person).filter_by(gender='female').count()
    perc_women = (sum_women * 100) / count_persons()
    return perc_women

def perc_man():
    sum_men = session.query(Person).filter_by(gender='male').count()
    perc_men = (sum_men * 100) / count_persons()
    return perc_men

def average_age_overall():
    sum_age = session.query(func.sum(Dob.age)).scalar()
    av_age = sum_age/count_persons()
    return av_age
