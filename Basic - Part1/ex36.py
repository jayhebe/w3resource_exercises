def add_int(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return "Bad params!"


if __name__ == '__main__':
    print(add_int(3, 5))
    print(add_int(3, "hahaha"))
