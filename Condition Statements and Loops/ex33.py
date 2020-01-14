"""
Write a Python program to convert month name to a number of days.
Expected Output:

List of months: January, February, March, April, May, June, July, August
, September, October, November, December
Input the name of Month: February
No. of days: 28/29 days
"""

month = input("Input the name of Month: ")

if month == "February":
    print("28/29 days")
elif month in ["January", "March", "May", "July", "August", "October", "December"]:
    print("31 days")
elif month in ["April", "June", "September", "November"]:
    print("30 days")
else:
    print("Wrong month")
