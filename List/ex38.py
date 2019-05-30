def change_pos(lst):
    result = []
    for i in range(0, len(lst), 2):
        result.append(lst[i + 1])
        result.append(lst[i])

    return result


if __name__ == '__main__':
    print(change_pos([0, 1, 2, 3, 4, 5]))
