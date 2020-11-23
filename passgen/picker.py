import secrets

# todo: there must be a better way to do this
_choice = secrets.choice  # default is cryptographic random generator from secrets


def make_picker_generator(words, num_words=5):
    """
    Return a generator. The generator will yield a list of randomly selected
    words from the provided iterator (words).
    :param words: iterator providing words (strings)
    :param num_words: Length of the list of str yielded by the generator.
    :return: Generator yielding list of str, according to specs.
    """

    def get_generator():
        while True:
            yield [_choice(word_list) for _ in range(num_words)]

    word_list = list(words)
    return get_generator()
