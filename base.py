from sqlalchemy import create_engine, Column, Integer, String, Unicode, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from parse_json import JSON_NAME, get_not_nested_table_data, get_double_nested_table_data, get_triple_nested_table_data, remove_special_characters_from_string, get_days_until_birthday

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    id = Column('id', Integer, primary_key=True)
    name = relationship("Name", uselist=False, back_populates="person")
    gender = Column(String)
    location = relationship("Location", uselist=False, back_populates="person")
    phone = Column(String)
    cell = Column(String)
    dob = relationship("Dob", uselist=False, back_populates="person")

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
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship("Person", back_populates="location")


class Dob(Base):
    __tablename__ = 'dob'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship("Person", back_populates="dob")
    date = Column(String)
    age = Column(Integer)
    days_until_birth = Column(Integer)

class Street(Base):
    __tablename__ = 'street'
    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey('location.id'))
    location = relationship("Location", back_populates="street")
    name = Column(String)
    number = Column(Integer)

    def __repr__(self):
        return f'(id:{self.id}, name:{self.name}, number:{self.number})'


engine = create_engine('sqlite:///persons.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()
person = Person()
location = Location()
street = Street()
dob = Dob()

# To INSERT data into tables
person.gender = get_not_nested_table_data(0, "gender")
person.name = Name(title=get_double_nested_table_data(0, "name", "title"))
person.phone = remove_special_characters_from_string(get_not_nested_table_data(0, "phone"))
person.cell = remove_special_characters_from_string(get_not_nested_table_data(0, "cell"))
person.id = 1
person.location = Location(person_id=1)

location.street = Street(name=get_triple_nested_table_data(0, 'location', 'street', 'name'),
                         number=get_triple_nested_table_data(0, 'location', 'street', 'number'),
                         location_id=1)

dob.date = get_double_nested_table_data(0, "dob", "date")
dob.age = get_double_nested_table_data(0, "dob", "age")
dob.days_until_birth = get_days_until_birthday(0, "dob", "date")
dob.person_id = 1

# To add data
session.add(person)
session.add(location)
session.add(dob)

session.commit()

# To print a result
# result = session.query(Street) \
#     .filter(Street.id == 1) \
#     .update({'name': 'grunwaldzka'})
# print(result)


# result2 = engine.execute("select * from person")
# for row in result2:
#     print(row)

session.close()
