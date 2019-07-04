data = {"one": 1, "two": 2, "three": 3, "four": 1, "five": 1}
newdata = {}
# for k, v in data.items():
#     if not list(data.values()).count(v) > 1:
#         newdata[k] = v
#
# print(newdata)
for k, v in data.items():
    if v not in newdata.values():
        newdata[k] = v

print(newdata)
