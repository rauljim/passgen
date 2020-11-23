DICTIONARIES = {
    'eff-long',  # https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt
}


def make_word_generator(dictionary):
    """
    Return a generator yielding words from dictionary. Dictionary
    must be one of the currently available (see DICTIONARIES).
    :param dictionary: string indicating what dictionary to use.
    :return: generator yielding words from dictionary.
    """
    def get_generator():
        with open(filename) as f:
            for line in f:
                yield line.strip()

    if dictionary in DICTIONARIES:
        filename = f'dictionaries/{dictionary}.txt'
    else:
        raise KeyError(f'Dictionary does not exist: {dictionary}')
    # Notice that if 'yield' was here KeyError would be raised
    # upon a call to next() due to lazy evaluation.
    # What we want is that the check is done immediately.
    return get_generator()
