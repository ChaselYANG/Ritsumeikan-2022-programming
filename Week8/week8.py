#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author：YANG Minxu
Student ID：26002204753
Program description:
    
"""

def rectangle_area(width, height):
    """Calculates the area of a rectangle,
    given its width and height."""
    area = width * height
    return area

my_area = rectangle_area(8,5)
print(my_area)

def greeting(name):
    """Says hi to the person passed in as an argument (must be a string)"""
    print("Hi, " + name + "!")

greeting("Bob")

def rectangle_area(width, height):
    """Calculates the area of a rectangle,
    given its width and height."""
    area = width * height
    return area

def assigning_func(w, h, app_dict):
    """Assigns a new keypair value pair to a dict, where
    the key is a tuple of the rect width and height, and
    the value is the area of the rectangle."""
    app_dict[(w, h)] = rectangle_area(w, h)

rect_areas = {}

assigning_func(6, 8, rect_areas)
print("Rectangle areas:", rect_areas)
assigning_func(12, 2, rect_areas)
print("Rectangle areas:", rect_areas)

names_scores = {
    "Bob": 40,
    "Monica": 80,
    "Paul": 91
}

passed_list = []
failed_list = []

def passornot(score_dict, passed, failed):
    """Function that evaluates if a student has passed or failed
    and stores the name of the students accordingly in separate
    lists. As an argument, it takes a dictionary where the keys
    are the student names and the values are the scores. the two
    other arguments are two lists to add the names to."""
    for name, score in score_dict.items():
        if score < 60:
            failed.append(name)
        else:
            passed.append(name)

passornot(names_scores, passed_list, failed_list)
print("Passed:", passed_list)
print("Failed:", failed_list)

def circle_area(r):
    pi = 3.14159
    return pi*(r*r)

print(circle_area(5))
#print(circle_area(5,6))

def greeting(name, message="Hello, ", times=3):
    print((message + name + "!\n")*times)

print("Only providing the name arguement, using default for others:")
greeting("Bob") #1 positional arguement

print("Overwriting the default value for message (order is important):")
greeting("Bob", "Hi, ") #2 positional arguements

print("Overwriting the default value for message and times (order is impt):")
greeting("Bob", "Hi, ", 1) #3 positional arguements

print("Overwriting times, but because of the order, the name needs to be specificed in the call: ")
greeting("Bob", times=5) #1 positional and one keyword argument

print("here, everything is specified by name/keyword, so the order is unambiguous: ")
greeting(times = 2, message= "Hi, ", name="Bob") #3 positional and two keyword arguments

print(passornot.__doc__)