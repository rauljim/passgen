from unittest import TestCase

from passgen import passgen


class Test(TestCase):
    def test_passgen(self):
        password_generator = passgen.passgen()
        password = next(password_generator)
        words = password.split()
        assert 5 == len(words)
