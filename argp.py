import argparse
from queries import perc_man, perc_women, average_age_overall, average_age_female, most_common_cities


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
                    default='man',
                    help='Specify percent: man or women. Default: %(man)s.')

parser.add_argument('--average_age',
                    choices=['man', 'women', 'all'],
                    # default='all',
                    help='Specify average age: man, women, all. Default: %(all)s.')

parser.add_argument('-c', '--most_common_cities',
                    nargs=1,
                    type=positive_int,
                    help='Specify how many common cities.')

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

