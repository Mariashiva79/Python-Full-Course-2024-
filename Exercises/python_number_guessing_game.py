import random

lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number, highest_number)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_number} and {highest_number}")

while is_running:

    guess = input(f"Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_number or guess > highest_number:
            print("That number is out of range")
            print(f"Please, select a number between {lowest_number} and {highest_number}")
        elif guess < answer:
            print("Too low!! Try again!")
        elif guess > answer:
            print("Too high!! Try again!")
        else:
            print(f"CORRECT NUMBER!! The answer was {answer}")
            print(f"Number os guesses: {guesses}")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Please, select a number between {lowest_number} and {highest_number}")

