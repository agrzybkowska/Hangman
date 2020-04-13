from game import Game

class HangmanPlay(Game):

    def __init__(self):
        super().__init__()

    def play_hangman(self):
        while Game.game_welcome(self) == "y":
            # starting a new game
            Game.new_game(self)
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


word1 = HangmanPlay()
word1.play_hangman()