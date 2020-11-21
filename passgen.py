from passgen import passgen

NUM_PASSWORDS_DEFAULT = 5

if __name__ == '__main__':
    for password, _ in zip(passgen.passgen(), range(NUM_PASSWORDS_DEFAULT)):
        print(password)
