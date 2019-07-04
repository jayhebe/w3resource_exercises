sample_data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
               {"VIII": "S007"}]
print(set([v for d in sample_data for v in d.values()]))
