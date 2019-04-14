def copy_str(s, n):
    if len(s) < 2:
        return s * n
    else:
        return s[:2] * n


if __name__ == '__main__':
    print(copy_str("a", 3))
    print(copy_str("hello", 4))
    print(copy_str("nice", 5))
