#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author：YANG Minxu
Student ID：26002204753
Program description:
First，read in the file to a list and convert the list to a Numpy array.
Then create a 1-D numpy array has 30 values.
Combines the two array from the file.
Create a 1-D number array that has 30 values.
The program then combines that array with the array it made earlier.
Last print the average of the first 1-D array 
and the sum of the last array

"""

import numpy as np
from numpy import random

def make_array(filename):
    
    """ 
First  Reads a file,then converts the string elements to floating point numbers
by creating an empty list and using a for loop.
Then fill it by creating an empty list and using a for loop.
Lastly return to the array.

    """
    
    with open(filename, 'r', encoding='utf-8') as f:
        textarray = f.read().splitlines()
        lst = []
        for i in textarray:
            floats = float(i)
            lst.append(floats)
        return np.array(lst)

read_arr = make_array("numbers.txt")
print("Array created from the numbers of the text file:", read_arr)
print("Type of read_arr:", type(read_arr))


arr_1 = np.linspace(5, 100, num = 30)

arr_1 = arr_1 + read_arr

arr_2 = random.rand(30)

stacked_array = np.stack((arr_1, arr_2), axis=0)
print("The stack array:", stacked_array)

average = np.mean(stacked_array[0])
print("Average of stacked_array[0]:",average)

summa = np.sum(stacked_array[1][0:5])
print("Sum of the first 5 elements of stacked_array[1]:", summa)
