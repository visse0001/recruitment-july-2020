# The script created for recruitment to Profil Software

Link to the [task](https://git.profil-software.com/recruitment-july-2020/backend).

The script parses the JSON serializer, populates the database with this data.
Contains functions that modify data in the database. The script can be used via the CLI.


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

### How to run

Create a database and populate a database by parsing JSON file.

Use command below and wait for a while:

`python base.py`
 
 Now you may use command below:
 
 `python argp.py --help`
 
 It will return:
 
```
A script that does operations with database data and returns values

optional arguments:
  -h, --help            show this help message and exit
  -p {man,women}, --perc {man,women}
                        Specify percent: man or women.
  -a {man,women,all}, --average_age {man,women,all}
                        Specify average age: man, women, all.
  -m, --most_safety_password
                        Return most safety password from database.
  -c MOST_COMMON_CITIES, --most_common_cities MOST_COMMON_CITIES
                        Specify number how many common cities need to return.
  -b IS_BORN_IN_DATE_RANGE [IS_BORN_IN_DATE_RANGE ...], --is_born_in_date_range IS_BORN_IN_DATE_RANGE [IS_BORN_IN_DATE_RANGE ...]
                        Specify two dates in format YYYY-MM-DD YYYY-MM-DD.
                        Return persons ids, titles, firstnames and lastnames.

```

Examples:

`python argp.py -p women`
`python argp.py -perc man`
`python argp.py -a all`
`python argp.py --most_safety_password`
`python argp.py --most_common_cities`
`python argp.py --is_born_in_date_range 1988-11-30 1989-11-30`


## Prettier JSON

You can use this command below to make JSON easier to read: <br/>
`python -m json.tool persons.json pretty_persons.json`
