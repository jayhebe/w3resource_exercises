def convert_to_upper(char_str):
    upper_char = [ch for ch in char_str[:4] if ch.isupper()]
    if len(upper_char) >= 2:
        return char_str.upper()
    else:
        return char_str


if __name__ == '__main__':
    print(convert_to_upper("Python"))
    print(convert_to_upper("PyThon"))
