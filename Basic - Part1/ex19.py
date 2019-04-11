def add_str(s):
    if s.startswith("Is"):
        return s
    else:
        return "Is" + s


if __name__ == '__main__':
    print(add_str("Island"))
    print(add_str("shot"))
    print(add_str("hehehe"))
