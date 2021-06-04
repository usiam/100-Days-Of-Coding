# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 17:15:26 2021

@author: Tahamid
"""

# =============================================================================
# Day 16: Object oriented programming
# =============================================================================

# 114. Intro to OOP

# =============================================================================
# Program is modelled after an object
# 
# Let's try to model a waiter:
#     1) Things it HAS: isHoldingPlate = False, responsibleTables = [1, 2, 3]
#     2) Things it DOES: takesOrder(table, order) takesPayment(table, payment)
# 
# The things an object HAS are called its attributes.
# and 
# The things it does are called its methods.
# 
# Now we can have multiple waiters. Each version is called an instance of waiter
# 
# Waiter (the blueprint) in OOP is called a class and every instance of the
# class is called an object
# syntax:
# objectName = className()
# to get attribute of the object: atrName = objectName.attribute
# to get a method of the object: methodName = objectName.method() 
# =============================================================================

import turtle
from turtle import Screen
                
myTurt = turtle.Turtle() # we fetched Turtle class from     the turtle module 
                         # and gave it the name myTurt

# we can also do from turtle import Turtle and then myTurt = Turtle()

# methods to change turtle object graphics
myTurt.shape('turtle')
myTurt.color('DarkSeaGreen4')
myTurt.forward(100)


# methods to display
myScr = Screen()
myScr.exitonclick()

# 146. Installing and using prettytable package

from prettytable import *

table = PrettyTable()
table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column("Type", ['Electric', 'Water', 'Fire'])
table.set_style(DEFAULT)
print(table)
print("\n")
fieldsToPrint = table.get_string(fields = ['Pokemon Name'])
print(fieldsToPrint)

# =============================================================================
# End of Day 16
# =============================================================================





