import argparse

DEFAULT_COUNT = 5


def get_cli_options(argv):
    parser = argparse.ArgumentParser(description='Password generator inspired by XKCD.')

    parser.add_argument('-C', '--count', action='store', metavar='COUNT',
                        type=int, default=DEFAULT_COUNT,
                        help=f'Generate COUNT passwords. Default: {DEFAULT_COUNT}.')

    return parser.parse_args(argv[1:])
