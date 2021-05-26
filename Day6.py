# -*- coding: utf-8 -*-
"""
Created on Tue May 25 10:07:11 2021

@author: Tahamid
"""

# =============================================================================
# Day 6
# =============================================================================

# 57. Functions

# =============================================================================
# syntax:
# def functionName(parameters):
#    functionCode here
# 
# to use this function you have to call the function using functionName
# (arguments)
#   
# So to use a function you have to (1) define it (2) call it
# =============================================================================

#step 1 def(ining) the function
def printIntroduction(name, age, country):
        print(f"Hello my name is {name}. "
          f"I'm {age} yrs old and I'm from {country}.")
    
#step 2 calling the function with proper parameters

printIntroduction('Tahamid', 21, 'Bangladesh')

# 58. Hurdles loop challenge 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json


# 59. Importance of indentation in python 
# code blocks separated by 4 spaces 


# 60. While loops

# =============================================================================
# syntax -
# 
# while somethingIsTrue:
#     do stuff
# 
# unlike for loops you have to do an increment or decrement in a while loop
# 
# we use while loops when we do not have predetermined knowledge of when to
# terminate the loop 
# =============================================================================

# 61, 62 Reeborg's world hurdle completing coding challenge

# =============================================================================
# 63. Final Project: Getting Reeborg through a maze
# 
# The solution has tricky edge cases where there are positions and the 
# direction the robot faces that cause you to go in an infinite loop. 
# The most general solution involves FIRST getting to a wall and then having
# the wall on the right side of the robot. Other than that it is a simple 
# challenge. The code block is given below.
# =============================================================================

# =============================================================================
# def turn_right():
#     for i in range(3):
#         turn_left()
# 
# while front_is_clear():
#     move()
# 
# turn_left()
#     
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
# =============================================================================

# More challenges can be found on https://reeborg.ca/index_en.html


# =============================================================================
# End of Day 6
# =============================================================================
