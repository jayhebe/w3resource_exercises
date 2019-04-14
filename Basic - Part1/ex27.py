def list_to_str(lst):
    result = ""
    for l in lst:
        result += l

    return result


if __name__ == '__main__':
    print(list_to_str(["hello", "world", "!"]))
