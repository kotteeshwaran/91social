sort_dict = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2',
'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print(sort_dict)
print()
sorted_dict = sorted(sort_dict, key=lambda x:x['color'])
print(sorted_dict)