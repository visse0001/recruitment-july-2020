from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f'(id:{self.id}, name:{self.nazwa}, fullname{self.fullname}, nickname{self.nickname}'


engine = create_engine('sqlite:///baza.db', echo=True)
Base.metadata.create_all(bind=engine)