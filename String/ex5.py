def swap_chars(str1, str2):
    return (str1[:2] + str2[2:]) + " " + (str2[:2] + str1[2:])


if __name__ == '__main__':
    print(swap_chars("xyz", "abc"))
