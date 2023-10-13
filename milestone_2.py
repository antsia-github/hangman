'''
This milestone aims to create the variables for the game.

It chooses a random word from a list of fruit, it then asks user to input a letter, 
and it will check if the input is a singe character.
'''

import random
word_list = ['durian', 'mangga', 'cempedak', 'rambutan', 'sharon']
word = random.choice(word_list)
print(word_list)
#print(word)
print('Now type a single letter :')
guess = input()

if len(guess) ==1:
    print("Good guess")
else:
    print("Oops! That is not a valid input.")

