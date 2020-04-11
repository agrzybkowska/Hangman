import hangman_words
import string
import random
import hangman_graphic

class Hangman:
    def __init__(self, secret_word):
        self.secret_word = secret_word
        self.letters_guessed = []
        self.available_letters = list(string.ascii_uppercase[:])
        self.missed_lives = 10

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

    def available_letters_display(self):
        return ' '.join(self.available_letters)

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

    def word_status(self):
        # shows progress of the game
        progress = []
        for item in self.secret_word:
            if item in self.letters_guessed:
                progress.append(item)
            else:
                progress.append("_")
        return ' '.join(progress)

    def game_over(self):
        if "_" not in self.word_status():
            print(f"{self.word_status()} \n"
                  f"Congratulations! You won! The secret word was {self.secret_word}")
        else:
            print(f"Game over! You lost. The secret word was {self.secret_word}")

    def game_welcome(self):
        play_or_not = input("Do you want to play the Hangman Game? Type y for Yes and n for No.   ").lower()
        while play_or_not not in ["y", "n"]:
            play_or_not = input("Invalid input. Try again. \n"
                                "Do you want to play the Hangman Game? Type y for Yes and n for No.   ").lower()
        else:
            return play_or_not

    def new_game(self):
        self.secret_word = random.choice(hangman_words.word_list)
        #print(self.secret_word)
        self.available_letters = list(string.ascii_uppercase[:])
        self.letters_guessed.clear()
        self.missed_lives = 10

    def play_hangman(self):
        while self.game_welcome() == "y":
            self.new_game()
            print("Welcome to the Hangman Game!")
            print(self.missed_lives)
            # play if you still have lives and your word is not guessed
            while self.missed_lives > 0 and "_" in self.word_status():
                # prints available lives
                print(f"You have {self.missed_lives} lives left")
                # print current progress
                print(self.word_status())
                print(f"Your available letters are:   {self.available_letters_display()}")
                # user input
                user_input = self.letter_input()
                # check if input is valid
                self.valid_character(user_input)
                # if letter is correct add it to the list of guessed letter
                self.letter_correct(user_input)
                # if letter is not correct print the message and take away one life
                self.letter_incorrect(user_input)
            else:
                # print the outcome of the game
                self.game_over()
        else:
            print("No worries. See you soon. Bye.")

def play_game():
    random_word = random.choice(hangman_words.word_list)
    word1 = Hangman(random_word)


#print(random_word)
word1 = Hangman()
word1.play_hangman()
#print(word1.letter_input())
#print(word1.invalid_character("BA"))
#Hangman.play_hangman()