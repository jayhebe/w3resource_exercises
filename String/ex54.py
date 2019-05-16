def first_repeat_smallest_index(char_str):
    result = {}
    for ch in char_str:
        if ch in result:
            return ch
        else:
            result[ch] = 0
    return None


if __name__ == '__main__':
    print(first_repeat_smallest_index("abcabc"))
    print(first_repeat_smallest_index("abbcabc"))
    print(first_repeat_smallest_index("abcbabc"))
    print(first_repeat_smallest_index("abcxxy"))
    print(first_repeat_smallest_index("abc"))
