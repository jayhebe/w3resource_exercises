import pprint


file_name = "testfile.txt"

with open(file_name, encoding="utf-8") as fp:
    file_content = fp.readlines()

file_content = "".join(file_content)

character_dict = dict()
for ch in file_content:
    character_dict.setdefault(ch, 0)
    character_dict[ch] += 1

pprint.pprint(character_dict)
