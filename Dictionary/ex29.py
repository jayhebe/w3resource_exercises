student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
new_list = {}
for k, v in student_list.items():
    new_list[k.replace(" ", "")] = v

print(new_list)
