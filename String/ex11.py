def remove_odd_chars(char_str):
    return "".join([char_str[i] for i in range(len(char_str)) if i % 2 == 0])


if __name__ == '__main__':
    print(remove_odd_chars("abcdef"))
    print(remove_odd_chars("python"))
