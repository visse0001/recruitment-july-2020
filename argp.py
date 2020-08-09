import argparse
from queries import \
    perc_man, \
    perc_women, \
    average_age_overall, \
    average_age_female, \
    most_common_cities, \
    most_safety_password, \
    is_born_in_date_range


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
                    help='Specify percent: man or women. Default: %(man)s.')

parser.add_argument('--average_age',
                    choices=['man', 'women', 'all'],
                    help='Specify average age: man, women, all.')

parser.add_argument('--most_safety_password',
                    action='store_true',
                    help='Return most safety password from database.')

parser.add_argument('-c', '--most_common_cities',
                    type=positive_int,
                    help='Specify how many common cities.')

parser.add_argument('-b', '--is_born_in_date_range',
                    type=str,
                    nargs='+',
                    help='Specify two dates in format YYYY-MM-DD YYYY-MM-DD. '
                         'Return persons ids, titles, firstnames and lastnames.')

args = parser.parse_args()

if args.perc == 'man':
    result = perc_man()
    print(result)

if args.perc == 'women':
    result = perc_women()
    print(result)

if args.average_age == 'all':
    result = average_age_overall()
    print(result)

if args.average_age == 'female':
    result = average_age_female()
    print(result)

if args.most_common_cities:
    n = args.most_common_cities
    result = most_common_cities(n)
    print(result)

if args.most_safety_password:
    result = most_safety_password()
    print(result)

if args.is_born_in_date_range:
    result = is_born_in_date_range(args.is_born_in_date_range[0], args.is_born_in_date_range[1])
    print(result)
