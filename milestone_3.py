import random

def check_guess(guess): 
  if guess.isalpha() and len(guess) == 1:
     return True
  else:
     return False
  
def ask_for_input():
  print('Enter a single alphabetical character :')
  while True:
    guess = input()   
    #if guess.isalpha() and len(guess) == 1:
    if check_guess(guess):  
      break
    else:
       "Invalid letter. Please, enter a single alphabetical character."
  return guess


word_list = ['durian', 'mangga', 'cempedak', 'rambutan', 'sharon']
word = random.choice(word_list)

guess = ask_for_input()

guess = guess.lower()

if guess in word:
   print(f"Good guess! {guess} is in the word.")
else:
   print(f"Sorry, {guess} is not in the word. Try again.")
