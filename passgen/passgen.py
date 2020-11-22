from passgen.picker import Picker
from passgen.dictionary import get_words_from_dictionary
from passgen.transformer import transform


def passgen(options):
    all_words = get_words_from_dictionary(options.dictionary)
    picker = Picker(all_words, options.numwords)
    while True:
        picked_words = picker.pick()
        transformed_words = transform(picked_words)
        yield transformed_words
