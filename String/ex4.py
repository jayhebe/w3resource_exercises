def replace_first_char(char_str):
    return char_str[0] + char_str[1:].replace(char_str[0], "$")


if __name__ == '__main__':
    print(replace_first_char("restart"))
    print(replace_first_char("abracadabra"))
