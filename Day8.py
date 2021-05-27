# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:07:30 2021

@author: Tahamid
"""

# =============================================================================
# Day 8
# =============================================================================

import math

# 79. Functions with inputs

def greet(name):
    print(f"Hello, {name}.")
    print(f"How do you do, {name}?")
    print("Isn't the weather nice today?")

greet('Tom')

# 80. Positional vs Keyword Arguments

def greetWith(name, location):
    print(f"Hello, {name}.")
    print(f"I've heard you're from {location}. How is it in {location}?")

greetWith('Jack', 'UK')

# if we called the function as greetWith('UK', 'Jack') then name = UK and
# location = Jack. 
# we can 'fix' this positional argument issue with keyword argument.
# if we call the function with greetWith(location = 'UK', name = 'Jack')


# 81. Number of cans of paint

# cover = area that the can of paint can cover
# Area = Area to cover
def paint_calc(height, width, cover):
  area = height * width
  numOfCans = area/cover
  print(f"You'll need {math.ceil(numOfCans)} cans to paint {area} sq area.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# 82. Prime number checker

def prime_checker(number):
  isPrime = True
  
  for i in range(2, number):
    if number % i == 0:
      isPrime = False
  
  if isPrime:
    print(f"{number} is a prime number.")
  else:
    print(f"{number} is not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)

# 83. Day 8 Project: Ceaser Cipher

import Day8utils

alphabet = Day8utils.alphabet

logo = Day8utils.logo
thankYou = Day8utils.thankYou

print(logo)
print("----------------------------------------------------------------")

userInput = input("Do you wish to use Ceaser Cipher en/decoder? "
                  "Type yes or no: ")

#caesar function combines encrypt and decrypt to reduce code
def caesar(initMsg, shift, direction):
    if direction == "decode":
        shift = -shift
    finalMsg = ""
    for letter in text:
        oldPos = alphabet.index(letter)
        newPos = (oldPos + shift) % len(alphabet)
        finalMsg += alphabet[newPos]
    print(f"\nThe {direction}d text is {finalMsg}.")

while userInput == "yes":
  
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(text, shift, direction)    
    
    userInput = input("Do you want to use this again? ")


if userInput == "no":
    print("\n--------------------------------")
    print(thankYou)
    print("Thank you for coming!")


# =============================================================================
# End of Day 8   
# =============================================================================
