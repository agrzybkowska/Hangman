import hangman_words
import random
import string


class Word:

    def __init__(self):
        # initialize attributes
        self.secret_word = ""
        self.available_letters = []
        #self.letters_guessed = []
        #self.missed_lives = 10

    def word_to_guess(self):
        self.secret_word = random.choice(hangman_words.word_list)
        return self.secret_word

    def letters_list(self):
        self.available_letters = list(string.ascii_uppercase[:])
        return self.available_letters
