# -*- coding: utf-8 -*-
"""
Created on Fri May 28 11:24:20 2021

@author: Tahamid
"""
# =============================================================================
# Day 9
# =============================================================================

# 89. Python Dictationaries

# =============================================================================
# Dictionaries have a key which is the name we use to refer to it and each key
# has a value
# 
# dict = {Key1 : Value1, Key2 : Value2, etc}
#
# for dictionaries instead of an index we give it the key
# x = dict[Key1]
#
# adding/editing keys:
# dict[newKey/oldKey] = newValue
#
# dictionary initialization: newDict = {}
#
# we can empty a dictationary using dict = {}
#
# looping through a dictionary
#
# for key in dict: (this only prints the keys)
#   print(key)
#   print(dict[key]) (also prints the value associated to each key)
#
# =============================================================================

# 90. Grading Program Exercise

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

studentGrades = {}

for student in student_scores:
  score = student_scores[student]
  if score <= 70:
    studentGrades[student] = "Fail"
  elif score <= 80:
    studentGrades[student] = "Acceptable"
  elif score <= 90:
    studentGrades[student] = "Exceeds Expectations"
  elif score <= 100:
    studentGrades[student] = "Outstanding"

print(studentGrades)


# 91. Nesting lists and dictionaries

# =============================================================================
# We can nest lists and dictionaries inside dictionaries
# {Key1 : [list], Key2 : {dictionary}}
# =============================================================================

capitals = {
    "France": "Paris",
    "Germany": "Berlin"}

# Nesting a list in a dict

travel_log1 = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Dortmund", "Hamburg"]
    }

# Nesting a dict in a dict

travel_log2 = {
    "France" : {
        "citiesVisited" :  ["Paris", "Lille", "Dijon"],
        "bestCity" : "Paris",
        "totalVisits" : 4
        },
    "Germany" : {
        "citiesVisited" : ["Berlin", "Dortmund", "Hamburg"],
        "bestCity" : "Dortmund",
        "totalVisits" : 2
        }
    }

# Nesting a dict in a list

travel_log3 = [
    {
     "country" : "France",
     "citiesVisited" :  ["Paris", "Lille", "Dijon"],
     "bestCity" : "Paris",
     "totalVisits" : 4
     },
    { 
     "country" : "Germany",
     "citiesVisited" : ["Berlin", "Dortmund", "Hamburg"],
     "bestCity" : "Dortmund",
     "totalVisits" : 2
    }
    
    ]

# 92. Travel log updater

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, timesVisited, citiesVisited):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = timesVisited
    new_country["cities"] = citiesVisited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)

# Day 9 Project: Secret Auction with Dictionaries

from os import system, name

logo = '''
       ___________
       \         /
        )_______(
        |"""""""|_.-._,.---------.,_.-._
        |       | | |               | | ''-.
        |       |_| |_             _| |_..-'
        |_______| '-' `'---------'` '-'
        )"""""""(
       /_________\\
     .-------------.
    /_______________\\

                          
'''

def maxBid(bidDict):
    maxBid = 0
    for bidder in bidDict:
        bid = bidDict[bidder]
        if bid > maxBid:
            maxBid = bid
            maxBidder = bidder
    print(f"The winner is {maxBidder} with a bid of ${maxBid}.")
    
def addBid(bidder, bid):
    bidDict[bidder] = bid

clear = lambda: system('cls' if name=='nt' else 'clear')
#lambda function syntax: funcName = lambda parameters : expression
    
print(logo)
print("Welcome to the secret auction program.")

bidDict = {}

runProgram = True
    
while runProgram:
    bidder = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    
    addBid(bidder, bid)
    
    moreBids = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if moreBids == 'yes':
        clear()
    else:
       maxBid(bidDict)
       runProgram = False
       

# =============================================================================
# End of Day 9
# =============================================================================
