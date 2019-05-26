def remove_045(lst):
    return [x for i, x in enumerate(lst) if i not in (0, 4, 5)]


if __name__ == '__main__':
    print(remove_045(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))
