def number_of_substrings(str1):
    str_len = len(str1)
    return int(str_len * (str_len + 1) / 2)


str2 = input("Input a string: ")
print("Number of substrings:")
print(number_of_substrings(str2))
