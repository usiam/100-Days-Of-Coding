"""
Created on Wed Jun 10, 10 12:15:26 2021

@author: Tahamid
"""

import random

# newDict = {newKey : newVal for item in list} creating a dict from a list

names = ['Alex', 'Brittany', 'Dave', 'Caroline', 'Freddie', 'Elenor']

studentScores = {student: random.randint(0, 100) for student in
                 names}  # gives each student a random score between 0, 100
print(studentScores)

# newDict = {newKey : newVal for (key, val) in dict.items()} # creating a new dict from an old dict
# dict.items() returns a list of tuples of the form (key, value)
# newDict = {newKey : newVal for (key, val) in dict.items() if test} # conditional dict comprehension

passedStudents = {student: score for (student, score) in studentScores.items() if score >= 60}
print(passedStudents)

# A dictionary of the words in a sentence and the number of letters in that word
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
wordLenDict = {word: len(word) for word in sentence.split(" ")}
print(wordLenDict)

# convert the celsius temp to fahrenheit temp in a dict of celsius temp everyday of a particular week

weatherInC = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weatherInF = {day : round(((temperature * (9/5)) + 32), 2) for (day, temperature) in weatherInC.items()}

print(weatherInF)


