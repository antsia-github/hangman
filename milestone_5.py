import random

class Hangman:
    '''
    This class is used to represent the Hangman game.

    Attributes:
        word (list): the word to be guessed
        word_guessed (list):A list of the letters of the word, with _ for each letter not yet guessed. 
        num_letters (int): The number of UNIQUE letters in the word that have not been guessed yet
        num_lives (int):The number of lives the player has at the start of the game.
        list_of_guesses (list): A list of the guesses that have already been tried
    '''

    def __init__(self, word_list, num_lives = 5.):    
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for i in self.word] # inititally ['_',...,'_']
        self.num_letters = len(set(self.word))  # number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = num_lives  # number of lives
        #self.word_list = word_list  # not necessary as an attribute
        self.list_of_guesses = [] # A list of the guesses that have already been tried.

    def check_guess(self, guess):
        ''' 
        This function checks if a character is part of the word to be guessed.

        If it is one of the correct character, it will fill the word_guess list 
        with this character and update the number of remaining letters to be guessed. 
        If it is not part of the word, it will update the number of opportunities left 
        to guess the next letter.    
      
        Args:
            guess (str): the character which needs checking 
        '''        
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
        '''
        This function asks for an input (a character) from the user 
      
        It checks if the character either is valid, has been tried, 
        or is part of the word to be guessed. It also updates 
        the list of letters which have been guessed by the user. 
        '''      

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
    '''
    This function runs the Hangman game.
      
    It sets the number of maximum valid attempts that user have in guessing the selected word. 
    It creates an instance of the Hangman class and uses the public attributes and method of the 
    object to runs the game.
      
    Args:
          word_list (list): A list of words from which the word to be guessed is drawn
    '''      

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