from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from parse_json import get_not_nested_table_data, get_double_nested_table_data, get_triple_nested_table_data, \
    remove_special_characters_from_string, get_days_until_birthday

from base import Person, Name, Location, Street, Login, Coordinates, Timezone, Dob, Registered, IdPerson,

Base = declarative_base()

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

person.gender = get_not_nested_table_data(0, "gender")
person.name = Name(title=get_double_nested_table_data(0, "name", "title"))
person.phone = remove_special_characters_from_string(get_not_nested_table_data(0, "phone"))
person.cell = remove_special_characters_from_string(get_not_nested_table_data(0, "cell"))
person.email = get_not_nested_table_data(0, "email")
person.nat = get_not_nested_table_data(0, "nat")
person.location = Location(person_id=1)
person.login = Login(uuid=get_double_nested_table_data(0, 'login', 'uuid'),
                     username=get_double_nested_table_data(0, 'login', 'username'),
                     password=get_double_nested_table_data(0, 'login', 'password'),
                     salt=get_double_nested_table_data(0, 'login', 'salt'),
                     md5=get_double_nested_table_data(0, 'login', 'md5'),
                     sha1=get_double_nested_table_data(0, 'login', 'sha1'),
                     sha256=get_double_nested_table_data(0, 'login', 'sha256'),
                     person_id=1)

person.registered = Registered(date=get_double_nested_table_data(0, "registered", "date"),
                               age=get_double_nested_table_data(0, "registered", "age"),
                               )
person.id_person = IdPerson(name=get_double_nested_table_data(0, "id", "name"),
                            value=get_double_nested_table_data(0, "id", "value"),
                            person_id=1
                            )

location.street = Street(name=get_triple_nested_table_data(0, 'location', 'street', 'name'),
                         number=get_triple_nested_table_data(0, 'location', 'street', 'number'),
                         location_id=1)

location.coordinates = Coordinates(latitude=get_triple_nested_table_data(0, "location", "coordinates", "latitude"),
                                   longitude=get_triple_nested_table_data(0, "location", "coordinates", "longitude"),
                                   location_id=1)

location.timezone = Timezone(offset=get_triple_nested_table_data(0, "location", "timezone", "offset"),
                             description=get_triple_nested_table_data(0, "location", "timezone", "description"),
                             location_id=1)

dob.date = get_double_nested_table_data(0, "dob", "date")
dob.age = get_double_nested_table_data(0, "dob", "age")
dob.days_until_birth = get_days_until_birthday(0, "dob", "date")
dob.person_id = 1