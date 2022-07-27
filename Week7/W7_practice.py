#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author/student name:
Student ID:
Program description:
"""

my_nested_list = [[1,1,3], ["apple", "orange", "orange"], [0], [0,0,0]]
print("Original list:", my_nested_list)

#remove the duplicated from the lists inside the list my_nested_list !
for index, a_list in enumerate(my_nested_list):
    my_nested_list[index] = list(set(a_list))
print("Dups inside small lists removed:", my_nested_list)

temp_list = [] #define empty list we will populate with unique lists
for element in my_nested_list: #for all the small lists in the nested list
    if element not in temp_list: #if the current small list is still not in the temporary list
        temp_list.append(element) #append it the temporary list

my_nested_list = temp_list #if we want to keep the original name for the list
print("Duplicate lists are removed:", my_nested_list)

my_string = "the phenomenon time dilation is the difference in the elapsed time as measured by two clocks"
split_string = my_string.split() #split a string by the whitespaces to a list
print("The split string in a list:", split_string)

string_counts = {} #define empty dictionary
for elem in split_string: #for the strings inside our list of strings
    if elem in string_counts: #if the current one is already in our counting dictionary (key)
        string_counts[elem] += 1 #increment the count
    else: #if the string is not yet in our dictionary (key)
        string_counts[elem] = 1 #assign the value to 1, since it's the first time

print("String count dictionary:", string_counts)
print('How many times we encountered the string "time"?', string_counts.get('time')) #use the get method
