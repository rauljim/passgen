from unittest import TestCase

from passgen import passgen, args

DEFAULT_OPTIONS = args.get_cli_options([])

class Test(TestCase):
    def test_passgen(self):
        password_generator = passgen.passgen(DEFAULT_OPTIONS)
        password = next(password_generator)
        words = password.split()
        assert 5 == len(words)
