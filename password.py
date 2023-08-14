#!usr/bin/env python
"""
A random password generator made using Python.

Easy to say/Easy to read idea came from lastpass.com

The memorable passwords came from phoenixNAP,
'Strong Password Ideas For Greater Protection' article
by ANDREJA VELIMIROVIC (Nov 10, 2021)
https://phoenixnap.com/blog/strong-great-password-ideas

Overall idea came from https://www.geeksforgeeks.org/create-a-random-password-generator-using-python/#
"""

import string
import random

password = []

pass_length = int(input("Please enter a password pass_length 0 < n < 50: "))
if pass_length < 1 or pass_length >= 50:
    print("Your password pass_length must be between 1 and 49 characters long")
    exit()

characterList = "" # Contains all the characters used in password generation
easy_to_say = False
easy_to_read = False
avoidance = [] # Determines if any characters should be avoided in the password

easy_to_say_input = input("Should the password be easy to say (Avoid numbers and special characters) [y/n]? ")
if easy_to_say_input.lower() == "y":
    easy_to_say = True

easy_to_read_input = input("Should the password be easy to read (Avoid o, 0, i, l, and 1) [y/n]? ")
if easy_to_read_input.lower() == "y":
    easy_to_read = True

avoidance_input = 0
if easy_to_say:
    avoidance_input = int(input('''Anything else you'd like to avoid?
                        1. UPPERCASE
                        2. lowercase
                        5. Skip (include all the above)
                        '''))
else:
    avoidance_input = int(input('''Anything else you'd like to avoid?
                            1. UPPERCASE
                            2. lowercase
                            3. NUM83RS
                            4. $YM&OLS
                            5. Skip (include all the above)
                            '''))

reading_avoidance = False
if avoidance_input != 5:
    reading_avoidance = True

while reading_avoidance:
    if avoidance_input == 1:
        avoidance.append(1)
    elif avoidance_input == 2:
        avoidance.append(2)
    elif avoidance_input == 3:
        avoidance.append(3)
    elif avoidance_input == 4:
        avoidance.append(4)
    else:
        print("Please choose a number 1 - 5")
    
    if len(avoidance) == 3 or (len(avoidance) == 1 and easy_to_say):
        reading_avoidance = False
        continue
    else:
        print("Anything else you'd like to avoid?")
        if not (1 in avoidance or 2 in avoidance):
            print("1. UPPERCASE")
            print("2. lowercase")
        if not (3 in avoidance):
            print("3. NUM83RS")
        if not (4 in avoidance):
            print("4. $YM&OLS")
        print("5. Skip (include all the above)")
    avoidance_input = int(input(""))
    if avoidance_input != 5:
        reading_avoidance = True
    else:
        reading_avoidance = False

# Only use allowed characters
if 1 in avoidance:
    characterList = string.ascii_lowercase
elif 2 in avoidance:
    characterList = string.ascii_uppercase
else:
    characterList = string.ascii_letters
if (not (3 in avoidance)) and not easy_to_say:
    characterList += string.digits
if (not (4 in avoidance)) and not easy_to_say:
    characterList += string.punctuation

if easy_to_read:
    if not (3 in avoidance): # Split was my old way of doing it, until I found replace()
        plcehldr = characterList.split("01", 1)
        characterList = "".join(plcehldr)
    characterList = characterList.replace("o", "")
    characterList = characterList.replace("O", "")
    characterList = characterList.replace("i", "")
    characterList = characterList.replace("I", "")
    characterList = characterList.replace("l", "")
    characterList = characterList.replace("L", "")

for i in range(pass_length):
    randomChar = random.choice(characterList)
    password.append(randomChar)

print()
print("Your generated password is:")
print("".join(password))
