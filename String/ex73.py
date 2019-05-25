import string


def count_values(char_str):
    uppercase = 0
    lowercase = 0
    special = 0
    numeric = 0

    for ch in char_str:
        if ch in string.ascii_uppercase:
            uppercase += 1
        if ch in string.ascii_lowercase:
            lowercase += 1
        if ch in string.digits:
            numeric += 1
        if ch in string.punctuation:
            special += 1

    return uppercase, lowercase, special, numeric


if __name__ == '__main__':
    print(count_values("@W3Resource.Com"))
