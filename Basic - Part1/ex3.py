import datetime


def print_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    print("%s: Log started" % print_time())
    print("%s: Log stopped" % print_time())
