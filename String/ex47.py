def lower_n_chars(char_str, n):
    return char_str[:n].lower() + char_str[n:]


if __name__ == '__main__':
    print(lower_n_chars("W3RESOURCE.COM", 4))
