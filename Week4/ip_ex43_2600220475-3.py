#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Author：YNAG Minxu
Student ID：26002204753
Program description:Add all even numbers from 1 to 300.

"""
 
number = 1
total = 0

while number > 0:
    if (number % 2) == 0:
        total += number
        if number == 300:
            break
    number += 1
    
print(total)
          