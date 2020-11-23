from passgen import args
from passgen.picker import make_picker_generator
from passgen.dictionary import make_word_generator
from passgen.transformer import transform


def passgen(options=None):
    """
    Main API

    Return a generator yielding passphrases according to options.
    :param options: options (see args.py for details)
    :return: generator yielding passphrases according to options.
    """
    if options is None:
        options = args.get_default_options()
    dictionary_words = make_word_generator(options.dictionary)
    picker = make_picker_generator(dictionary_words, options)
    for picked_words in picker:
        transformed_words = transform(picked_words)
        yield transformed_words
