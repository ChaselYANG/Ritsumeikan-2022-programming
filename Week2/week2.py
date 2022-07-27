#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author：YANG Minxu
Student ID：26002204753
Program description:
    
"""

print(3*2+6)

age = 32
half_age = age/2
print(age)
print(half_age)

a, b, c = 1, 2, 3
print(a*b*c)

# variable "a" is integer 3
a = int(3)
print(a)
print(type(a))

# variable "a" is float 4.2
a = float(4.2)
print(a)
print(type(a))

# variable "b" is actually 3.0
b = float(3)
print(b)
print(type(b))

# logical operators
a, b, c = 10, 15, 20
print(a < b)
print(not a < 15 and c != b)


string_1 = 'holds a string'
string_2 = "this is also correct"
string_3 = 'Leibniz\'s law of continuity'
string_4 = "Pascal's calculator" 
print(string_1)
print(string_2)
print(string_3)
print(string_4)

# string indexing
print(string_1[0])
print(string_1[3])

#string concatenation
my_string_1 = "Introduction"
my_string_2 = "Programming"
print(my_string_1 + ' ' + 'to ' + my_string_2)

#printing length of string
print(len('Newton'))
print(len("12345"))

# Capitalize
my_string = "programming"
print(my_string.capitalize())

# .format() method
print('there are {} students in the class.'.format('49'))

no_students = 49
class_name = "Introduction to Programming"
print('There are {} students in the {} class.'.format(no_students, class_name))