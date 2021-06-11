"""
Created on Wed Jun 9, 10 12:15:26 2021

@author: Tahamid
"""

scoreFile = open('score.txt')
content = scoreFile.read()
print(content)
scoreFile.close()

# another way to open files

with open('score.txt', mode='r') as file:  # dont need to close with this method. mode = 'r' means read only
    fileContent = file.read()
    print(fileContent)

with open('score.txt', mode='a') as fileWrite:  # mode = 'a' allows us to append to it
    # mode = 'w' rewrites the whole file and also creates the file if it doesnt exist
    string = "\nThis is the added text"
    fileWrite.write(string)
