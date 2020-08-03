from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import select
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
# OR
compiled_second = expression_postgres.compile().params
print(compiled.params)
print(compiled_second)
# {'gender_1': 'ed'}

print(expression_postgres.right)
print(expression_postgres.left)
# :gender_1
# user.gender

print(expression_postgres.operator)
# <built-in function eq>

print(expression_mysql.left)
# user.gender

engine.execute(
    user_table.select().where(user_table.c.gender == 'female')
)
"""
FROM user 
WHERE user.gender = ?
2020-08-03 13:57:47,974 INFO sqlalchemy.engine.base.Engine ('female',)
"""

# INSERT
insert_stmt = user_table.insert().values(gender='male', email='john@doe.com')
conn = engine.connect()
result = conn.execute(insert_stmt)

# SELECT
select_stmt = select([user_table.c.gender, user_table.c.email]). \
    where(user_table.c.gender == 'male')
result_select = conn.execute(select_stmt)
for row in result_select:
    print(row)
