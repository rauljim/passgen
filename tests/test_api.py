import pytest

from passgen import api, args


def test_passgen():
    password_generator = api.passgen()
    password = next(password_generator)
    words = password.split()
    assert args.DEFAULT_NUM_WORDS == len(words)


def test_empty_dictionary():
    options = args.get_default_options()
    options.min_chars = 1234567890  # no words to chose from (no dictionary word complies with this requirement)
    password_generator = api.passgen(options)
    with pytest.raises(StopIteration):
        next(password_generator)
