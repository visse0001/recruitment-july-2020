from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from parse_json import JSON_NAME, get_gender

Base = declarative_base()


class Person(Base):
    __tablename__ = 'persons'

    id = Column('id', Integer, primary_key=True)
    gender = Column(String)

    def __repr__(self):
        return f'(id:{self.id}, gender:{self.name}'


engine = create_engine('sqlite:///persons.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()
person = Person()

person.gender = get_gender(JSON_NAME)

session.add(person)
session.commit()
session.close()
