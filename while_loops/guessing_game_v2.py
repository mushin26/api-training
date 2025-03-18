#!/usr/bin/env python3
"""Number Guessing Game with Turn Limit"""

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Initialize the turn counter
turn = 0

while True:
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

    # Check if this was the last turn
    if turn == 3:
        print(f"Sorry, you're out of turns! The correct number was {secret_number}.")
        break

