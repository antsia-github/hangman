import random

class Hangman:
    #def __init__(self) -> None:
    def __init__(self, word_list, num_lives = 5.):    
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for i in self.word] # inititally ['_',...,'_']
        self.num_letters = len(set(self.word))  # number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = num_lives  # number of lives
        self.word_list = word_list 
        self.list_of_guesses = [] # A list of the guesses that have already been tried.

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            id_guess = 0
            for letter in self.word:
                if letter == guess:
                   #id_guess = self.word.index(guess)
                   self.word_guessed[id_guess] = letter
                id_guess += 1
            self.num_letters -= 1       
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f'You have {self.num_lives} lives left')

    def ask_for_input(self):
      #while True:
        print('Guess a letter and enter it as a single alphabetical character:')
        guess = input()   
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!") 
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
        print(f'The guessed word is {self.word_guessed}') 
        #print(f'The real word is {self.word}')   

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
           game.ask_for_input()
        else:
           print('Congratulations. You won the game!')
           break

word_list = ['durian', 'mangga', 'cempedak', 'rambutan', 'sharon']
play_game(word_list)