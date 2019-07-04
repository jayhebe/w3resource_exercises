def is_dict_empty(d):
    # if len(d) == 0:
    #     return True
    # else:
    #     return False
    if not bool(d):
        return True
    else:
        return False


d1 = {}
d2 = {'data1': 100, 'data2': -54, 'data3': 247}
print(is_dict_empty(d1))
print(is_dict_empty(d2))
