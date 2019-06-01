original_list = [{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]
print([{key: value for key, value in item.items() if key != "key1"} for item in original_list])
