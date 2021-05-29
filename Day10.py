# -*- coding: utf-8 -*-
"""
Created on Fri May 29 18:00:58 2021

@author: Tahamid
"""

# =============================================================================
# Day 10
# =============================================================================

# 97. Functions with outputs

def formatName(fName, lName):
    
    fName = fName.title()
    lName = lName.title()
    
    return f"{fName} {lName}"

# =============================================================================
#   Manually can be done with a loop
#     for i in range(len(fName)):
#         if i != 0:
#             fName[i] = fName[i].lower()
#         else:
#             fName[i] = fName[i].upper()
#     fName = "".join(fName)
# =============================================================================
    
formattedName = formatName("jAck", "baUER")
print(formattedName)


# 98. Days in Month

def isLeap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
      return False

def daysInMonth(year, month):
    
  if year < 0 or month < 1 or month > 12:
      return "Invalid input"
    
  monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  
  if isLeap(year):
      monthDays[1] = 29
      
  days = monthDays[month - 1]    
  return days

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = daysInMonth(year, month)
print(f"\n{days}")

# 99. Docstrings

def formatName(fName, lName):
    
    '''
    Parameters
    ----------
    fName : str
        first name.
    lName : str
        last name.

    Returns
    -------
    str
        formatted string with first letters of each name capitalized
        and everything else in lower case.
    '''
    
    fName = fName.title()
    lName = lName.title()
    
    return f"{fName} {lName}"
 
# 100. Day 10 Project: Simple calculator

from os import system, name


logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  
| |_________________| | 
|  ___ ___ ___   ___  | 
| | 7 | 8 | 9 | | + | | 
| |___|___|___| |___| | 
| | 4 | 5 | 6 | | - | | 
| |___|___|___| |___| | 
| | 1 | 2 | 3 | | x | | 
| |___|___|___| |___| |  
| | . | 0 | = | | / | | 
| |___|___|___| |___| |  
|_____________________|
"""

def intro():
    print(logo)
    print("Welcome to basic python calculator!\n")
    print("-----------------------------------")

clear = lambda: system('cls' if name=='nt' else 'clear')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def addOperation(operator, funcName):
    operations[operator] = funcName

intro()

operations = {}

addOperation('+', add)
addOperation('-', subtract)
addOperation('*', multiply)
addOperation('/', divide)

def calculator():
    num1 = float(input("What is the first number? "))
    print("")
    for operator in operations:
        print(operator, end = " ")
    calc = True
    while calc:
        op = input("\nPick an operator: ")
        num2 = float(input("\nWhat's the next number? "))
        funcName = operations[op]
        ans = round(funcName(num1, num2),2)
        print(f"\n{num1} {op} {num2} = {ans}") 
        print("-----------------------------------")
        
        keepCalc = input(f"Type 'y' to continue calculating with {ans} or type "
                            "'n' to start a new calculation or 'q' to quit: ")

        if keepCalc == 'y':
            num1 = ans
        elif keepCalc == 'q':
            return
        elif keepCalc == 'n':
            calc = False
            clear()
            intro()
            calculator()   
        else:
            print("Invalid input! Restart program.")
            calc = False
            
calculator()     
   
print("\nThank you for using the calculator~")

# Possible additions later: exponents, n-th roots, maybe uniary operations
# adding uniary operations will require some changes to how the code works now

# =============================================================================
# End of Day 10
# =============================================================================