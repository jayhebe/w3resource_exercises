def remove_duplicate_chars(char_str):
    for ch in char_str:
        if char_str.count(ch) > 1:
            char_str = char_str.replace(ch, "")

    return char_str


# from collections import OrderedDict
#
#
# def remove_duplicate_chars(str1):
#     return "".join(OrderedDict.fromkeys(str1))


if __name__ == '__main__':
    print(remove_duplicate_chars("python exercises practice solution"))
    print(remove_duplicate_chars("w3resource"))
