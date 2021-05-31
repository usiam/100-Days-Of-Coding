# -*- coding: utf-8 -*-
"""
Created on Mon May 31 16:04:24 2021

@author: Tahamid
"""

# =============================================================================
# Day 12
# =============================================================================

# 114. Scopes

# local scope

def drink():
    volume = 100 
    print(volume)
    
drink()
#print(volume) # not defined outside the function i.e. it's only accessible in
# the function which means it has a local scope.



# global scope

volume = 1000

def drink():
    volume = 100 
    print(f"Volume local = {volume}")
    
drink()
print(f"Volume global = {volume}") 


# volume = 1000 is accessible anywhere because it is global 

# scopes are applicable to everything not just variables

def resources():
    def water():
        volume = 100 
        print(f"Volume local = {volume}")
        
#water() # not accessible because water() function is local to the resources()
# function


# 115. No block scope

# functions create scopes in python. If/while/for loops dont so no block
# scopes in python like Java or C/C++


# 116. Modify global variables in a local scope

# to modify a global variable inside a local scope we have to say it's global
enemies = 0

def increaseEnemies():
    global enemies
    enemies += 2 # this will not work because we have not defined enemies 
    # INSIDE the local scope of this function

    print(f"Updated number of enemies = {enemies}")

# this is bad practice. We usually do not want to modify global vars 

# a better way to do this would be

def incEnemies():
    return enemies + 1
    
increaseEnemies()
enemies = incEnemies()
print(f"Global enemies = {enemies}")

# 117. Python constants and global scope

# constants are usually upper case
PI = 3.14159
URL = ''
TWITTERNAME = ''

# Day 12 Project: Number guessing game

import random
from os import system, name

clear = lambda : system('cls' if name == 'nt' else 'clear')

logo = '''
  / __|_  _ ___ ______ |_   _| |_  ___  | \| |_  _ _ __ | |__  ___ _ _ 
 | (_ | || / -_|_-<_-<   | | | ' \/ -_) | .` | || | '  \| '_ \/ -_) '_|
  \___|\_,_\___/__/__/   |_| |_||_\___| |_|\_|\_,_|_|_|_|_.__/\___|_|                                                                       
'''
def checkStatus(guess, num):
    if guess > num:
        print(">Too high.")
    elif guess < num:
        print(">Too low.")
    else:
        print(f"\nYou got it! The answer was {guess}.")

def setDifficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    if difficulty == 'easy':
        attempts = LIVES[difficulty]
    elif difficulty == 'hard':
        attempts = LIVES[difficulty] 
  
    return attempts
     
def playGame():
    attempts = setDifficulty()    
    print(f"You get {attempts} attempts.") 
    
    gameOver = False
    
    while not gameOver:  
        guess = int(input("Make a guess: "))  
        checkStatus(guess, NUMBER)
        attempts -= 1   
        
        if guess == NUMBER or attempts <= 0:
            print(f"\nGame over! The number was {NUMBER}.")
            gameOver = True
            break
        else:
            print("Guess again.")
        
        print(f"\nYou have {attempts} attempts left.")
        
print(logo)
print("Welcome to the Number Guessing Game!")
print("\nI'm thinking of a number between 1 and 100.")  
          
while input("Do you want to play the game? Type 'y' or 'n': ") == 'y':
    clear()
    NUMBER = random.randint(1, 100)
    LIVES = {'easy' : 10, 'hard': 5}
    playGame()
            
print("\nThanks for playing~")
    
# =============================================================================
# End of Day 12
# =============================================================================
