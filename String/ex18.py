def first_three(char_str):
    if len(char_str) < 3:
        return char_str
    else:
        return char_str[:3]


if __name__ == '__main__':
    print(first_three("ipy"))
    print(first_three("python"))
