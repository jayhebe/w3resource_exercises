def insert_end(char_str):
    if len(char_str) < 2:
        return char_str
    else:
        return char_str[-2:] * 4


if __name__ == '__main__':
    print(insert_end("Python"))
    print(insert_end("Exercises"))
