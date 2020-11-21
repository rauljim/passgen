from passgen import passgen
from passgen import args

if __name__ == '__main__':
    cli_options = args.get_cli_options()
    for password, _ in zip(passgen.passgen(), range(cli_options.count)):
        print(password)
