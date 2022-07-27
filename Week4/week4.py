#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author：YANG Minxu
Student ID：26002204753
Program description:

"""

# number = 4
# if number < 10:
#     print(number, 'is less than 10')

# if number < 10 and number*2 > 7:
#     print(number, 'is less than 10 and and multiplying it by 2 results in more than 7')

# number = 10

# if number > 100:
#     print('number is greater than 100')
# elif number == 50:
#     print('number is 50')
# elif number < 20:
#     print('number is less than 20')
# else:
#     print('all above evaluated False')

# number = 17
# if number >= 0:
#     if number == 0:
#         print('zero')
#     else:
#         print('positive')
# else:
#     print('negative')

scientist_list = ['Einstein', 'Curie', 'Newton']
dob_list = [1879, 1867, 1643]
for scientist, dob in zip(scientist_list, dob_list):
    # print(scientist, 'was born in', dob)
    # print("{} was born in {}".format(scientist, dob))
    print(f"{scientist} was born in {dob}")

# scientist_list = ['Einstein', 'Curie', 'Newton']
# for index, scientist in enumerate(scientist_list):
#     print(index, scientist)

# scientist_list = ['Einstein', 'Curie', 'Newton', 'Darwin', 'Tesla', 'Galilei', 'Lovelace']
# for s in scientist_list:
#     if s == 'Tesla':
#         break
#     print(s)
# print("loop ended")

# number_list = [1, 4, 6, 33, 78, 99, 3, 150, 12, 1]
# for n in number_list:
#     if n == 99:
#         continue
#     print(n)
# print("loop ended")

# n = 10
# while n > 0:
#     n += 2
#     if n == 30:
#         break
#     print(n)
# print("loop ended")