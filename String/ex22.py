def lexicographi_sort(char_str):
    return sorted(char_str, key=str.upper)


if __name__ == '__main__':
    print(lexicographi_sort("w3resource"))
    print(lexicographi_sort("quickbrown"))
