# -*- coding: utf-8 -*-
"""
Created on Sat May 23 17:43:58 2021

@author: Tahamid
"""
# =============================================================================
# Day 3
# =============================================================================

# 27. Control flow with if/else and Conditional operators

'''
if condition is True:
    do this
else:
    do this
'''

# Program to allow people to buy tickets to rollercoaster
print("Welcome to the rollercoaster!")
height = float(input("What is your height in cm? "))

if height >= 120:
    print("Here is your ticket. Have fun!")
else:
    print(f"Sorry you're {height} cm,"  
         " which is less than 120 cm :(")


'''
Comparison operators:
> - greater than
< - less than
>= - greater or equal
<= - less or equal
== - equal to (Note: == is comparison and = is assignment)
!= - not equal (! implies not)
'''

# 28. Coding challenge - Check if number is odd or even

'''
% - modulo operator. Returns the remainder.
5 % 2 = 1 
'''

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print(f"Your number, {number}, is even!")
else:
    print(f"Your number, {number}, is odd!")

# 29. Nested if and elif 

'''
if condition:
    if condition1:
        do this
    elif condition2:
        do this
    else:
        do this
else:
    do this
'''

# Improve the ticket program where you check age and 
# give them a certain price.

print("Welcome to the rollercoaster!")

height = float(input("What is your height in cm? "))

if height >= 120:
    
    age = int(input("What is your age? "))
    ticketPriceOver18 = 12
    ticketPriceBetween12And18 = 7
    ticketPriceUnder12 = 5
    
    if age > 18:
        print(f"That will be ${ticketPriceOver18} please.")
    elif 12 <= age <= 18:
        print(f"That will be ${ticketPriceBetween12And18}"
              " please.")
    else:
        print(f"That will be ${ticketPriceUnder12}"
              " please.")

    print("Here is your ticket. Have fun!")

else:
    print(f"Sorry you're {height} cm,"  
         " which is less than 120 cm :(")
    
'''
A better way to do this would be
    
if age < 12:
    print price
elif age <= 18:
    print price
else:
    print price
        
This is better because it reads better.
'''

# 30. BMI Calculator 2.0 (with interpretation)

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / (height ** 2))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

# 31. Checking if a year is a leap year

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"Year {year} is a leap year")
        else:
            print(f"Year {year} is not a leap year")   
    else:
        print(f"Year {year} is a leap year.")
else:
    print(f"Year {year} is not a leap year.")

# 32. Multiple if statements in succession

'''
if condition1:
    do A
if condition2:
    do B
if condition3:
    do C
'''

# Improving the rollercoaster program even more (v 3.0)
# now with picture taking option

print("Welcome to the rollercoaster!")

height = float(input("What is your height in cm? "))

if height >= 120:
    
    age = int(input("What is your age? "))
    
    ticketPriceOver18 = 12
    ticketPriceBetween12And18 = 7
    ticketPriceUnder12 = 5
    
    if age < 12:
        ticketPrice = ticketPriceUnder12
    elif age <= 18:
        ticketPrice = ticketPriceBetween12And18
    else:
        ticketPrice = ticketPriceOver18
    
    picTaken = input("Do you want a picture? ")
    
    if picTaken == "Yes":
        picPrice = 3
        totalBill = ticketPrice + picPrice
        print(f"Your total cost is ${totalBill}.")    
    elif picTaken == "No":
        totalBill = ticketPrice
        print(f"That will be ${totalBill} please.")
    
    print("Here is your ticket. Have fun!")

else:
    print(f"Sorry you're {height} cm,"  
         " which is less than 120 cm :(")
    

# 33. Coding challenge: Pizza delivery program

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

smallPrice = 15
medPrice = 20
largePrice = 25
pepSmallPrice = 2
pepOtherPrice = 3
cheesePrice = 1

bill = 0

if size == "S":
    bill += smallPrice
elif size == "M":
    bill += medPrice
else:
    bill += largePrice
    
if add_pepperoni == "Y":
    if size == "S":
        bill += pepSmallPrice
    else:
        bill += pepOtherPrice

if extra_cheese == "Y":
    bill += cheesePrice

print(f"Your final bill is ${bill}.")

# 34. Logical operators

'''
and - True if both conditions are true and False if 
even one of the conditions is false
or - True if either is true and false if BOTH are false.
'''

# Free ticket for midlife crisis addition to 
# rollercoaster program


print("Welcome to the rollercoaster!")

height = float(input("What is your height in cm? "))

if height >= 120:
    
    age = int(input("What is your age? "))
    
    ticketPriceOver18 = 12
    ticketPriceBetween12And18 = 7
    ticketPriceUnder12 = 5
    ticketPriceWithMidlifeCrisis = 0
    if age < 12:
        ticketPrice = ticketPriceUnder12
    elif age <= 18:
        ticketPrice = ticketPriceBetween12And18
    elif age >= 45 and age <= 55:
        ticketPrice = ticketPriceWithMidlifeCrisis
    else:
        ticketPrice = ticketPriceOver18
    
    picTaken = input("Do you want a picture? ")
    
    if picTaken == "Yes":
        picPrice = 3
        totalBill = ticketPrice + picPrice
        print(f"Your total cost is ${totalBill}.")    
    elif picTaken == "No":
        totalBill = ticketPrice
        print(f"That will be ${totalBill} please.")
    
    print("Here is your ticket. Have fun!")

else:
    print(f"Sorry you're {height} cm,"  
         " which is less than 120 cm :(")
    
# 35. Love Calculator (Kind of Challenging tbh)

'''
useful functions => 
str.count('char') - gives the count of char in str
str.lower() - makes all the characters lower case.
'''

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lowerName1 = name1.lower()
lowerName2 = name2.lower()

lowerNames = lowerName1 + lowerName2 

checkTrue = "true"
checkLove = "love"

totalTrue = 0
totalLove = 0

for c in lowerNames:
    for d in checkTrue:
        if c == d:
            totalTrue += 1 
    for e in checkLove:
        if c == e:
            totalLove += 1

        
score = int(str(totalTrue) + str(totalLove))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
    
    
# 36. Day 3 Project - Treasure Island.

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

level1Choice = input("You are in a maze with two paths. Choose the 'left' or 'right' path? ").lower()

if level1Choice != "left":
    print("\nYou were devoured by a monster. Game Over.")
else:
    level2Choice = input("You have come to a lake. "
                         "Do you want to 'swim' across or 'wait' for help? ").lower()
    if level2Choice != "wait":
        print("\nYou were eaten by piranhas in the lake. Game Over.")
    else:
        level3Choice = input("The game master has guided you to a wall with three doors!"
                             " Choose the 'red' or 'blue' or 'yellow' door? ").lower()
        if level3Choice != "yellow":
            print("\nYou fell off the map. Game Over.")
        else:
            print("\nYou've found the treasure. You Win!")
            
            
# =============================================================================
# End of Day 3  
# =============================================================================






























