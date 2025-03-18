#!/usr/bin/env python3
"""Number Guessing Game with Simplified Turn Logic"""

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Initialize the turn counter
turn = 0

while turn < 3:
    # Ask the user for their guess
    guess = int(input("Guess the number between 1 and 10: "))

    # Validate the guess
    if guess < 1 or guess > 10:
        print("Invalid guess. Please enter a number between 1 and 10.")
    elif guess == secret_number:
        print("You guessed it! Great job!")
        break
    elif guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")

    # Increment the turn counter
    turn += 1

print(f"The correct number was {secret_number}.")

