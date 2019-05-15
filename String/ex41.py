def strip_str(char_str, characters):
    return "".join([ch for ch in char_str if ch not in characters])


if __name__ == '__main__':
    print(strip_str("The quick brown fox jumps over the lazy dog.", "aeiou"))
