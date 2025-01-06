import random

import ascii_art as art
from words import words


def get_random_word() -> str:
    """Return word chosen at random."""
    random.seed()
    return random.choice(words).upper()


def hangman() -> None:
    """Play Hangman, a word guessing terminal game."""
    print(art.logo)
    print("Welcome to Hangman! Can you guess the word before it's too late?")

    answer = get_random_word()
    word_display = ["_" for _ in answer]
    lives = 6
    guessed_letters = []

    print(art.stages[lives])
    print(f"Word: {"".join(word_display)}")

    while "_" in word_display and lives > 0:
        print(f"{lives} lives left!") if lives > 1 else print(f"{lives} life left!")
        guess = input("Guess a letter: ").upper()

        if guess in guessed_letters:
            print(f"You already guessed {guess}!")
        elif guess in answer:
            for index, letter in enumerate(answer):
                if letter == guess:
                    word_display[index] = guess
        else:
            lives -= 1
            print(f"{guess} is not in the word! You lose one life.")

        guessed_letters.append(guess)
        print(art.stages[lives])
        print(f"Word: {"".join(word_display)}")

    print("You win!") if lives > 0 else print(f"You lose! The word was {answer}.")


if __name__ == "__main__":
    hangman()
