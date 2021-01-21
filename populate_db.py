from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api import DataAPI
from parse_json import ParseData
from utils import remove_special_char

from db_tables import Base, Person, Name, Location, Street, Login, Dob, Registered, IdPerson, Coordinates, Timezone

if __name__ == '__main__':
    engine = create_engine('sqlite:///persons.db', echo=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    data_api = DataAPI(num_results=1000)
    data_api_response = data_api.response
    parse_data = ParseData(data=data_api_response)
    persons_sum = parse_data.get_sum_persons()
    for index in range(persons_sum):
        person = Person(gender=parse_data.get_not_nested_table_data(index, "gender"),
                        email=parse_data.get_not_nested_table_data(index, "email"),
                        phone=remove_special_char(parse_data.get_not_nested_table_data(index, "phone")),
                        cell=remove_special_char(parse_data.get_not_nested_table_data(index, "cell")),
                        nat=parse_data.get_not_nested_table_data(index, "nat"),
                        )

        session.add(person)

        name = Name(title=parse_data.get_double_nested_table_data(index, "name", "title"),
                    first=parse_data.get_double_nested_table_data(index, "name", "first"),
                    last=parse_data.get_double_nested_table_data(index, "name", "last"),
                    person_id=person.id
                    )

        session.add(name)

        location = Location(city=parse_data.get_double_nested_table_data(index, "location", "city"),
                            state=parse_data.get_double_nested_table_data(index, "location", "state"),
                            country=parse_data.get_double_nested_table_data(index, "location", "country"),
                            postcode=parse_data.get_double_nested_table_data(index, "location", "postcode"),
                            person_id=person.id
                            )

        session.add(location)

        street = Street(location_id=location.id,
                        number=parse_data.get_triple_nested_table_data(index, "location", "street", "number"),
                        name=parse_data.get_triple_nested_table_data(index, "location", "street", "name")
                        )

        session.add(street)

        coordinates = Coordinates(location_id=location.id,
                                  latitude=parse_data.get_triple_nested_table_data(index, "location", "coordinates",
                                                                                   "latitude"),
                                  longitude=parse_data.get_triple_nested_table_data(index, "location", "coordinates",
                                                                                    "longitude"),
                                  )
        session.add(coordinates)

        timezone = Timezone(location_id=location.id,
                            offset=parse_data.get_triple_nested_table_data(index, "location", "timezone", "offset"),
                            description=parse_data.get_triple_nested_table_data(index, "location", "timezone",
                                                                                "description"),
                            )

        session.add(timezone)

        login = Login(person_id=person.id,
                      uuid=parse_data.get_double_nested_table_data(index, "login", "uuid"),
                      username=parse_data.get_double_nested_table_data(index, "login", "username"),
                      password=parse_data.get_double_nested_table_data(index, "login", "password"),
                      salt=parse_data.get_double_nested_table_data(index, "login", "salt"),
                      md5=parse_data.get_double_nested_table_data(index, "login", "md5"),
                      sha1=parse_data.get_double_nested_table_data(index, "login", "sha1"),
                      sha256=parse_data.get_double_nested_table_data(index, "login", "sha256")
                      )

        session.add(login)

        dob = Dob(person_id=person.id,
                  date=parse_data.get_double_nested_table_data(index, "dob", "date"),
                  age=parse_data.get_double_nested_table_data(index, "dob", "age"),
                  days_until_birthday=parse_data.get_days_until_birthday(index, "dob", "date")
                  )

        session.add(dob)

        registered = Registered(person_id=person.id,
                                date=parse_data.get_double_nested_table_data(index, "registered", "date"),
                                age=parse_data.get_double_nested_table_data(index, "registered", "age")
                                )
        session.add(registered)

        id_person = IdPerson(person_id=person.id,
                             name=parse_data.get_double_nested_table_data(index, "id", "name"),
                             value=parse_data.get_double_nested_table_data(index, "id", "value"),
                             )

        session.add(id_person)
        session.commit()

    session.close()
