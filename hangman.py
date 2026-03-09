import os
import sys

def clear_screen():
    # Print newlines to push secret word out of scrollback buffer
    print("\n" * 100)
    os.system("cls" if os.name == "nt" else "clear")

HANGMAN_STAGES = [
    """
      -----
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
]

MAX_WRONG = len(HANGMAN_STAGES) - 1


def get_secret_word():
    while True:
        word = input("Player 1, enter the secret word: ").strip().lower()
        if word.isalpha() and len(word) >= 2:
            return word
        print("Please enter a word with at least 2 letters (letters only).")


def display(word, guessed, wrong):
    print(HANGMAN_STAGES[wrong])
    display_word = " ".join(ch if ch in guessed else "_" for ch in word)
    print(f"  Word: {display_word}")
    print(f"  Wrong guesses: {', '.join(sorted(guessed - set(word))) or 'none'}")
    print(f"  Lives left: {MAX_WRONG - wrong}")
    print()


def play():
    word = get_secret_word()
    clear_screen()
    print("Player 2, it's your turn to guess!\n")

    guessed = set()
    wrong = 0

    while wrong < MAX_WRONG:
        display(word, guessed, wrong)

        if all(ch in guessed for ch in word):
            print("Congratulations Player 2! You guessed the word!\n")
            return

        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Enter a single letter.\n")
            continue
        if guess in guessed:
            print("Already guessed that letter.\n")
            continue

        guessed.add(guess)
        if guess not in word:
            wrong += 1
            print(f"'{guess}' is not in the word.\n")
        else:
            print(f"'{guess}' is in the word!\n")

    display(word, guessed, wrong)
    print(f"Game over! The word was: {word}\n")


def main():
    while True:
        play()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break
        clear_screen()


if __name__ == "__main__":
    main()
