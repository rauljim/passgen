from unittest import TestCase
from passgen.loader import get_words_from_file


class Test(TestCase):
    def test_get_words_from_file(self):
        with self.assertRaises(FileNotFoundError):
            get_words_from_file('file_not_found.txt')
        # get_words_from_file('test_loader.py')  # file exists
        # get_words_from_file('__init__.py')  # empty file
        # get_words_from_file('../static/eff_large.txt')
