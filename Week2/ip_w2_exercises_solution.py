#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: student name
Student ID: student id number
Program description: Practicing variable assignment, type checking, operators, and string methods
"""
#assign three variables to numbers 10, 20, and 31, and use operators to get their average, and
#print the result
num_1 = 10
num_2 = 20
num_3 = 31
average = (num_1 + num_2 + num_3)/3
print(average)
# print the the data type of variable average
print(type(average))
#using comparison operators, change the following statement into
#False at least 2 different ways
print(num_1 < num_2)
print(num_1 > num_2)
print(num_1 == num_2)

#assign the following string to a variable and print it: I don't know much about programming yet.
string_0 = "I don't know much about programming yet."
print(string_0)
#complete the following print function so the string reads: The 4th character is "o".
#bonus: use string indexing of string_0 to access the 4th character in the print function!
print('The 4th character is "' + string_0[3] + '"')
#print the length of the following string
my_string = "apples"
print(len(my_string))
#use the format method after the dot to insert the words 'inventor' and 'mechanical engineer'
#into the string
print("Nikola Tesla was a Serbian-American {}, electrical engineer, {}".format('inventor', 'mechanical engieer'))