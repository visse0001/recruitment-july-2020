import argparse

from db_conn import get_session
from argparse_queries_to_db import \
    perc_man, \
    perc_women, \
    average_age_overall, \
    most_common_cities, \
    most_safety_password, \
    is_born_in_date_range, \
    average_age_female_or_man


def positive_int(s: str) -> int:
    try:
        value = int(s)
    except ValueError:
        raise argparse.ArgumentTypeError(f'Expected integer, got {s!r}')

    if value <= 0:
        raise argparse.ArgumentTypeError(f'Expected positive integer, got {value}')

    return value


parser = argparse.ArgumentParser(description='A script that does operations with database data and returns values')
parser.add_argument('-p', '--perc',
                    choices=['man', 'women'],
                    help='Specify percent: man or women.')

parser.add_argument('-a', '--average_age',
                    choices=['all', 'women', 'man'],
                    help='Return average age for all.')

parser.add_argument('-m', '--most_safety_password',
                    action='store_true',
                    help='Return most safety password from database.')

parser.add_argument('-c', '--most_common_cities',
                    type=positive_int,
                    help='Specify number how many common cities need to return.')

parser.add_argument('-b', '--is_born_in_date_range',
                    type=str,
                    nargs='+',
                    help='Specify two dates in format YYYY-MM-DD YYYY-MM-DD. '
                         'Return persons ids, titles, firstnames and lastnames.')

args = parser.parse_args()

session = get_session()

if args.perc == 'man':
    result = perc_man(session)
    print(f"The percentage of men in the base {result}%")

if args.perc == 'women':
    result = perc_women(session)
    print(f"The percentage of women in the base {result}%")

if args.average_age == 'all':
    result = average_age_overall(session)
    print(f"The average age overall: {result}.")

if args.average_age == 'women':
    result = average_age_female_or_man('female', session)
    print(f"The average age of {args.average_age} is {result}.")

if args.average_age == 'man':
    result = average_age_female_or_man('male', session)
    print(f"The average age of {args.average_age} is {result}.")

if args.most_common_cities:
    n = args.most_common_cities
    result = most_common_cities(n, session)
    print(f"Most common cities are: {result}")

if args.most_safety_password:
    result = most_safety_password(session)
    print(f"Most safe password and sum of points from database are for example: {result}")

if args.is_born_in_date_range:
    from_date = args.is_born_in_date_range[0]
    to_date = args.is_born_in_date_range[1]
    result = is_born_in_date_range(from_date, to_date, session)
    print(f"People that was born between dates are: {result}")

session.close()