from passgen.picker import make_picker_generator
from passgen.dictionary import get_words_from_dictionary
from passgen.transformer import transform


def passgen(options):
    """
    Main API

    Return a generator yielding passphrases according to options.
    :param options: options (see args.py for details)
    :return: generator yielding passphrases according to options.
    """
    all_words = get_words_from_dictionary(options.dictionary)
    picker = make_picker_generator(all_words, options.numwords)
    while True:
        picked_words = next(picker)
        transformed_words = transform(picked_words)
        yield transformed_words
