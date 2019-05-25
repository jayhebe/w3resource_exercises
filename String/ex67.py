from itertools import groupby


def remove_all_consecutive(char_str):
    result = []
    for key, group in groupby(char_str):
        result.append(key)

    return "".join(result)


if __name__ == '__main__':
    print(remove_all_consecutive("xxxxxxxxxxxxyyyyyyyyyyyy"))
