"""
Group: 3
Author: Samuel Lara and Ethan Liu
Date: 8/24/22
Description: A program that prompts the user to guess a number between 1 and 100 and continues to do so until the 
user has chosen the correct number.
"""

import random
import check_input

#generates random number asks user to start guessing
random_number = random.randint(1, 100)
attempts = 0
correct = False
guess = check_input.get_int_range("I'm thinking of a number. Make a guess (1-100): ", 1, 100)

#runs the program until the user guesses the correct number and adds attempts for every try
while not correct:
    if guess == random_number:
        attempts += 1
        print("Correct!  You got it in " + str(attempts) + " tries.")
        correct = True
    elif guess > random_number:
        attempts += 1
        guess = check_input.get_int_range("Too high! Guess again (1-100):", 1, 100)
    elif guess < random_number:
        attempts += 1
        guess = check_input.get_int_range("Too low! Guess again (1-100):", 1, 100)