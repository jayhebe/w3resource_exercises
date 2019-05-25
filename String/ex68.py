def seperate_chars(char_str):
    single_chars = []
    repeat_chars = []
    for ch in char_str:
        if char_str.count(ch) == 1:
            single_chars.append(ch)
        else:
            repeat_chars.append(ch)

    return "".join(single_chars), "".join(set(repeat_chars))


if __name__ == '__main__':
    print(seperate_chars("aabbcceffgh"))
