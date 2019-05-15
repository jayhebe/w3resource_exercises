import string


def contain_all_letters(char_str):
    for letter in string.ascii_lowercase:
        if letter not in char_str.lower():
            return False

    return True


if __name__ == '__main__':
    print(contain_all_letters("The quick brown fox jumps over the lazy dog"))
    print(contain_all_letters("The quick brown fox jumps over the lazy cat"))
