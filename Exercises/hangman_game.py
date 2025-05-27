# juego del ahorcado

from wordslist import words
import random

# creando el diccionario del ahorcado

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")
               }


# Game

def display_man(wrong_guesses):
    print("******************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("******************")


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = list("_" * len(answer))  # Mostrar barras bajas según la longitud de la palabra
    guesses_letter = set()
    is_running = True
    wrong_guesses = 0
    max_attempts = 6

    while is_running and wrong_guesses < max_attempts:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue
        if guess in guesses_letter:
            print(f"{guess} is already guessed")
            continue

        letter_found = False

        for i in range(len(answer)):
            if answer[i] == guess:
                hint[i] = guess
                letter_found = True
        if not letter_found:
            wrong_guesses += 1

        guesses_letter.add(guess)

        if wrong_guesses >= max_attempts:
            print("++++++++++++++++++++++++++++++++++++++++++")
            print(f"Game over, the secret word is \033[1m{answer}\033[0m")
            print("++++++++++++++++++++++++++++++++++++++++++")
        else:
            display_man(wrong_guesses)
            display_hint(hint)

        if "_" not in hint:
            display_man(wrong_guesses)
            print(f"\033[1m{answer.upper()}\033[0m")
            print("YOU WIN!!!")
            is_running = False


if __name__ == "__main__":
    main()
