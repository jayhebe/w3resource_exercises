def near_thousand(n):
    if abs(1000 - n) < 100 or abs(2000 - n) < 100:
        return True
    else:
        return False


if __name__ == '__main__':
    print(near_thousand(999))
    print(near_thousand(99))
    print(near_thousand(998))
    print(near_thousand(1911))
