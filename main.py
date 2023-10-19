import __main__
import random
# Today we are gonna make guess the number game

import random

def guess_number(x):
    randomint = random.randint(1, x)
    guess = 0
    while guess != randomint:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess > randomint:
            print("Your guess is too high, try again")
        elif guess < randomint:
            print("Your guess is too low, try again")
    print("You guessed it correctly!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = high
        feedback = input(f"Is my {guess} too high (h), too low (l), or correct (c)? Type 'h', 'l', or 'c': ")
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print("Congrats!")

x = int(input("Up to which number do you want to guess? "))
guess_number(x)
computer_guess(x)