def exchange_chars(char_str):
    return char_str[-1] + char_str[1:-1] + char_str[0]


if __name__ == '__main__':
    print(exchange_chars("abcd"))
    print(exchange_chars("12345"))
