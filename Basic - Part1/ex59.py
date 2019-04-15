def calc_height(feet, inches):
    total_inches = inches + feet * 12

    return total_inches * 2.54


if __name__ == '__main__':
    print(calc_height(5, 3))
