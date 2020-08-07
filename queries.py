from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from base import Person

engine = create_engine('sqlite:///persons.db', echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

results = session.query(Person).filter_by(gender='female').all()
print(results)
