#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author：YANG Minxu
Student ID：26002204753
Program description:

"""

# our_list = ['Pythagoras', 427, 'Plato', ['apple', 'a plum', 3], True, 'Aristotle']
# print('Our list:', our_list)
# print('The first element in the list container is:', our_list[0])
# print('Type of second element is:', type(our_list[1]))
# print('The length of out list is:', len(our_list))
# print('Length of "Pythagoras" is:', len('our_list[0]'))

# print('List inside our list:', our_list[3])
# print('Type of list inside our list:', type(our_list[3]))
# print('Length of list inside our list:', len(our_list[3]))
# print('The first element in the list inside our list is:', our_list[3][0])
# print('The second element in the list inside our list is:', our_list[3][1])
# print(type(our_list[3][0]))

# for element in our_list:
#     print(type(element))

# print('The last element in the list is:', our_list[-1])
# print('The third to last element in the list is:', our_list[-3])

# print('The first two elements from our_list are:', our_list[0:2])
# print('With notation index 3 to 5:', our_list[3:5])
# our_new_list = our_list[1:4]
# print('Our new list:', our_new_list)

# print(our_new_list[1:2])
# print(our_new_list[:2])
# print(our_new_list[1:])

# my_list2 = [1, True, 'three', 4.5]
# print('My list 2:', my_list2)
# my_list2[2] = 'four'
# print('My list 2:', my_list2)
# my_list2[2] = '4'
# print('My list 2:', my_list2)

# my_list2[2][0] = 'a'

# another_list = ['B', 'This is a sentence.', '459', ['B', 'C', 127.45]]
# for element in another_list:
#     if 'This' in element:
#         print('Part 1:',element)

# for element in another_list:
#     if 'B' in element:
#         print('Part 2:',element)

scientist_dict = {
    'Da Vinci': 1452,
    'Galilei': 1564,
    'Newton': 1642,
}

# print(len(scientist_dict))

random_dict = {
    23: 'abcd',
    14.678: 34,
    'abc': [1,2,3]
}

# print(scientist_dict['Galilei'])

scientist_dict['Da Vinci'] = 1519
# print(scientist_dict)

scientist_dict['Darwin'] = 1809
# print(scientist_dict)

print("Is the key 'Newton' in the dictionary?", 'Newton' in scientist_dict)

# for name in scientist_dict:
#     print(name)

# for name in scientist_dict.keys():
#     print(name)

# for date in scientist_dict.values():
#     print(date)

for name, date in scientist_dict.items():
    print('The name of the scientist:', name, ', Corresponding date:', date)

gpu_dict = {
    "Nvidia": {
        "GPU": "3090 TI",
        "MSRP": False,
        "Launch year": 2022,
        "Manufacturer": ["Gigabyte", "MSI", "Zotac"]},
    "AMD": {
        "GPU": "RX 6800 XT",
        "MSRP": False,
        "Launch year": 2020,
        "Manufacturer": ["AMD", "Asrock"]}
}

print("Printing the value for the key 'Nvidia'")
print(gpu_dict['Nvidia'])
print("Printing the value for the key 'AMD'")
print(gpu_dict['AMD'])
print("Manufacturers for Nvidia:")
# print(gpu_dict['Nvidia']['Manufacturer'])
for manufacturer in gpu_dict['Nvidia']['Manufacturer']:
    print(manufacturer)
