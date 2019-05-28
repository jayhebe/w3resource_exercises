from itertools import permutations


def all_permutations(lst):
    return list(permutations(lst))


if __name__ == '__main__':
    print(all_permutations(["a", "b", "c"]))
