def cap_first_last(char_str):
    result = []
    words = char_str.split()
    for word in words:
        result.append(word[0].upper() + word[1:-1] + word[-1].upper())

    return " ".join(result)


if __name__ == '__main__':
    print(cap_first_last("python exercises practice solution"))
    print(cap_first_last("w3resource"))
