#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Author：YANG Minxu
Student ID：26002204753
Program description:
Create two new lists and make them merge into one.
Use .append method to add a third list
then use the .reverse method to reverse the list
Create a new dictionary and enumerate it
add the scientist's name and number
use the .update method in the former dictionary
create index list 
use slicing to get the first 5 elements and put the values into the list.
use a for loop to check whether the number is even or odd.
pick out the odd number, and print the maximum number.


"""
scientist_list_1 =['Einstein','Curie','Newton','Darwin']
scientist_list_2 =['Tesla','Galilei','Lovelace']

scientist_list = scientist_list_1 + scientist_list_2

scientist_list_3 = ['Hawking','Faraday']
for scientist in scientist_list_3:
    scientist_list.append(scientist)
    
print("Length of the scientist list:", len(scientist_list))

scientist_list.reverse()
print("Revered scientist list",scientist_list)

scientist_dict = {}

for index, scientist in enumerate(scientist_list):
    scientist_dict[scientist] = index
    
scientist_dict_2 ={
    "Faraday" : 1,
    "Boyle" : 9
}
scientist_dict.update(scientist_dict_2)

print("The scientist dictionary:",scientist_dict)

index_list = list(scientist_dict.values())

numbers = index_list[0:5]
print("Numbers list:",numbers)

one = numbers.pop(0)

for number in numbers:
    if(number % 2) !=0:
       numbers.remove(number)
       
print("The number list filtered out of odd numbers:",numbers)

print("The maximum number in the number list:",max(numbers))
       
       
       
       