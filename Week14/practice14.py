#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author：YANG Minxu
Student ID：26002204753
Program description:
    
"""


class Car:
    classification = 'vehicle'
    application = 'transportation'

    def __init__(self, name, fuel_source, speed):
        self.name = name
        self.fuel_source = fuel_source
        self.speed = speed

    def accelerate(self, acc):
        self.speed += acc
        return self.speed

bmw = Car('BMW', 'gasoline', 60)
print(bmw.accelerate(20))