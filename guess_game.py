#!/usr/bin/env python3
"""Number Guessing Game | Step 3"""

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Ask the user for their guess
guess = int(input("Guess the number between 1 and 10: "))

# Check the user's guess and provide hints
if guess == secret_number:
    print("You guessed it! Great job!")
elif guess > secret_number:
    print("Too high!")
elif guess < secret_number:
    print("Too low!")

