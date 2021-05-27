# -*- coding: utf-8 -*-
"""
Created on Thu May 27 17:04:04 2021

@author: Tahamid
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    encodedMsg = ""
    for letter in text:
        oldIndInAlph = alphabet.index(letter)
        newIndInAlph = (oldIndInAlph + shift) % len(alphabet)
        encodedMsg += alphabet[newIndInAlph]
    print(f"The encoded text is {encodedMsg}.")

# =============================================================================
# the line: newIndInAlph = (shift + oldIndInAlph) % len(alphabet)
# is required to ensure you can shift any alphabet without facing a
# indexoutofbound error. The modulus gives the remainder so before the total
# is less than len(alphabet) it returns total and anything above len(alphabet) 
# it returns the remainder.
#
# a soft solution to the problem would be just extending the alphabet list
# with another alphabet list (alphabet.extend(alphabet)).
# It is a soft solution because it would still 
# face a index error for certain shifts unlike the current solution
# =============================================================================

def decrypt(text, shift):
    decodedMsg = ""
    for letter in text:
        oldIndInAlph = alphabet.index(letter)
        newIndInAlph = (oldIndInAlph - shift) % len(alphabet)
        decodedMsg += alphabet[newIndInAlph]
    print(f"The decoded message is {decodedMsg}.")    


logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

thankYou = '''
.▀█▀.█▄█.█▀█.█▄.█.█▄▀　█▄█.█▀█.█─█
─.█.─█▀█.█▀█.█.▀█.█▀▄　─█.─█▄█.█▄█
'''