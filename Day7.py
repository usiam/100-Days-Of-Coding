# -*- coding: utf-8 -*-
"""
Created on Wed May 26 15:47:39 2021

@author: Tahamid
"""

# =============================================================================
# Day 7
# =============================================================================

# BUILD A VERSION OF YOUR OWN HANGMAN GAME

import random
import Day7utils

logo = Day7utils.logo
stages = Day7utils.stages
lb = Day7utils.lineBreak

word_list = Day7utils.word_list

word = random.choice(word_list)
lives = 6

# initialize a list using
# listName = [initValue] * listSize
display = ['_'] * len(word)

# =============================================================================
# we can also initiate using a loop
# 
# for i in range(len(word)):
#     display += '_'
# =============================================================================

print(logo)

print("\n")

print(display)

# =============================================================================
# gameOver = False
# while gameOver:
#   take guess
#   for loop:
#       if letter matches guess:
#           change the display's element in that index to guess
#   print display
#   if "_" not in display:
#       gameOver = True
# =============================================================================

while display.count('_') != 0 and lives != 0:
    guess = input("\nGuess a letter: ").lower()
    print(lb)
    
    # enumerate keeps track of both index and value and we can start enumerating
    # from any position in the iterable
    for index, letter in enumerate(word): 
        if letter == guess:
          display[index] = guess
    if guess not in word:
        lives -= 1
       
    print(stages[lives])
    print(display)
   
# =============================================================================
# we can also use a simple for loop instead of enumerate
# for i in range(len(word)):
#     letter = word[i]
#     if letter == guess:
#       display[i] = guess
#     else:
#         print("Wrong")
# =============================================================================

if lives == 0:
    print(f"\n{lb}")
    print(f"\nThe word was {word}.")
    print("You lose!")
else:
    print(f"\n{lb}")
    print("\nYou win!")


# =============================================================================
# End of Day 7
# =============================================================================
