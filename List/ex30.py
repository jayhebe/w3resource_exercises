def element_freq(lst):
    result = {}
    for item in lst:
        result.setdefault(item, 0)
        result[item] += 1

    return result


if __name__ == '__main__':
    print(element_freq([10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]))
