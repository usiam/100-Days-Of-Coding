# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 13:08:52 2021

@author: Tahamid
"""
# =============================================================================
# Day 14: Project
# =============================================================================

# Higher or Lower Game Project

from Day14utils import logo, vs, data
import random
from os import system, name

clear = lambda : system('cls' if name == 'nt' else 'clear')

def incScore():
    global SCORE 
    SCORE = SCORE + 1

def checkHigherOrLower(aDict, bDict):
    count = 'follower_count'
    if aDict[count] > bDict[count]:
        return 'A', aDict
    else:
        return 'B', bDict 

def printComparison(aDict, bDict):    
    aStr =  f"Compare A: {aDict['name']}, a {aDict['description']}, from {aDict['country']}"
    bStr = f"Compare B: {bDict['name']}, a {bDict['description']}, from {bDict['country']}"    
    print(aStr)
    print(vs)
    print(bStr)

def higherLower(aDict, bDict):
    print('\n')
    # ensures they are not the same
    while aDict == bDict:
        bDict = data[random.randint(0, len(data) - 1)]
    printComparison(aDict, bDict)
    gameOver = False
    while not gameOver:
        answer, corrDict = checkHigherOrLower(aDict, bDict)
        guess = input("\nWho has more followers? Type 'A' or 'B': ")
        if guess == answer:
             incScore()
             nextDict = data[random.randint(0, len(data) - 1)]
             higherLower(corrDict, nextDict)
        else:
            print("\nGame Over!")       
        gameOver = True

    
print(logo)  
while input("\nDo you want to play higher or lower? Type 'y' or 'n': ") == 'y':
    clear()  
    print(logo) 
    aDict = data[random.randint(0, len(data) - 1)]
    bDict = data[random.randint(0, len(data) - 1)]
    SCORE = 0   
    higherLower(aDict, bDict)
    print(f"\nYour final score is {SCORE}.")

print("Thanks for playing~")    
    
# =============================================================================
# End of Day 14
# =============================================================================
