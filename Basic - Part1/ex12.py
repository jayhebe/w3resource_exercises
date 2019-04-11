import calendar


def print_month_calendar(year, month):
    print(calendar.month(year, month))


if __name__ == '__main__':
    y, m = input("Please enter the year and month: ").split(",")
    print_month_calendar(int(y), int(m))
