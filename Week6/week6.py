#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author：YANG Minxu
Student ID：26002204753
Program description:
    
"""

# languages = ["FORTRAN", "COBOL", "LISP"]
# print('initial list;', languages)

# languages.append("ALGOL")
# print('updated list;', languages)

# # NOT ALLOWED
# languages = ["FORTRAN", "COBOL", "LISP"]
# languages.append("ALGOL", "BASIC")

# languages = ["FORTRAN", "COBOL", "LISP"]
# print('initial list;', languages)
# languages.append(["ALGOL", "BASIC"])
# print('updated list;', languages)

# languages_1 = ["FORTRAN", "COBOL", "LISP"]
# languages_2 = ["ALGOL", "SNUBOL", "BASIC"]
# print('initial list;', languages_1, languages_2)
# new_list = languages_1 + languages_2
# print('merged list;', new_list)

# languages_1 = ["FORTRAN", "COBOL", "LISP"]
# languages_2 = ["ALGOL", "SNUBOL", "BASIC"]
# print('initial languages 1 list;', languages_1)
# languages_1.extend(languages_2)
# print('updated languages 1 list;', languages_1)

# languages_1 = ["FORTRAN", "COBOL", "LISP"]
# languages_2 = ["ALGOL", "SNUBOL", "BASIC"]
# print('initial list;', languages_1)
# for l in languages_2:
    # languages_1.append(l)
# print('updated list;', languages_1)

our_list = []
i = 0
while len(our_list) < 10:
    our_list.append(i)
    i += 1
print("our list;", our_list)
# print("the length of our list;", len(our_list))
# maximum = max(our_list)
# minimum = min(our_list)
# print("maximum;", maximum, "\nminimum;", minimum)

# languages = ["FORTRAN", "COBOL", "LISP"]
# languages.insert(1, "ALGOL")
# print(languages)

# languages = ["FORTRAN", "COBOL", "LISP", "COBOL"]
# languages.remove("COBOL")
# print(languages)
# languages.remove("COBOL")
# print(languages)

# languages = ["FORTRAN", "COBOL", "LISP", "ALGOL"]
# print("initial list:", languages)
# languages.pop(2)
# print("updated list:", languages)

# popped_element = languages.pop(1)
# print("2x modified list:", languages)
# print("popped element:", popped_element)

# languages = ["FORTRAN", "COBOL", "LISP"]
# print("initial list:", languages)
# languages.reverse()
# print("reversed list:", languages)

# l1 = ["FORTRAN", "COBOL", "LISP"]
# l2 = l1.copy()
# print("l1:", l1)
# print("l2:", l2)

# lang1 = ["FORTRAN", "COBOL", "LISP"]
# lang2 = lang1
# print("lang1:", lang1)
# print("lang2:", lang2)

# languages = {
#     "FORTRAN": 1957,
#     "LISP": 1958,
#     "COBOL": 1959,
# }

# print("keys of languages list:", list(languages.keys()))
# values = list(languages.values())
# print("second element of values:", values[1])

# print(languages.get('FORTRAN'))
# print(languages['FORTRAN'])

# print(languages.get('ALGOL'))

# l1 = {
#     "FORTRAN": 1957,
#     "LISP": 1958,
#     "COBOL": 1959
# }

# l2 = {
#     "SNOBOL": 1962,
#     "BASIC": 1964
# }

# print("og dict:", l1)
# l1.update(l2)
# print("updated dict:", l1)

# l1 = {
#     "FORTRAN": 1957,
#     "LISP": 1958,
#     "COBOL": 1959
# }

# l2 = {
#     "FORTRAN": "a programming language",
# }

# print("og dict:", l1)
# l1.update(l2)
# print("updated dict:", l1)

# ls = {
#     "FORTRAN": 1957,
#     "LISP": 1958,
#     "COBOL": 1959
# }

# print("og dict:", ls)
# ls.pop("LISP")

# print("updated dict:", ls)
# poppy = ls.pop("COBOL")
# print("2x modified dict:", ls)
# print("popped element:", poppy)

# langs = ["FORTRAN", "COBOL", "LISP"]
# new_list = []

# for l in langs:
#     if "L" in language:
        