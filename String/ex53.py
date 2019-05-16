def first_repeat(char_str):
    for ch in char_str:
        if char_str.count(ch) > 1:
            return ch
    return None


if __name__ == '__main__':
    print(first_repeat("abcdabcd"))
    print(first_repeat("abcd"))
