def get_ndegrees(num):
    count = 0
    flag = True
    while flag:
        if str(pow(2, count + 1)) in num:
            count += 1
        else:
            flag = False

    return count


if __name__ == '__main__':
    print(get_ndegrees("2481632"))
    print(get_ndegrees("248163264"))
