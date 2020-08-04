# The script created for recruitment to Profil Software

Link to the [task](https://git.profil-software.com/recruitment-july-2020/backend).


### Virtual Enviroment
Create a virtual environment: <br/>
`python3.7 -m venv env`

To activate a venv: <br/>
`source env/bin/activate`

## Dependencies
[Python 3.7](https://www.python.org/downloads/) <br>
[pip](https://pip.pypa.io/en/stable/installing/) <br>
[SQLAlchemy](https://docs.sqlalchemy.org/en/13/intro.html)

To install dependencies from requirements.txt: <br>
`pip install -r requirements.txt`

## Prettier JSON

You can use this command below to make JSON easier to read: <br/>
`python -m json.tool persons.json pretty_persons.json`