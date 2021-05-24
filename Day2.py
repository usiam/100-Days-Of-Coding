# -*- coding: utf-8 -*-
"""
Created on Sat May 22 14:45:51 2021

@author: Tahamid
"""
# =============================================================================
# Day 2
# =============================================================================

# 17. Primitive Data Types - Strings/Integers/Floats/Booleans

'''
Strings - "Hello" 
You can get each character out of a string. The way you do this is Hello[i] where i ranges from 0 to length - 1.
So, "Hello"[0] gives you H. And "Hello"[-1] gives you o but also "Hello"[len(Hello) - 1] gives you o.

Note: "123" is a string not a number. "123" + "456" gives you 123456 not 123+456. So, the + sign concatenates.

int - Whole numbers like 123 or 456.
Now, 123 + 456 gives you 579.

You can split large numbers using _ instead of ,
So, 123_456 is just 123456.

float - Floating point numbers i.e. decimal numbers like 123.456.

boolean - True or False
'''

# 18. Type Error, Type Checking, and Type Conversion

'''
type() - Function to check type
Primitive Data Type name (variableName) - Casts the variable into the primitive data type
'''
name = input("What is your name? ")
numChar = len(name)
#print(type(numChar))

strNumChar = str(numChar)
print("Your name is " + name + ". And it has " + strNumChar + " characters.")

num = 123456
print(type(num))
print(type(str(num)))
print(type(float(num)))

# 19. Coding Challenge - Data Types

two_digit_number = input("Type a two digit number: ")
num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])
print(num1 + num2)

# you can generalize this to any digit number by using the following

any_digit_number = input("Type a number of any number of digits: ")

nums = []

for c in any_digit_number:
  nums.append(int(c))

print(sum(nums))

# 20. Mathematical operations in python

'''
3+5 addition
3-5 subtraction
3*5 multiplication
3/5 division
3**5 exponent

Priority - PEMDAS explains the order of priority
Order - (), **, * or /, + or -. It also goes in order from left to right.
So, (3*3 + 3/3 - 3) gives 7.0
'''
print((3*3 + 3/3 - 3))
print(((3) * ((3+3)/3)) - 3)

# 21. Coding challenge - BMI Calculator

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

BMI = float(weight)/((float(height))**2)
intBMI = int(BMI)

print(f"Your weight is {weight}. Your height is {height}." 
      " So, your BMI is {intBMI}.")

# 22. Number manipulation and F Strings in python

'''
round(float, precision) - rounds the float with precision number of decimals
// - floor division. Gives the closest smallest integer. 8//3 = 2.6666 = 2 
+= integer - incrementing. x += 1 => x = x+1
-= integer - decrementing
 print(f"StringHere") - F string. If you use f string you dont have to cast
'''

# 23. Coding challenge - Life in weeks

'''
Gives the number of days, weeks, and months left till 90
'''

age = input("What is your age? ")

yearsLeft = 90 - int(age)
daysLeft = yearsLeft * 365
weeksLeft = yearsLeft * 52
monthsLeft = yearsLeft * 12

print(f"You have {daysLeft} days, {weeksLeft} weeks,"
      " and {monthsLeft} months left.")


# 24. Day 2 Project. Tip calculator (and dividing the bill)
print("Welcome to the tip calculator.")
totalBill = float(input("What was the total bill? $"))
tipPercent = float(input("What percentage tip would you like to give?"
                   " 10, 12, or 15? "))
numPeople = int(input("How many people to split the bill? "))

billPerPerson = round((totalBill * (1 + (tipPercent/100)))/numPeople, 2)
print(f"Each person should pay about ${billPerPerson}")


# =============================================================================
# End of Day 2
# =============================================================================

