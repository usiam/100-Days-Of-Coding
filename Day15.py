# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:32:22 2021

@author: Tahamid
"""

# =============================================================================
# Day 15
# =============================================================================

from Day15utils import resources, MENU, coins, logo, nextOrderArt
from os import system, name

print(logo)

money = 0

clear = lambda : system('cls' if name == 'nt' else 'clear')

def updateMoney(coffeeChoice):
    '''
    Updates money depending on the choice of coffee's cost
    '''
    global money
    money = money + MENU[coffeeChoice]['cost']    
    
def printReport():
    '''
    Prints how much resource is left in the machine
    '''
    print("\nREPORT:\n-----------")
    for resource in resources:
        print(f"{resource.title()}: {resources[resource]} ml")
    print(f"Money: ${money}\n")

def checkResources(coffeeChoice):
    ''' 
    Checks if there is enough resource in the maching to make the choice 
    of coffee
    '''
    
    ingredients = MENU[coffeeChoice]['ingredients']

    for ingredient in ingredients:
       ingrNeeded = ingredients[ingredient]
       ingrRem = resources[ingredient]
       if ingrRem - ingrNeeded <= 0:
           print(f"\nSorry there is not enough {ingredient}. Refilling now!")
           refill()
           return False
    return True

def processPay():
    '''
    Returns how much the customer paid depending on the number of coins of 
    each type inserted
    '''
    print("\n")
    coinList = []
    for coin in coins:
        coinList.append(int(input(f"Please insert {coin}: ")))
    pay = (coinList[0] * 0.25) + (coinList[1] * 0.10) + (coinList[2] * 0.05) + (coinList[3] * 0.01)
    return pay

def makeCoffee(coffeeChoice):
    '''
    Subtracts the resources that the choice of coffee requires from 
    the resources in the machine
    '''
    ingredients = MENU[coffeeChoice]['ingredients']
    
    for ingredient in ingredients:
        ingrNeeded = ingredients[ingredient]
        resources[ingredient] -= ingrNeeded
    print(f"\nHere is your {coffeeChoice}. Enjoy!")
 
# a rather crude way to reset the tank. Better solution update hopefully soon
def refill():
    ''' 
    Refills the machine with the max resources possible. Function is called
    when checkResources(coffeeChoice) returns False.
    '''
    resources['water'] = 1000
    resources['milk'] = 500
    resources['coffee'] = 250
        
       
turnOff = False
while not turnOff:
    coffeeChoice = input("What would you like? (espresso/latte/cappuccino): ")
    if coffeeChoice == 'off':                        
        print("\nMachine turning off now!")
        turnOff = True
    elif coffeeChoice == 'report':
        printReport()    
    else:
        suffRes = checkResources(coffeeChoice)
        if suffRes == False:
            turnOff = True
        else:
            paid = processPay()
            coffeeCost = MENU[coffeeChoice]['cost']
            if paid >= coffeeCost:
                updateMoney(coffeeChoice)
                change = round(paid - coffeeCost, 2)
                print(f"\nHere is ${change} dollars in change.")
                makeCoffee(coffeeChoice)
                print(nextOrderArt)
            else:
                print("\nSorry that's not enough money. Money refunded.")



# =============================================================================
# End of Day 15
# =============================================================================
