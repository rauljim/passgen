from unittest import TestCase
from passgen.transformer import transform


class Test(TestCase):
    def test_transform_delimiter(self):
        self.assertEqual('a b c', transform(list('abc')))
        self.assertEqual('a b c', transform(list('abc'), delimiter=' '))
        self.assertEqual('a.b.c', transform(list('abc'), delimiter='.'))
        self.assertEqual('a.b.c', transform(tuple('abc'), delimiter='.'))
