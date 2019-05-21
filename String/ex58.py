def remove_spaces_to_front(char_str):
    return " " * char_str.count(" ") + char_str.replace(" ", "")


if __name__ == '__main__':
    print(remove_spaces_to_front("w3resource .  com  "))
    print(remove_spaces_to_front("   w3resource.com  "))
