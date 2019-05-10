def remove_char(char_str, n):
    list_str = list(char_str)
    list_str.remove(char_str[n])
    return "".join(list_str)


if __name__ == '__main__':
    print(remove_char("python", 0))
    print(remove_char('Python', 3))
    print(remove_char('Python', 5))
