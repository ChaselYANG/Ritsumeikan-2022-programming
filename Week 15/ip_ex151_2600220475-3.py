#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: YANG Minxu
Student ID: 2600220475-3

""" 

from numpy import random

class Adventurer:
    """
    Instansitate of the Adventurer class defines an object with class
    attribute maximum health, and instance attributes name and (current) health.
    An Adventurer can introduce itself, and has an instance method that decides 
    if the Adventurer needs healing or not.
    """
    max_health = 100

    def __init__(self, name):
        self.name = name
        self.health = random.randint(60, 91)
     
    def intro(self):
        """
        Adventurer introduction.
        Returns a string.
        """   
        print("Hello my name is " + self.name + "!")
    
    def needs_heal(self):
        """
        Check if the adventurer is less than 80%, if less then it needs healing.
        Returns a string.
        """
        if self.health < 80:
            print("I need healing!")
            return True
        else:
            print("I'm fine!")
            return False
            
      
class Healer(Adventurer):
      """
      The healer class inherits from the Adventurer class.
      The healer has an instance method to heal the adventurer.
      """
    
      def __init__(self, name, medicine_stock):
          super().__init__(name)
          self.medicine_stock = medicine_stock
    
    
      def healer_intro(self):        
         """
         Provide an introduction to the healer and print out
         the current medicine inventory using the adventurer's 
         introduction method.
         """
         
         self.intro()
         print("My current medicine stock is {}.".format(self.medicine_stock))
    
              
      def heal(self, adventurer):
         """
         Treat the adventurer if there are medicines in stock; 
         if not, do not treat them and print out the medicine.
          
         """

         heal_value = adventurer.max_health - adventurer.health

         if self.medicine_stock == 0:
            print("I'm out of medicine, sorry!")
            return


         if heal_value > self.medicine_stock:
             print("I can only help this much, sorry!")
             adventurer.health += self.medicine_stock
             self.medicine_stock = 0
             return

         print("Here you go, fully healed!")
         adventurer.health = adventurer.max_health
         self.medicine_stock -= heal_value

         return

healer = Healer("Bob the Healer", 80)

adventurers = ["Emma", "Peter", "Anna", "Jim", "John"]

healed_list = []

for i in adventurers:
    print()

    adventurer = Adventurer(i)
    adventurer.intro()
    
    if adventurer.needs_heal():
        print("Health of", adventurer.name, "is",adventurer.health)
        healer.healer_intro()
        healer.heal(adventurer)
        print("Health of " + adventurer.name + "now is", adventurer.health)

    healed_list.append((adventurer.name, adventurer.health))

print("\n", healed_list)
