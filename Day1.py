# -*- coding: utf-8 -*-
"""
Created on Fri May 21 16:43:07 2021

@author: Tahamid
"""

# =============================================================================
# Day 1
# =============================================================================

# 5. Print function
print("Hello world!")

# 6. Printing Challenge
print('Day 1 - Python Print Function'
      '\nThe function is declared like this:'
      '\nprint(\'what to print\')')

# 7. String manipulation
print("Hello" + " Tahamid")

'''
\n = newline
+ = string concatenation
'''

# 8. Lesson on errors and debugging

# 9. Debugging challenge

'''
print(Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
  print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n.")
'''

print("Day 1 - String Manipulation")
print("String Concatenation is done with the" + "   + " + "sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# 10. Input function
input("What is your name? ") #input function returns the string fed into it
print("Hello " + input("What is your name? "))

# 11. Input challenge

'''
Print the lenght of the string of the user's name
'''
print(len(input("What is your name? ")))

# 12. Variables
name = input("What is your name? ")
print(name)

# 13. Swapping values of a and b
a = input("Value of a: ")
b = input("Value of b: ")

temp = a 
a = b
b = temp

print("\n")
print("a: " + a)
print("b: " + b)

# 14. Naming your variable

'''
Give your variables a meaningful name
''' 

# 15. Quiz 

# 16. Project: Band name generator
print("Welcome to the Band Name Generator.")
nameOfCity = input("What's the name of the city you grew up in?\n")
nameOfPet = input("What's your pet's name?\n")
nameOfBand = nameOfCity + " " + nameOfPet
print("\nYour band name could be " + nameOfBand)


# =============================================================================
# End of Day 1 
# =============================================================================
