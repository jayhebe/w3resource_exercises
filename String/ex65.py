def common_chars(char_str1, char_str2):
    result = []
    for ch in char_str1:
        if ch in char_str2:
            result.append(ch)

    if len(result) != 0:
        return sorted(result)
    else:
        return "No common characters"


if __name__ == '__main__':
    print(common_chars("Python", "PHP"))
    print(common_chars("Java", "PHP"))
    print(common_chars("abcde", "cdefg"))
