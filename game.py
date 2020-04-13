from word import Word
from letters_actions import Letters

class Game(Letters):

    def __init__(self):
        super().__init__()


    def game_welcome(self):
        # starting question
        play_or_not = input("Do you want to play the Hangman Game? Type y for Yes and n for No.   ").lower()
        while play_or_not not in ["y", "n"]:
            play_or_not = input("Invalid input. Try again. \n"
                                "Do you want to play the Hangman Game? Type y for Yes and n for No.   ").lower()
        else:
            return play_or_not

    def new_game(self):
        # reset all assigned values to the attributes
        Word.word_to_guess(self)
        Word.letters_list(self)
        Letters.letters_guessed_reset(self)
        Letters.missed_lives_reset(self)

    def available_letters_display(self):
        return ' '.join(self.available_letters)

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
        # game over statements
        if "_" not in self.word_status():
            print(f"{self.word_status()} \n"
                  f"Congratulations! You won! The secret word was {self.secret_word}")
        else:
            print(f"Game over! You lost. The secret word was {self.secret_word}")



