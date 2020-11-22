import argparse

DEFAULT_DICTIONARY = 'eff-long'
DEFAULT_NUMWORDS = 5
DEFAULT_COUNT = 1


def get_cli_options(argv):
    parser = argparse.ArgumentParser(description='Password generator inspired by XKCD.')

    parser.add_argument('-d', '--dictionary', action='store', metavar='DICTIONARY',
                        type=str, default=DEFAULT_DICTIONARY,
                        help=f'Specify DICTIONARY. Available options: eff-long (default).')
    parser.add_argument('-n', '--numwords', action='store', metavar='NUMWORDS',
                        type=int, default=5,
                        help=f'')
    parser.add_argument('-c', '--count', action='store', metavar='COUNT',
                        type=int, default=DEFAULT_COUNT,
                        help=f'Generate COUNT passwords. Default: {DEFAULT_COUNT}.')

    return parser.parse_args(argv[1:])
