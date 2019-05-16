def repeated_chars(char_str):
    result = {}
    for ch in char_str:
        result.setdefault(ch, 0)
        result[ch] += 1

    return {key: value for key, value in result.items() if value >= 2}


if __name__ == '__main__':
    print(repeated_chars("thequickbrownfoxjumpsoverthelazydog"))
