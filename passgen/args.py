import argparse

DEFAULT_DICTIONARY = 'eff-long'
DEFAULT_NUM_WORDS = 5
DEFAULT_COUNT = 1
DEFAULT_MIN_CHARS = 1
DEFAULT_MAX_CHARS = 2 ** 15  # that should be large enough (even for hyper-long compounded words) :-)


def get_cli_options(argv=None):
    parser = argparse.ArgumentParser(description='Password generator inspired by XKCD.')

    parser.add_argument('-d', '--dictionary', action='store', metavar='DICTIONARY',
                        type=str, default=DEFAULT_DICTIONARY,
                        help=f'Specify DICTIONARY. Available options: eff-long (default).')
    parser.add_argument('-n', '--num-words', action='store', metavar='NUM_WORDS',
                        type=int, default=5,
                        help=f'')
    parser.add_argument('-c', '--count', action='store', metavar='COUNT',
                        type=int, default=DEFAULT_COUNT,
                        help=f'Generate COUNT passwords. Default: {DEFAULT_COUNT}.')
    parser.add_argument('--min-chars', action='store', metavar='MIN_CHARS',
                        type=int, default=DEFAULT_MIN_CHARS,
                        help=f'Consider only words containing a minimum of MIN_CHARS. Default: {DEFAULT_MIN_CHARS}')
    parser.add_argument('--max-chars', action='store', metavar='MAX_CHARS',
                        type=int, default=DEFAULT_MAX_CHARS,
                        help=f'Consider only words containing a maximum of MAX_CHARS. Default: no limit')

    if argv is not None and len(argv) > 0:
        argv = argv[1:]  # parse_args doesn't want first arg (program name)
    options = parser.parse_args(argv)

    if options.count < 0:  # --count 0 is noop
        print(f'WARING: ignoring negative --count.')  # todo: maybe this can be done in the parser?
        options.count = DEFAULT_COUNT
    if options.max_chars < options.min_chars:
        print(f'WARNING: ignoring --max-chars: max-chars ({options.max_chars}) < min-chars ({options.min_chars})')
        options.max_chars = DEFAULT_MAX_CHARS
    return options


def get_default_options():
    return get_cli_options([])
