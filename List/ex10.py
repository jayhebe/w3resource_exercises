def longer_than_n(lst, n):
    return [i for i in lst if len(i) > n]


if __name__ == '__main__':
    print(longer_than_n(["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 3))
