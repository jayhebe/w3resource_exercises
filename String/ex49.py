def get_vowels(char_str):
    return [ch for ch in char_str if ch in "aeiouAEIOU"]


if __name__ == '__main__':
    print(get_vowels("w3resource"))
