from unittest import TestCase
from passgen.dictionary import make_word_generator


class Test(TestCase):
    def test_get_words_from_dictionary(self):
        words = make_word_generator('eff-long')
        # check it's an iterator
        _ = next(words)
        # it is a generator (not a sequence)
        with self.assertRaises(TypeError):
            print(len(words))

    def test_dictionary_not_found(self):
        with self.assertRaises(KeyError):
            _ = make_word_generator('dictionary-not-found')
