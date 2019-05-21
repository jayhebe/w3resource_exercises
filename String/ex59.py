def max_char(char_str):
    result = {}
    for ch in char_str:
        result.setdefault(ch, 0)
        result[ch] += 1

    return sorted(result.items(), key=lambda obj: obj[1], reverse=True)[0]


if __name__ == '__main__':
    print(max_char("Python: Get file creation and modification date/times"))
    print(max_char("abcdefghijkb"))
