def character_freq(char_str):
    char_freq = {}
    for ch in char_str:
        char_freq.setdefault(ch, 0)
        char_freq[ch] += 1

    return char_freq


if __name__ == '__main__':
    print(character_freq("google.com"))
    print(character_freq("hello, world"))
