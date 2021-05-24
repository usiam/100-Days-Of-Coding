# -*- coding: utf-8 -*-
"""
Created on Sun May 23 15:55:47 2021

@author: Tahamid
"""

# =============================================================================
# Day 4
# =============================================================================

# 39. Randomization

'''
Random is a built in module in python library. 

To use modules we must import them. 

import random imports the module

random is now an object and we have access to all of its functions accessed using random.functionName
'''

import random

# generating a random integer between [a, b] using random.randint(a, b)
randomInt = random.randint(1, 10)
print(randomInt)


# generating a random floating point number between [0, 1) using random.random()
randFloat = random.random()
print(randFloat)

# generating a random floating point number between [0, a) using random.random() * a
randFloat5 = random.random() * 5
print(randFloat5)


# generating a random floating point number between [a, b) using random.uniform(a, b)
randomFloat = random.uniform(0, 5)
print(randomFloat)

# 40. Heads or Tails RNG

headArt = '''
           __-----__
      ..;;;--'~~~`--;;;..
    /;-~IN GOD WE TRUST~-.\
   //      ,;;;;;;;;      \\
 .//      ;;;;;    \       \\
 ||       ;;;;(   /.|       ||
 ||       ;;;;;;;   _\      ||
 ||       ';;  ;;;;=        ||
 ||LIBERTY | ''\;;;;;;      ||
  \\     ,| '\  '|><| 1995 //
   \\   |     |      \  A //
    `;.,|.    |      '\.-'/
      ~~;;;,._|___.,-;;;~'
          ''=--'

        - Daniel C Au -
'''

tailArt = '''

               ,,==="""""""===,,
           ,==""' |\ |   /\   `""==,
        ,="'|\    | \|  /__\   /\  `"=,
      /"    |,"\  |  | /'  `\ /  )     "\
    /"  ,"  |                 `\/    /|  "\
   /'  |   ,                       /",|   `\
  /'   ",/"                           |    `\
 /'      I=I=I               ,d8ba,___      `\
/'     I=8=8=8=I_I_          88888P"""       `\
|   xXXXXXXXXXXXXXXXxIxx    ,888"             |
| ~XXXXXXXXXXXXXXX~-~-~-~-~ d888~-~-~-~-~-~-~ |
| ~-~-~-~-~-~-~-~-,aad888ba,8888,-~-~-~-~-~-~ |
| ~-~-~-~-~-~-,ad888888888888888b-~-~-~-~-~-~ |
\ ~-~-~-~-~,ad8888888888888888888-~-~-~-~-~-~ /
`\ -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~- /'
 `\ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~,-,~~~~~ /'
  `\    /"\         1 9 9 4        \ /\    /'
   `\  "\,/'                   |\   `\ `  /'
     "\      /""\   |    |     |,'\     /"
       `"=,_ \__/   |__  |__   |    ,="'  Normand
          `""=,__             __,=""'     Veilleux
               ``""=========""''


'''
prompt = input("Do you want to flip a coin? Y or N: ").upper()

if prompt == "Y":
    outcome = random.randint(0,1)

    if outcome == 0:
        print("You got heads\n\n")
        print(headArt)
    else:
        print("You got tails\n\n")
        print(tailArt)
else:
    print("Alright! Have a good day.")



# 41. List data structure

# =============================================================================
# list structure

# listName = [item1, item2, item3, ...]

# lists are used to store multiple data that are somehow related and can have order 

# to get the i-th item in the list we use: listName[i] where i ranges from 0 to len(list) - 1.

# Python also has negative indexing.
# listName[-1] gives the last item and then listName[-2] gives 2nd to last item.

# You can also change items.
# listName[0] = newData

# You can add things to the list at the end.
# listName.append(newData)

# You can add things to the list at any position.
# listName.insert(position, newData)

# You can 'extend' a list with another list.
# list2Name = ["a", "b", "c", ...]
# list1Name.extend(list2Name)

# *** Any time you come across a new data structure just look at the documentation 
# and see the possible things you can do with it.*** 
# =============================================================================

# 42. Program to randomly choose someone to pay for everyone in a list

names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ") # str.split("what_to_split_at") creates a 
# list of items from a string and separates the string at "what_to_split_at"

randNum = random.randint(0, len(names) - 1)

payPerson = names[randNum]

print(f"{payPerson} is going to buy the meal today!")

# 43. Nested lists 

# You can make lists of lists. The way to do that is 
# listName = [listName1, listName2]


# 44. Code challenge: Treasure map

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

colNum = int(position[0]) - 1 # - 1 because indexing in python starts from 0
rowNum = int(position[1]) - 1

map[rowNum][colNum] = "X"

print(f"{row1}\n{row2}\n{row3}")

# 45. Day 4 Project: Rock/Paper/Scissor

import random

print("\nWelcome to Rock-Paper-Scissor")

moves = ["rock", "paper", "scissor"]
rand = random.randint(0, 2)
comMove = moves[rand]

playerMove = input("What is your move? Rock or Paper or Scissor?\n").lower()

if playerMove == comMove:
    print(f"The computer also chose {comMove}. It's a draw!")
elif playerMove == "rock" :
    if comMove == "scissor":
        print(f"Computer chose {comMove}. You win!")
    else:
        print(f"Computer chose {comMove}. You lose!")
elif playerMove == "paper":
    if comMove == "rock":
        print(f"Computer chose {comMove}. You win!")
    else:
        print(f"Computer chose {comMove}. You lose!")
elif playerMove == "scissor":
    if comMove == "paper":
        print(f"Computer chose {comMove}. You win!")
    else:
        print(f"Computer chose {comMove}. You lose!")
else:
    print(f"Your move, {playerMove}, is illegal.")









































# =============================================================================
# End Of Day 4
# =============================================================================
