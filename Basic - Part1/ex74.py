import hashlib


def hash_word(word):
    return hashlib.md5(word.encode()).hexdigest()


if __name__ == '__main__':
    print(hash_word("123456"))
