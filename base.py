from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

import sqlite3

from parse_json import get_not_nested_table_data, get_double_nested_table_data, get_triple_nested_table_data, \
    remove_special_characters_from_string, get_days_until_birthday, get_not_nested_table_data_from_all_indexes, \
    count_persons, list_wihout_spec_char, get_double_nested_table_data_from_all_indexes, \
    get_triple_nested_table_data_from_all_indexes, JSON_NAME

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    id = Column('id', Integer, primary_key=True)
    gender = Column(String)
    name = relationship("Name", uselist=False, back_populates="person")
    location = relationship("Location", uselist=False, back_populates="person")
    email = Column(String)
    login = relationship("Login", uselist=False, back_populates="person")
    dob = relationship("Dob", uselist=False, back_populates="person")
    registered = relationship("Registered", uselist=False, back_populates="person")
    phone = Column(String)
    cell = Column(String)
    id_person = relationship("IdPerson", uselist=False, back_populates="person")
    nat = Column(String)
    days_until_birthday = Column(Integer)

    def __repr__(self):
        return f'(id:{self.id}, gender:{self.name})'


class Name(Base):
    __tablename__ = 'name'

    id = Column('id', Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship("Person", back_populates="name")
    title = Column(String)
    first = Column(String)
    last = Column(String)

    def __repr__(self):
        return f'(id:{self.id}, title:{self.title}, first:{self.first}, last:{self.last})'


class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship("Person", back_populates="location")
    street = relationship("Street", uselist=False, back_populates="location")
    city = Column(String)
    state = Column(String)
    country = Column(String)
    postcode = Column(Integer)
    coordinates = relationship("Coordinates", uselist=False, back_populates="location")
    timezone = relationship("Timezone", uselist=False, back_populates="location")


class Street(Base):
    __tablename__ = 'street'

    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey('location.id'))
    location = relationship("Location", back_populates="street")
    name = Column(String)
    number = Column(Integer)

    def __repr__(self):
        return f'(id:{self.id}, name:{self.name}, number:{self.number})'


class Login(Base):
    __tablename__ = 'login'

    id = Column('id', Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship("Person", back_populates="login")
    uuid = Column(String)
    username = Column(String, unique=True)
    password = Column(String)
    salt = Column(String)
    md5 = Column(String)
    sha1 = Column(String)
    sha256 = Column(String)

    def __repr__(self):
        return f'(id:{self.id}, username:{self.username})'


class Dob(Base):
    __tablename__ = 'dob'

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship("Person", back_populates="dob")
    date = Column(String)
    age = Column(Integer)
    days_until_birth = Column(Integer)

    def __repr__(self):
        return f'(id:{self.id}, date:{self.date}, age:{self.age}, days_until_birth:{self.days_until_birth})'


class Registered(Base):
    __tablename__ = 'registered'

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship("Person", back_populates="registered")
    date = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f'(id:{self.id}, date:{self.date}, age:{self.age})'


class IdPerson(Base):
    __tablename__ = 'id_person'

    id_person = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship("Person", back_populates="id_person")
    name = Column(String)
    value = Column(String)

    def __repr__(self):
        return f'(id:{self.id_person}, name:{self.name}, value:{self.value})'


class Coordinates(Base):
    __tablename__ = 'coordinates'

    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey('location.id'))
    location = relationship("Location", back_populates="coordinates")
    latitude = Column(String)
    longitude = Column(String)

    def __repr__(self):
        return f'(id:{self.id}, latitude:{self.latitude}, longitude:{self.longitude})'


class Timezone(Base):
    __tablename__ = 'timezone'

    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey('location.id'))
    location = relationship("Location", back_populates="timezone")
    offset = Column(String)
    description = Column(String)

    def __repr__(self):
        return f'(id:{self.id}, offset:{self.offset}, description:{self.description})'


engine = create_engine('sqlite:///persons.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()
person = Person()
name = Name()
# location = Location()
# street = Street()
# login = Login()
# coordinates = Coordinates()
# timezone = Timezone()
# dob = Dob()
# registered = Registered()
# id_person = IdPerson()

# populate data
# for, person, location -> person, ... commit, next index
session = Session()
count_of_persons = count_persons()
for index in range(1000):
    person = Person(gender=get_not_nested_table_data(index, "gender"),
                    email=get_not_nested_table_data(index, "email"),
                    phone=remove_special_characters_from_string(get_not_nested_table_data(index, "phone")),
                    cell=remove_special_characters_from_string(get_not_nested_table_data(index, "cell")),
                    days_until_birthday=get_days_until_birthday(index, "dob", "date"),
                    nat=get_not_nested_table_data(index, "nat"),
                    )
    session.add(person)
    session.commit()

    name = Name(title=get_double_nested_table_data(index, "name", "title"),
                first=get_double_nested_table_data(index, "name", "first"),
                last=get_double_nested_table_data(index, "name", "last"),
                person_id=person.id
                )
    session.add(name)
    session.commit()
session.close()
