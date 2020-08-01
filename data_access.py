from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = 'persons'

    id = Column('id', Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f'id:{self.id}, name:{self.name}, fullname{self.fullname}, nickname{self.nickname}'


engine = create_engine('sqlite:///persons.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()

persons = session.query(Person).all()
print(persons)
for person in persons:
    print(person)

session.commit()
session.close()