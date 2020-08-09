import argparse
from queries import perc_man, perc_women, most_common_cities

def positive_int(s: str) -> int:
    try:
        value = int(s)
    except ValueError:
        raise argparse.ArgumentTypeError(f'Expected integer, got {s!r}')

    if value <= 0:
        raise argparse.ArgumentTypeError(f'Expected positive integer, got {value}')

    return value

parser = argparse.ArgumentParser(description='A script that does operations with database data and returns values')
parser.add_argument('-a', '--average_age',
                    choices=['man', 'women', 'all'],
                    nargs=1,
                    default='all',
                    help='Specify whose average age: all, man or women. Defaulf: %(default)s')

parser.add_argument('-c', '--most_common_cities',
                    nargs=1,
                    type=positive_int,
                    help='Specify how many common cities')

args = parser.parse_args()


