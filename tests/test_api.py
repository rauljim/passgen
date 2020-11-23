from unittest import TestCase

from passgen import api, args


class Test(TestCase):
    def test_passgen(self):
        password_generator = api.passgen()
        password = next(password_generator)
        words = password.split()
        assert args.DEFAULT_NUM_WORDS == len(words)

    def test_empty_dictionary(self):
        options = args.get_default_options()
        options.min_chars = 1234567890  # no words to chose from (no dictionary word complies with this requirement)
        password_generator = api.passgen(options)
        with self.assertRaises(StopIteration):
            next(password_generator)
