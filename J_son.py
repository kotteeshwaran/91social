import json

dict_key = {}
number = int(input("Enter the number of values to be inserted:"))
for x in range(number):
    key = input("Enter the key {}:".format(x))
    value = input("Enter the value {}:".format(x))
    dict_key[key] = value
print(json.dumps(dict_key,sort_keys=True,indent=4))