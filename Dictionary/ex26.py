sample_data = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'},
               {'id': 3, 'success': True, 'name': 'Alex'}]
count = 0
for data in sample_data:
    if data["success"] is True:
        count += 1

print(count)
