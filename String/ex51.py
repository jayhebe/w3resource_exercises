def non_repeated_chars(char_str):
    for ch in char_str:
        if char_str.count(ch) == 1:
            return ch
    return None


if __name__ == '__main__':
    print(non_repeated_chars("thequickbrownfoxjumpsoverthelazydog"))
    print(non_repeated_chars("abcdef"))
    print(non_repeated_chars("abcabcdef"))
    print(non_repeated_chars("aabbcc"))
