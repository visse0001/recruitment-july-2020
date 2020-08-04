from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

import sqlite3

from parse_json import get_not_nested_table_data, get_double_nested_table_data, get_triple_nested_table_data, \
    remove_special_characters_from_string, get_days_until_birthday, get_not_nested_table_data_from_all_indexes, \
    count_indexes, list_wihout_spec_char

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

    def __repr__(self):
        return f'(id:{self.id}, gender:{self.name})'


class Name(Base):
    __tablename__ = 'name'

    id = Column('id', Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship("Person", back_populates="name")
    title = Column(String)

    def __repr__(self):
        return f'(id:{self.id}, title:{self.title})'


class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True)
    street = relationship("Street", uselist=False, back_populates="location")
    coordinates = relationship("Coordinates", uselist=False, back_populates="location")
    timezone = relationship("Timezone", uselist=False, back_populates="location")
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship("Person", back_populates="location")
    city = Column(String)
    state = Column(String)
    country = Column(String)
    postcode = Column(Integer)


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


engine = create_engine('sqlite:///persons.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()
person = Person()
location = Location()
street = Street()
dob = Dob()
login = Login()
id_person = IdPerson()

all_genders = get_not_nested_table_data_from_all_indexes("gender")
all_emails = get_not_nested_table_data_from_all_indexes("email")
all_phone_with_spec_char = get_not_nested_table_data_from_all_indexes("phone")
all_phone = list_wihout_spec_char(all_phone_with_spec_char)
all_cell_with_spec_char = get_not_nested_table_data_from_all_indexes("cell")
all_cell = list_wihout_spec_char(all_cell_with_spec_char)
all_nat = get_not_nested_table_data_from_all_indexes("nat")



def bulk_save_persons():
    index = 0
    persons = []
    for element in range(count_indexes()):
        person = Person(gender=all_genders[index], email=all_emails[index], phone=all_phone[index], cell=all_cell[index], nat=all_nat[index])
        persons.append(person)
        index += 1

    session.add_all(persons)
    session.commit()


bulk_save_persons()

session.commit()

session.close()
