"""
Created on Wed Jun 10, 10 12:15:26 2021

@author: Tahamid
"""

# List comprehension allows us to create a new list from an old list

# the syntax is newList = [newItem for item in itemList]

numbers = [1, 2, 3]
newNumbers = [(number + 1) for number in numbers]

print(newNumbers)

# this code is doing the same thing as

# numbers = [1, 2, 3]
# newNumbers = []
# for number in numbers:
#     number = number + 1
#     newNumbers.append(number)


name = 'Tahamid'
newList = [char for char in name]  # this will just create a list of characters in the name
print(newList)

# comprehension can be used with any sequence in python

# Sequences in python = list, range, string, tuple, etc

doubledList = [(num * 2) for num in range(1, 5)]
print(doubledList)

# Now we will take this a step further. We will also use conditionals inside the comprehension. This
# is called a conditional list comprehension

evenList = [num for num in range(100) if (num % 2 == 0)]
# you read this as, for num in range(100) if num % 2 == 0 then appen num to evenList

print(evenList)

names = ['Alex', 'Brittany', 'Dave', 'Caroline', 'Freddie', 'Elenor']
fourLetterNamesList = [name for name in names if (len(name) <= 4)]
longNamesUpperCase = [name.upper() for name in names if (len(name) > 5)]
print(fourLetterNamesList)
print(longNamesUpperCase)

# squaring numbers in a list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

# list of numbers in both lists i.e data overlap

with open('file1.txt') as file1:
    firstList = file1.read().split('\n')
    firstList = firstList[:len(firstList) - 1]  # last one is an empty string
with open('file2.txt') as file2:
    secondList = file2.read().split('\n')
    secondList = secondList[:len(secondList) - 1]

result = [int(num) for num in firstList if num in secondList]
print(result)
