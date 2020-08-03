from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from parse_json import JSON_NAME, get_not_nested_column_data, get_title_nested_column_data, get_street_name_or_number

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    id = Column('id', Integer, primary_key=True)
    name = relationship("Name", uselist=False, back_populates="person")
    gender = Column(String)
    location = relationship("Location", uselist=False, back_populates="person")

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

person.gender = get_not_nested_column_data(JSON_NAME, "gender")
person.name = Name(title=get_title_nested_column_data(JSON_NAME))
person.id = 1
person.location = Location(person_id=1)
session.add(person)

location.street = Street(name=get_street_name_or_number(JSON_NAME, 'name'),
                         number=get_street_name_or_number(JSON_NAME, 'number'),
                         location_id=1)
session.add(location)


# result = session.query(Street) \
#     .filter(Street.id == 1) \
#     .update({'name': 'grunwaldzka'})

session.commit()

# Implicit JOIN
# query = session.query(Person, Name).filter(Person.id == Name.person_id).all()
# print(query)

# JOIN to use the relationship()-bound
# query2 = session.query(Person, Name).join(Person.name).all()
# print(query2)

# either Person and Name may be reffered to anyway in the query
# query3 = session.query(Person, Name).join(Person.name).filter(Name.title == 'Miss').first()
# print(query3)

# we can specify an explicit FROM using select_from()
query4 = session.query(Person, Name).select_from(Name).join(Name.person).all()
print(query4)


# result2 = engine.execute("select * from street")
# for row in result2:
#     print(row)

session.close()
