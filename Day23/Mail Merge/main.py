"""
Created on Wed Jun 9, 10 12:15:26 2021

@author: Tahamid
"""

nameFile = "Input/Names/invited_names.txt"
letterFile = "Input/Letters/starting_letter.txt"
readytosendFilePath = "Output/ReadyToSend/"

with open(nameFile) as namesFile:
    names = namesFile.read().split('\n')

with open(letterFile) as file:
    content = file.read()
    for name in names:
        finalLetter = content.replace('[name]', name)
        Letter = finalLetter.replace('Angela', 'Tahamid')
        with open(f"{readytosendFilePath}letter_for_{name}.txt", mode='w') as writeToFile:
            writeToFile.write(Letter)
