def first2_last2(char_str):
    if len(char_str) < 2:
        return ""
    else:
        return char_str[:2] + char_str[-1:2:-1]


if __name__ == '__main__':
    print(first2_last2("w3resource"))
    print(first2_last2("w3"))
    print(first2_last2("w"))
