# -*- coding: utf-8 -*-
"""
Created on Mon May 24 13:30:10 2021

@author: Tahamid
"""

# =============================================================================
# Day 5
# =============================================================================

# 48. For loop and list

fruits = ["apple", "peach", "pear"]

for fruit in fruits:
    print(fruit)
    print(f"{fruit} pie")
   
# syntax:
# for varName in iterableName: 
#    do this


# 49. Coding Challenge: Average Height

student_heights = input("Input a list of student heights: ").split(",")
sumHeights = 0
numStudents = 0

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  sumHeights += student_heights[n]
  numStudents += 1
  
avgHeight = round(sumHeights/numStudents)
print(f"The average height of the students in the list is {avgHeight} cm.") 

# you can also do this using built in functions:
# sum(student_heights)/len(student_heights)

# 50. Highest score

student_scores = input("Input a list of student scores:\n").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

maxScore = student_scores[0]

for score in student_scores:
    if score > maxScore:
        maxScore = score

print(f"Max score in the list is {maxScore}!")

#this is what the max(iterable) does

# 51. For loops and range() function

for number in range(1, 11, 3): #number goes from [1, 11-1]
    print(number)

#range(begin, end, stepSize) where end is not included

# 52. Coding Challenge: Adding all even numbers from 1-100

total = 0

for i in range(2, 101, 2):
    total += i

print(f"Sum of all even numbers between 1 and 100 is: {total}")

# 53. Fizzbuzz

print("\nFizzbuzz Interview Question\n")

for i in range(1, 101):
    if i % 3 == 0:
        str = "Fizz"
        if i % 5 == 0:
            str += "Buzz"
        print(f"{str} ({i})")
    elif i % 5 == 0:
        str = "Buzz"
        print(f"{str} ({i})")
    else:
        str = i
        print(str)
        
# 54. Day 5 Project: Password Generator
##############################################################################

# METHOD 1 - Using a list and then converting to string 

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


passList = []

# appends nr_letters number of letters into the passList
for i in range(nr_letters):
    letterIndex =  random.randint(0, len(letters) - 1)
    passList.append(letters[letterIndex])
    # we could also use passList.append(random.choice(letters))

# appends nr_symbols number of symbols into the passList    
for i in range(nr_symbols):
    symbolIndex =  random.randint(0, len(symbols) - 1)
    passList.append(symbols[symbolIndex])

# appends nr_numbers number of numbers into the passList
for i in range(nr_numbers):
    numberIndex =  random.randint(0, len(numbers) - 1)     
    passList.append(numbers[numberIndex])

# shuffles the order of the elements in the passList 10 times
for i in range(10):
    j = random.randint(0, len(passList) - 1)
    k = random.randint(0, len(passList) - 1)
    temp = passList[j]
    passList[j] = passList[k]
    passList[k] = temp

# random.sample(passList,  len(passList)) also shuffles
# random.shuffle() also works. random.shuffle(passList) just overwrites 

#shuffledPassList = random.sample(passList, len(passList))

password = ""
 
# turns the passList into a string  
for i in passList:
     password += i
     
# you can also join the elements in a list using " ".join(listName)
# this joins the elements in the list and puts a whitespace " " between them
 
print(f"\nThe randomly generated password with {nr_letters} letters," 
       f" {nr_symbols} symbols, and {nr_numbers} numbers is: {password}")    

##############################################################################

# Method 2 - No list needed; directly concatenates to a str

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = ""

for i in range(nr_letters):
    password += random.choice(letters)

for i in range(nr_symbols):
    password += random.choice(symbols)

for i in range(nr_numbers):
    password += random.choice(numbers)

shuffled = "".join(random.sample(password, len(password)))

print(f"\nThe randomly generated password with {nr_letters} letters," 
       f" {nr_symbols} symbols, and {nr_numbers} numbers is: {shuffled}")  


# =============================================================================
# End of Day 5
# =============================================================================
