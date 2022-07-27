#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author：YANG Minxu
Student ID：26002204753
Program description:
    
"""

class Cat:
    animal_type = "carnivore"

    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def describe(self):
        return "{} is {} years old".format(self.name, self.age)

    def say(self, sound):
        return "{} says {}".format(self.name, sound)

marie = Cat("Marie", "black", 3)
print(marie.describe())

print(marie.say("Meow"))

# marie = Cat("Marie", "orange", 9)
# tutu = Cat("Tutu", "brown", 6)

# print("Name of the marie object:", marie.name)
# print("Color and age of the tutu object:", tutu.color, tutu.age)
# print("Animal type of the marie object:", marie.animal_type)

# marie.age = 8
# print(marie.age)