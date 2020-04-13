import hangman_words

import random
import hangman_graphic
from word import Word


class Letters(Word):

    messages = {'guessLetter': "What's your guess letter?   ",
                'incorrectInput': "Incorrect input.",
                'numSpecChar': "Numbers and special characters are not allowed.",
                'again': "Try again",
                'oneLetter': "Only one letter is allowed.",
                'chosenLetter': "The letter was already chosen"
                }

    def __init__(self):
        # initialize attributes
        super().__init__()
        self.letters_guessed = []
        self.missed_lives = 10


    def letter_input(self):
        # get user input
        letter = input(f"{self.messages['guessLetter']}").upper()
        return letter

    def valid_character(self, letter):
        # checks if input is valid and displays available letters
        while letter.isalpha() is False or len(letter) > 1 or letter not in self.available_letters:
            if letter.isalpha() is False:
                letter = input(f"{self.messages['incorrectInput']} {self.messages['numSpecChar']} "
                               f"{self.messages['again']}\n"
                               "What's your guess letter?   ").upper()
            elif len(letter) > 1:
                letter = input(f"{self.messages['incorrectInput']} {self.messages['oneLetter']} "
                               f"{self.messages['again']}\n"
                               f"{self.messages['guessLetter']}").upper()
            else:
                letter = input(f"{self.messages['incorrectInput']} {self.messages['chosenLetter']}"
                               f" {self.messages['again']}\n"
                               f"{self.messages['guessLetter']}").upper()
        else:
            return self.available_letters.remove(letter)

    def letter_correct(self, letter):
        # adds letter to the list of guessed letters
        if letter in self.secret_word:
            self.letters_guessed.append(letter)
            print("You have guessed a letter!")

    def letter_incorrect(self, letter):
        # if letter is not in the secret word than a life is taken
        if letter not in self.secret_word:
            self.missed_lives -= 1
            print("Sorry, incorrect letter.")
            return hangman_graphic.lives_num(self.missed_lives)

    def letters_guessed_reset(self):
        return self.letters_guessed.clear()

    def missed_lives_reset(self):
        self.missed_lives = 10
        return self.missed_lives


# x = Letters()
# print(x.letter_input())