#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Author：YANG Minxu
Student ID：26002204753
Program description:The program take the list and flattens it ,and changes
it to add it to the normal list.
Then filter the positive numbers in the list and the two stored in 
the list,Odd and even numbers. It have 3 parameters which are the list of
 numbers, even and odd numbers.
Last step delete duplicate content from the list.
    
"""

num_lst = [[1,1,4,66],[-55,7],[-1,43,55,-6,12,12,4]]

even_numbers = []
odd_numbers = []

def flatten_list(a_list):
    """Take the list and flattens it, and changes it to add it to the 
    normal list."""
    flat_num_lst = []
    for lst in a_list:
        for element in lst:
            flat_num_lst.append(element)
    
    return flat_num_lst


def filter_numbers(number_list,evens=even_numbers,odds=odd_numbers):
    """Filter the positive numbers in the list and the two stored in 
    the list, Odd and even numbers. It have 3 parameters which are the list of
     numbers, even and odd numbers."""
    for i in number_list:
        if i > 0:
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)
        
def remove_dups(a_list):
    """Delete duplicate content from the list"""
    dups_removed = list(dict.fromkeys(a_list))
    return dups_removed


print("Original nested list:", num_lst)

flat_num_lst = flatten_list(num_lst)
print("Flattened list:", flat_num_lst)

filter_numbers(flat_num_lst)
print("The even numbers:", even_numbers)
print("The odd numbers:", odd_numbers)

uniq_even_numbers = remove_dups(even_numbers)
uniq_odd_numbers = remove_dups(odd_numbers)
print("The unique even numbers:", uniq_even_numbers)
print("The unique odd numbers:", uniq_odd_numbers)