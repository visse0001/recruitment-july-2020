from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_session():
    engine = create_engine('sqlite:///persons.db', echo=False)

    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()

    return session
