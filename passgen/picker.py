import secrets


#todo: convert the whole thing into a generator
class Picker:
    """
    Picker keeps a copy of the words provided. Randomly selected words
    can be retrieved via pick().
    """
    __choice = secrets.choice  # default is cryptographic random generator from secrets

    def __init__(self, words, num_words=5):
        """
        Build a Picker containing the words provided.
        :param words: iterable containing a list of words
        :param num_words: number of words to be retrieved.
        """
        self.words = list(words)  # keep a copy
        self.num_words = num_words

    def pick(self):
        """"
        Return a list of words randomly selected, following the options
        specified in the constructor.
        """
        return [self.__choice(self.words) for _ in range(self.num_words)]
