def poor_to_good(char_str):
    if "not" in char_str and "poor" in char_str and char_str.index("not") < char_str.index("poor"):
        return char_str.replace(char_str[char_str.index("not"):char_str.index("poor") + 4], "good")
    else:
        return char_str


if __name__ == '__main__':
    print(poor_to_good("The lyrics is not that poor!"))
    print(poor_to_good("The lyrics is poor!"))
