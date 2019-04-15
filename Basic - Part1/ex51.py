import cProfile


def get_sum():
    print(2 + 1)


print(cProfile.run("get_sum()"))
