from unittest import TestCase

from passgen import api, args

DEFAULT_OPTIONS = args.get_cli_options([])

class Test(TestCase):
    def test_passgen(self):
        password_generator = api.passgen(DEFAULT_OPTIONS)
        password = next(password_generator)
        words = password.split()
        assert 5 == len(words)
