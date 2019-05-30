from itertools import combinations


def all_sublist(lst):
    result = []
    for i in range(0, len(lst) + 1):
        result.extend([list(x) for x in list(combinations(lst, i))])

    return result


if __name__ == '__main__':
    print(all_sublist([1, 2, 3, 4]))
