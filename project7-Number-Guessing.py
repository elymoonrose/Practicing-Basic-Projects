# This is a number guessing game where you will choose an initial range,
# and then you will have to guess the number that will appear within the range chosen!

import random

top_of_range = input("Please enter the range in which you want to guess: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a number larger tan 0 next time.")
        quit()
else:
    print("Please enter a number next time.")
    quit()


random_numbers = random.randint(0, top_of_range)
guesses = 0


while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time.")
        continue

    if user_guess == random_numbers:
        print("That's right!")
        break
    elif user_guess > random_numbers:
        print("You are above the correct number! Make another guess.")
    else:
        print("You are below the correct number! Make another guess")

print("You guessed it in", guesses, "guesses!")
