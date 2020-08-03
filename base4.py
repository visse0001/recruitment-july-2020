from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

Base = declarative_base()


class Network(Base):
    __tablename__ = 'network'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    def __repr__(self):
        return f'Name: {self.name}'


# network_one = Network(name="net1")
# network_two = Network(name="net2")

engine = create_engine('sqlite:///base4.db', echo=True)
Base.metadata.create_all(bind=engine)
session = Session(bind=engine)


session.add_all([
    Network(name='net1'),
    Network(name='net2')
])

session.flush()

