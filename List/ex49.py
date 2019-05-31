colors = ["Black", "Red", "Maroon", "Yellow"]
color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]

result = []
for color, code in zip(colors, color_codes):
    result.append({"color_name": color, "color_code": code})

print(result)
