import secrets


class Picker:
    __choice = secrets.choice  # default is cryptographic random generator from secrets

    def __init__(self, sequence, num_words=5):
        self.words = list(sequence)  # keep a copy
        self.num_words = num_words

    def pick(self):
        return [self.__choice(self.words) for _ in range(self.num_words)]
