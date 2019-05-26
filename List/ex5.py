def same_first_last(lst):
    count = 0
    for item in lst:
        if len(item) < 2:
            continue
        else:
            if item[0] == item[-1]:
                count += 1

    return count


if __name__ == '__main__':
    print(same_first_last(['abc', 'xyz', 'aba', '1221']))
