# buildings = []
# count = 0
# while count != 8:
#     building = int(input("Please input the height of the building: "))
#     if building != "":
#         buildings.append(building)
#         count += 1
#     else:
#         continue
#
#
# print(sorted(buildings, reverse=True)[:3])


print("Input the heights of eight buildings:")
lst = [int(input()) for i in range(8)]
print("Heights of the top three buildings:")
lst = sorted(lst)
print(*lst[:4:-1], sep='\n')
