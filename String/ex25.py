def caesar_encryption(char_str, offset):
    new_str = ""
    for ch in char_str:
        new_str += chr(ord(ch) + offset)

    return new_str


if __name__ == '__main__':
    print(caesar_encryption("password", 3))
    print(caesar_encryption("abc", 2))
