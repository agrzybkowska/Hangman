import hangman_words
import string
import random
import hangman_graphic


class LetterWord:
    def __init__(self):
        # initialize attributes
        self.secret_word = ""
        self.available_letters = []
        self.letters_guessed = []
        self.missed_lives = 10

    def word_to_guess(self):
        self.secret_word = random.choice(hangman_words.word_list)
        return self.secret_word

    def letters_list(self):
        self.available_letters = list(string.ascii_uppercase[:])
        return self.available_letters

    def letter_input(self):
        # get user input
        letter = input("What's your guess letter?   ").upper()
        return letter

    def valid_character(self, letter):
        # checks if input is valid and displays available letters
        while letter.isalpha() is False or len(letter) > 1 or letter not in self.available_letters:
            if letter.isalpha() is False:
                letter = input("Incorrect input. Numbers and special characters are not allowed. Try again\n"
                               "What's your guess letter?   ").upper()
            elif len(letter) > 1:
                letter = input("Incorrect input. Only one letter is allowed. Try again.\n"
                               "What's your guess letter?   ").upper()
            else:
                letter = input("The letter was already chosen. Try again.\n"
                               "What's your guess letter?   ").upper()
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

