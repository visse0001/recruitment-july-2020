from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy import engine, inspect
from sqlalchemy.dialects import mysql, postgresql

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

# Second way - it doesn't work, I don't know why
# with engine.connect() as conn:
#     metadata.create_all(conn, checkfirst=False)
#
inspector = inspect(engine)
table_names = inspector.get_table_names()
print(table_names)

columns = inspector.get_columns('street')
print(columns)


print(user_table.c.id + 5)
# "user".id + :id_1

print(user_table.c.gender + "same name")
# "user".gender || :gender_1

expression_mysql = user_table.c.gender == 'ed'
print(expression_mysql.compile(dialect=mysql.dialect()))
# user.gender = %s

expression_postgres = user_table.c.gender == 'ed'
print(expression_postgres.compile(dialect=postgresql.dialect()))
# "user".gender = %(gender_1)s

compiled = expression_postgres.compile()
print(compiled.params)
# {'gender_1': 'ed'}