from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    def __repr__(self):
        return "<User(%r, %r)>" % (
            self.name, self.fullname
        )


ed_user = User(name="ed", fullname="Edward Jones")

engine = create_engine('sqlite:///base3.db', echo=True)
Base.metadata.create_all(bind=engine)
session = Session(bind=engine)

session.add(ed_user)

session.add_all([
    User(name='wendy', fullname="Wendy Weather"),
    User(name='mary', fullname="Mary Con"),
    User(name='fred', fullname="Fred Flin")
])

session.commit()

ed_user.name = "Edwardo"
fake_user = User(name='fakeuser', fullname='invalid')
session.add(fake_user)

query = session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()
print(query)
ed_nam = ed_user.name
print(ed_nam)

session.rollback()
if fake_user in session:
    print("True")
else:
    print("False")

from sqlalchemy import select

sel = select([User.name, User.fullname]).where(User.name == 'ed').order_by(User.id)
result = session.connection().execute(sel).fetchall()
print(result)

query_two = session.query(User).filter(User.name == 'ed').order_by(User.id)
print(query_two.all())
# result: [<User('ed', 'Edward Jones')>, <User('ed', 'Edward Jones')>, <User('ed', 'Edward Jones')>]

for name, fullname in session.query(User.name, User.fullname):
    print(name, fullname)
"""
result:
ed Edward Jones
wendy Wendy Weather
mary Mary Con
fred Fred Flin
"""

for row in session.query(User, User.name):
    print(row.User, row.name)
"""
result:
<User('ed', 'Edward Jones')> ed
<User('wendy', 'Wendy Weather')> wendy
<User('mary', 'Mary Con')> mary
<User('fred', 'Fred Flin')> fred
"""