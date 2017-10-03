#!/usr/bin/env python

import random

secret = random.randint(1,20)
done = False

def check_guess(guess):
    if guess > secret:
        return 1
    elif guess < secret:
        return -1
    elif guess == secret:
        return 0

def get_guess():
    return int(input("What is your guess? "))

print("I have chosen a number between 1 and 20. Guess what number it is.")

while not done:
    response = check_guess(get_guess())
    if response > 0:
        print("Your guess is too high.")
    elif response < 0:
        print("Your guess is too low.")
    elif response == 0:
        print("You guessed correctly!")
        done = True

