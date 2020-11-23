import secrets

# todo: there must be a better way to do this
from passgen import args

_choice = secrets.choice  # default is cryptographic random generator from secrets


def make_picker_generator(words, options=None):
    """
    Return a generator. The generator will yield a list of randomly selected
    words from the provided iterator (words).
    :param words: iterator providing words (strings)
    :param options: options (see args.py)
    :return: Generator yielding list of str, according to specs.
    """
    def get_generator():
        while True:
            yield [_choice(word_list) for _ in range(options.num_words)]

    if options is None:
        options = args.get_default_options()
    word_list = []
    for word in words:
        if options.min_chars <= len(word) <= options.max_chars:
            word_list.append(word)
    return get_generator()
