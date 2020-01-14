"""
Write a Python program to get next day of a given date.
Expected Output:

Input a year: 2016
Input a month [1-12]: 08
Input a day [1-31]: 23
The next date is [yyyy-mm-dd] 2016-8-24
"""


def is_leap_year(y):
    if y % 4 == 0 and y % 100 != 0:
        return True
    return False


year = int(input("Input a year: "))
month = int(input("Input a month [1-12]: "))
day = int(input("Input a day [1-31]: "))

if month == 12 and day == 31:
    year += 1
    month = day = 1
elif month in [1, 3, 5, 7, 8, 10] and day == 31:
    month += 1
    day = 1
elif month in [4, 6, 9, 11] and day == 30:
    month += 1
    day = 1
elif month == 2:
    if is_leap_year(year) and day == 29:
        month += 1
        day = 1
    elif not is_leap_year(year) and day == 28:
        month += 1
        day = 1
else:
    day += 1

print("The next date is [yyyy-mm-dd] {}-{}-{}".format(year, month, day))
