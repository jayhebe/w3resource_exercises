def sum_digits(char_str):
    result = 0
    for ch in char_str:
        if ch.isdigit():
            result += int(ch)

    return result


if __name__ == '__main__':
    print(sum_digits("123abcd45"))
    print(sum_digits("abcd1234"))
