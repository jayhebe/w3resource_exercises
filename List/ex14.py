def remove_even_number(num_lst):
    return [num for num in num_lst if num % 2 == 1]


if __name__ == '__main__':
    print(remove_even_number([7, 8, 120, 25, 44, 20, 27]))
