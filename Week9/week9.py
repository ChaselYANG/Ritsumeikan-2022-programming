#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author：YANG Minxu
Student ID：26002204753
Program description:
    
"""

# from telnetlib import OUTMRK


# def return_number():
#     return 5

# print("Calling the function:", return_number())
# print("Calling the function and multiplying the return value by 6:", return_number() * 6)
# x = return_number()
# y = x**2
# print(y)

# def multiply(x, y):
#     z = x * y

# our_value = multiply(3, 4)
# print(our_value)

# def operation(x, y):
#     z = x*y
#     n = y**2
#     return z, n

# number_1, number_2 = operation(3, 4)
# print(number_1)
# print(number_2)

# def is_even(n):
#     if n % 2 == 0:
#         return print("The number is even")
#     else:
#         return print("The number is odd")

# is_even(41)
# is_even(42)                         

# def is_divisible(x, y):
#     if x % y == 0 :
#         return True
#     return False

# boolean = is_divisible(4, 2)
# print(boolean)

# def f():
#     n = 5
#     return n*2

# print("Calling function f and printing the return value:", f())
# # print(n) won't print as it is not defined

# def function_f():
#     n = 5
#     print(n)

# def function_g():
#     n = "Just a string"
#     print(n)

# print("Calling function_f:")
# function_f()
# print("Calling function_g:")
# function_g()

# x = 7

# def function_f(y):
#     x = 3
#     return (y*3)
# print("Calling function_f and printing the return value:", function_f(3))
# print(x)

# n = 0
# def add(x):
#     n += x

# add(3)

# n = 5555
# print(id(n))
# n += 3
# print(id(n))

# my_list = ['oranges', 'grapes']
# print("Original list:", my_list)
# print(id(my_list))
# my_list.append('apples')
# print("List is modified by adding a new element to it:", my_list)
# print(id(my_list))

# my_list = ['oranges', 'grapes']
# print("Original list:", my_list)

# def modify_list(elem, remove_index):
#     my_list.append(elem)
#     my_list.pop(remove_index)

# modify_list('apples', 1)
# print("List is modified by adding a new element to it:", my_list)

# my_list = ['oranges', 'grapes']
# print("Original list:", my_list)

# def make_new_list(lst, elem, remove_index):
#     lst.append(elem)
#     lst.pop(remove_index)
#     return lst

# new_list = make_new_list(my_list.copy(), 'apple', 1)
# print("New list:", new_list)
# print("Original list:", my_list)

# print("ID of the original list:", id(my_list))
# print("ID of the new list:", id(new_list))

# file = open('w9.txt', 'w', encoding='utf-8')
#file = open('/Users/zhenyu/Documents/Github Repository/Ritsumei-35405/Week 9/w9.txt, 'w', encoding='utf-8')

# with open('w9.txt', 'w', encoding='utf-8') as f:
#     f.write('Hello, world!\n')
#     f.write("File starts\n")
#     f.write("Another line...")
#     f.write("Another string.")

with open('w9.txt', 'r', encoding='utf-8') as f:
    data = f.read()

print(data)

with open('w9.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()

print(data)
print(type(data))

with open('w9.txt', 'r', encoding='utf-8') as f:
    data = f.read().splitlines()

print(data)

my_numbers = [1,2,3,4,76,8,9,9]

with open('testw9.txt', 'w', encoding='utf-8') as f:
    for i in my_numbers:
        # the elements of my_numbers are written line by line to testw9.txt as str:
        f.write(str(i) + '\n')

with open("testw9.txt", 'r', encoding='utf-8') as f:
    data = f.read().splitlines()

print(data)
print("type of the list elements:", type(data[0]))

new_data = []
for i in data:
    new_data.append(int(i))

print(new_data)
print("type of the list elements:", type(new_data[0]))