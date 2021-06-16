"""
Created on Wed Jun 11, 10 12:15:26 2021

@author: Tahamid
"""

# Error handling and exceptions

# FileNotFound Error
# KeyError
# IndexError
# TypeError

# Key words in error handling

# try - the error prone code is inside this block

# except - do this if you face an exception/error

# else - do this if there is no error

# finally - do this no matter what happens error or no error

try:
    file = open('afile.txt')
    dict = {'a': 'Apple'}
    print([dict['a']])
except FileNotFoundError: # make sure to add the anticipated error type to make sure other errors are caught
    print("File not there. Creating the file.")
    file = open('afile.txt', 'w')
    file.write("XYZ")
except KeyError as missingKey:
    print(f"The key {missingKey} cannot be found.")
else:
    stuff = file.read()
    print(stuff)
finally:
    print("Closing file.")
    file.close()

# raise - to make your own exception

while True:
    h = float(input("Enter a height in m: "))
    m = float(input("Enter a weight in kg: "))
    if h > 3:
        raise ValueError("Human heights are not above 3 m.")
    else:
        bmi =  m /(h**2)
        print(f"Your bmi is {bmi}")
        break

# KeyError handling where some posts don't havc likes.

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
  try:
    total_likes = total_likes + post['Likes']
  except KeyError:
    post['Likes'] = 0 # if there is no likes key that means the likes are 0 so we init to 0 every time we find the
                      # KeyError exception
    total_likes += 0

print(facebook_posts)
print(total_likes)

