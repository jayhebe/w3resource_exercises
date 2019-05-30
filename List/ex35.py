from itertools import product


def concatenate(lst1, n):
    # return [x[0] + str(x[1]) for x in sorted(list(product(lst1, list(range(1, n + 1)))), key=lambda t: t[1])]
    result = []
    for i in range(1, n + 1):
        for j in lst1:
            result.append(j + str(i))

    return result


if __name__ == '__main__':
    print(concatenate(['p', 'q'], 5))
