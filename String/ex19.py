def split_str(char_str, spec_char):
    return char_str.rsplit(spec_char, 1)[0]


if __name__ == '__main__':
    str1 = 'https://www.w3resource.com/python-exercises/string'
    print(split_str(str1, "/"))
    print(split_str(str1, "-"))
