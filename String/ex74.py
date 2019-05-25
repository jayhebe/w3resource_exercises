def contain_str(char_str1, char_str2):
    indexes = []
    for ch in char_str2:
        indexes.append(char_str1.index(ch))

    return char_str1[min(indexes):max(indexes) + 1]


if __name__ == '__main__':
    print(contain_str("PRWSOERIUSFK", "OSU"))
