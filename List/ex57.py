color1 = ["green", "orange", "black", "white"]
color2 = ["green", "green", "green", "green"]

print(list(map(lambda x: x == "green", color1)))
print(list(map(lambda x: x == "green", color2)))
print(all(x == "green" for x in color1))
print(all(x == "green" for x in color2))
