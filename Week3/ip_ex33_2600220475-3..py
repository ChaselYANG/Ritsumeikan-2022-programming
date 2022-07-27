#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 12:07:09 2022

Author：YNAG Minxu
Student ID：26002204753
"""

iterations=0
number=4
while number<100000:
    print(number)
    number=2**number
    iterations=1+iterations
print("It took this many iterations:")
print(iterations)

