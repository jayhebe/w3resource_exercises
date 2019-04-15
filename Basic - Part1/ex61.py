"""
1 foot = 12 inches
1 yard = 3 feet
1 yard = 36 inches
1 mile = 1760 yards
1 mile = 5280 feet
"""

d_ft = int(input("Input distance in feet: "))
d_inches = d_ft * 12
d_yards = d_ft / 3.0
d_miles = d_ft / 5280.0

print("The distance in inches is %i inches." % d_inches)
print("The distance in yards is %.2f yards." % d_yards)
print("The distance in miles is %.2f miles." % d_miles)
