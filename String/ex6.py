def add_suffix(char_str):
    if len(char_str) < 3:
        return char_str

    if char_str.endswith("ing"):
        return char_str + "ly"

    return char_str + "ing"


if __name__ == '__main__':
    print(add_suffix("abc"))
    print(add_suffix("string"))
    print(add_suffix("s"))
