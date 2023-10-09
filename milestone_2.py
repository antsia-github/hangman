import random

word_list = ['durian', 'mangga', 'cempedak', 'rambutan', 'sharon']
word = random.choice(word_list)
#print(word_list)
print(word)
print('Now type a single letter :')
guess = input()

if len(guess) ==1:
    print("Good guess")
else:
    print("Oops! That is not a valid input.")

