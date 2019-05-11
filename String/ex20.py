def reverse_str(char_str):
    if len(char_str) % 4 == 0:
        return char_str[::-1]
    return char_str


if __name__ == '__main__':
    print(reverse_str("hello"))
    print(reverse_str("This is a test.."))
