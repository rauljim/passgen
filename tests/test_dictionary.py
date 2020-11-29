import pytest

from passgen.dictionary import make_word_generator


def test_get_words_from_dictionary():
    words = make_word_generator('eff-long')
    # check it's an iterator
    _ = next(words)
    # it is a generator (not a sequence)
    with pytest.raises(TypeError):
        print(len(words))


def test_dictionary_not_found():
    with pytest.raises(KeyError):
        _ = make_word_generator('dictionary-not-found')
