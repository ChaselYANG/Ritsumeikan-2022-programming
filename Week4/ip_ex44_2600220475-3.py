#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Author：YNAG Minxu
Student ID：26002204753
Program description:Add List 1 and List 2 one by one until the sum appears to be greater than 25.

"""

number_list_1 = [1,2,3,4,5,6,7,8,9,10,11]
number_list_2 = [10,11,12,13,14,15,16,17,18,19,20]

print("Length of the first list:", len(number_list_1))
print("Length of the second list:", len(number_list_2))
for number_1,number_2 in zip(number_list_1 , number_list_2):
    summa = (number_1 + number_2)
    print("The sum is" ,summa)
    if summa > 25:
        break
        