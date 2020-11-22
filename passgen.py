import itertools
import sys

from passgen import passgen
from passgen import args

if __name__ == '__main__':
    cli_options = args.get_cli_options(sys.argv)
    passwords = passgen.passgen(cli_options)
    for password in itertools.islice(passwords, cli_options.count):
        print(password)
