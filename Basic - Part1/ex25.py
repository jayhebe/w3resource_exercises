def value_in_group(group, value):
    if value in group:
        return True
    else:
        return False

    
if __name__ == '__main__':
    print(value_in_group([1, 2, 3, 4], 3))
    print(value_in_group([2, 3, 4, 5], 3))
    print(value_in_group([2, 3, 4, 5], 8))
