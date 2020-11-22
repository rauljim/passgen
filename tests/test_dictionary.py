from unittest import TestCase
from passgen.dictionary import get_words_from_dictionary


class Test(TestCase):
    def test_get_words_from_file(self):
        get_words_from_dictionary('eff-long')
        with self.assertRaises(KeyError):
            get_words_from_dictionary('dictionary-not-found')
