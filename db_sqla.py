from sqlalchemy.orm import sessionmaker

from models import Person

from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('sqlite:///sqla.db')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    new_person = Person(name='John')

    session.add(new_person)
    session.commit()