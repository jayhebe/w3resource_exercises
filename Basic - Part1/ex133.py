# import datetime
#
#
# start_time = datetime.datetime.now()
#
# for _ in range(100000):
#     pass
#
# end_time = datetime.datetime.now()
# print(end_time - start_time)


from timeit import default_timer


def timer(n):
    start = default_timer()
    # some code here
    for row in range(0, n):
        print(row)
    print(default_timer() - start)


timer(5)
timer(15)
