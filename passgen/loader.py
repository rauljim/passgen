def get_words_from_file(filename):
    with open(filename) as f:
        return [line.strip() for line in f]
