import random

def check_guess(guess): 
  ''' 
  This function checks if a character is a single letter 
  '''

  if guess.isalpha() and len(guess) == 1:
     return True
  else:
     return False

# def ask_for_input():
#   print('Enter a single alphabetical character :')
#   while True:
#     guess = input()   
#     #if guess.isalpha() and len(guess) == 1:
#     if check_guess(guess):  
#       break
#     else:
#        "Invalid letter. Please, enter a single alphabetical character."
#   return guess


def ask_for_input():
  '''
  This function asks for an input from the user

  It calls the check_guess function to check if the guess is a valid single character. 
  '''
  print('Enter a single alphabetical character :')
  guess = input()   
  #check if the guess is a single letter
  status = check_guess(guess)  
  return guess, status


word_list = ['durian', 'mangga', 'cempedak', 'rambutan', 'sharon']
word = random.choice(word_list)

while True:
  guess, status = ask_for_input()   
  if status:  
    break
  else:
    print("Invalid letter. Please, enter a single alphabetical character.")

guess = guess.lower()

if guess in word:
   print(f"Good guess! {guess} is in the word.")
else:
   print(f"Sorry, {guess} is not in the word. Try again.")
