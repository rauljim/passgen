from passgen.picker import Picker
from passgen.loader import get_words_from_file
from passgen.transformer import transform

NUM_WORDS_DEFAULT = 5
WORDS_FILE_DEFAULT = 'static/eff_large.txt'  # https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt


def passgen():
    all_words = get_words_from_file(WORDS_FILE_DEFAULT)
    picker = Picker(all_words, NUM_WORDS_DEFAULT)
    while True:
        picked_words = picker.pick()
        transformed_words = transform(picked_words)
        yield transformed_words
