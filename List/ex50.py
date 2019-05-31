original_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
print(sorted(original_list, key=lambda x: x["key"]["subkey"], reverse=True))
