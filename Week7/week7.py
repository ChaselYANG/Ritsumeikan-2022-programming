#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author：YANG Minxu
Student ID：26002204753
Program description:
    
"""

# lang_tuple = ("FORTRAN", "COBOL", "LISP")
# print("initial tuple:", lang_tuple, "\ndata type:", type(lang_tuple))
# print("second element:", lang_tuple[1])

# my_tuple = (10, 20, 30, 40)

# n1, n2, n3, n4 = my_tuple
# print("For example, number 2:", n2)

# sd = {
#     'Da Vinci': 1452, 
#     'Galilei': 1564, 
#     'Newton': 1642
# }

# elements = list(sd.items())
# print("List of dict items in a list of tuples:", elements)
# print("First element:", elements[0])

# my_set = {2, 3, 4, "apples"}
# print("My set:", my_set)

# lang_set = {"FORTRAN", "COBOL", "LISP"}
# print("Original language set:", my_set)
# lang_set.add("C++")
# print("New language set:", lang_set)

# lang_set.add("FORTRAN")
# print("Language set was not modified:", lang_set)

# lang_set = {"FORTRAN", "COBOL", "LISP"}
# print("Original language set:", lang_set)
# lang_set.remove("COBOL")
# print("Modified language set:", lang_set)
# lang_set.pop()
# print("Modified language set:", lang_set)

# ls1 = {"FORTRAN", "COBOL", "LISP"}
# ls2 = {"C++", "COBOL"}

# print("Original language sets:", ls1, ",", ls2)

# inter = ls1.intersection(ls2)
# diff = ls1.difference(ls2)

# print("Elements that exist in both ls1 and ls2:", inter)
# print("Elements that exist in ls1 but not in ls2:", diff)

# ls1.update(ls2)
# print("Updated ls1:", ls1)

# my_list = ["FORTRAN", "COBOL", "FORTRAN", 1, 2, 2]
# my_set = set(my_list)

# print("Original list:", my_list, '\ntype:', type(my_list))
# print("duplicates removed:", my_set, '\ntype:', type(my_set))

# my_list = list(set(my_list))
# print("The list in dupes removed:", my_list, '\ntype:', type(my_list))

my_list = ["FORTRAN", "COBOL", "FORTRAN", 1, 2, 2]
my_list = list(dict.fromkeys(my_list))
print("Duplicates removed and order preserved:", my_list)

my_tuple = ("apple", "apple", "orange")
my_set = {"apple", "apple", "orange"}

print("My tuple:", my_tuple, '\nMy set:', my_set)
print('The word (string) "orange" is an element in the tuple:', "orange" in my_tuple)
print('The word (string) "lemon" is not an element in the set:', "lemon" not in my_tuple)

mnl = [[1, 1, 3], ["apple", "orange", "orange"], [0], [0, 0, 0]]
print("My list:", mnl)

for index, a_list in enumerate(mnl):
    mnl[index] = list(dict.fromkeys(a_list))

print("My list with duplicates removed:", mnl)

temp = []
for element in mnl:
    if element not in temp:
        temp.append(element)

mnl = temp
print("dupes are removed:", mnl)

my_str = "the phenomenon time dilation is the difference in the elapsed time as measured by two clocks"
split_str = my_str.split()
print("My string:", my_str)
print(type(split_str))

string_counts = {}
for elem in split_str:
    if elem in string_counts:
        string_counts[elem] += 1
    else:
        string_counts[elem] = 1

print("String counts:", string_counts)
print('How many times we encountered the string time:', string_counts["time"])