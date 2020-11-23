from passgen.picker import make_picker_generator
from passgen.dictionary import make_word_generator
from passgen.transformer import transform


def passgen(options):
    """
    Main API

    Return a generator yielding passphrases according to options.
    :param options: options (see args.py for details)
    :return: generator yielding passphrases according to options.
    """
    dictionary_words = make_word_generator(options.dictionary)
    picker = make_picker_generator(dictionary_words, options)
    while True:
        picked_words = next(picker)
        transformed_words = transform(picked_words)
        yield transformed_words
