#!/usr/bin/env python3
"""Number Guessing Game with Input Validation"""

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Initialize the turn counter
turn = 0

while turn < 3:
    # Ask the user for their guess
    guess = input("Guess the number between 1 and 10: ")

    # Validate if the input is a number
    if not guess.isdigit():
        print("Invalid input. Please enter a valid number.")
        continue

    # Convert the guess to an integer
    guess = int(guess)

    # Validate the range of the guess
    if guess < 1 or guess > 10:
        print("Invalid guess. Please enter a number between 1 and 10.")
        continue

    # Check the guess
    if guess == secret_number:
        print("You guessed it! Great job!")
        break
    elif guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")

    # Increment the turn counter
    turn += 1

print(f"The correct number was {secret_number}.")

