from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy import engine

Base = declarative_base()

engine = create_engine('sqlite:///persons.db', echo=True)

metadata = MetaData()

user_table = Table('user', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('gender', String),
                   Column('email', String)
                   )

name_table = Table('name', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('user_id', Integer, ForeignKey("user.id"))
                   )

location_table = Table('location', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('user_id', Integer, ForeignKey("user.id")),
                   )

street_table = Table('street', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('location_id', Integer, ForeignKey("location.id")),
                   Column('name', String),
                   Column('number', Integer),
                   )



# First way to create all tables
metadata.create_all(engine)
# metadata.drop_all(engine)



# Second way - it doesn't work, I don't know why
# with engine.connect() as conn:
#     metadata.create_all(conn, checkfirst=False)
#
# inspector = inspect(engine)
# table_names = inspector.get_table_names()
# print(table_names)

print()
#
# columns = inspector.get_columns('street')
# print(columns)

# for tname in inspector.get_table_names():
#     for column in inspector.get_columns(tname):
#         if column["street"] == 'number':
#             print(tname)
