"""
Write a Python program to filter a given list whether the values in the list are having length of 6 using Lambda.
"""

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = filter(lambda day: day if len(day) == 6 else '', weekdays)
for d in days:
    print(d)
