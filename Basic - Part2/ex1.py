# def diff_nums(num_list):
#     for num in num_list:
#         if num_list.count(num) > 1:
#             return False
#     return True


def diff_nums(num_list):
    if len(num_list) == len(set(num_list)):
        return True
    else:
        return False


if __name__ == '__main__':
    nums = input("Please enter numbers: ").split()
    print(diff_nums(nums))
