DICTIONARIES = {
    'eff-long',  # https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt
}

def get_words_from_dictionary(dictionary):
    if dictionary in DICTIONARIES:
        filename = f'dictionaries/{dictionary}.txt'
    else:
        raise KeyError(f'Dictionary does not exist: {dictionary}')
    with open(filename) as f:
        return [line.strip() for line in f]
