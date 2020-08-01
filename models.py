from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from parse_json import JSON_NAME, get_not_nested_column_data, get_title_nested_column_data

Base = declarative_base()


class Person(Base):
    __tablename__ = 'persons'

    id = Column('id', Integer, primary_key=True)
    name = relationship("Name", uselist=False, back_populates="person")
    gender = Column(String)

    def __repr__(self):
        return f'(id:{self.id}, gender:{self.name}'


class Name(Base):
    __tablename__ = 'names'

    id = Column('id', Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship("Person", back_populates="name")
    title = Column(String)

    def __repr__(self):
        return f'(id:{self.id}, title:{self.title}'


engine = create_engine('sqlite:///persons.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()
person = Person()

person.gender = get_not_nested_column_data(JSON_NAME, "gender")
person.name = Name(title=get_title_nested_column_data(JSON_NAME))
session.add(person)
session.commit()
session.close()
