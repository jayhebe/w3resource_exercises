from itertools import product


def all_permutations(char_str, number):
    result = []
    chars = list(char_str)
    for ch in product(chars, repeat=number):
        result.append(ch)
    return result


if __name__ == '__main__':
    print(all_permutations('xyz', 3))
    print(all_permutations('xyz', 2))
    print(all_permutations('abcd', 4))
