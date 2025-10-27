# Project 2: The perfect guess

# We are going to write a program that generates a random number and asks 
# the user to # guess it.

# If the player's guess is higher than the actual number, the program 
# displays "Lower number please". Similarly, if the user's guess is too 
# low, the program prints "higher number please* When the user guesses 
# the correct number, the program displays the number of guesses the 
# player used to arrive at the number.

# Hint: Use the random module.

from random import randint

guess = randint(1, 100)
no_of_guesses = 0

while True:
    num = int(input("Guess the number between 1 to 100: "))

    if 1 > num  or num > 100:
        print("Invalid number....!\nGuess a number between 1 to 100\n")
        no_of_guesses += 1
    elif num == guess:
        no_of_guesses += 1
        print(f"You have guess the number '{guess}' correctly in '{no_of_guesses}' times")
        break
    elif num > guess:
        no_of_guesses += 1
        print("You have guessed wrong number.\nPlease enter lower number")
    else :
        no_of_guesses += 1
        print("You have guessed wrong number.\nPlease enter higher number")