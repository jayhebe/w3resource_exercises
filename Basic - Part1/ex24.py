def is_vowel(letter):
    if letter in "aeuio":
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_vowel("c"))
    print(is_vowel("e"))
    print(is_vowel("i"))
