from functions import *

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

attempts = 0
guess_number = randomNumber()

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty != "easy" and difficulty != "hard":
    raise Exception("Sorry, you can only choose 'easy' or 'hard' difficulty.")

elif difficulty == "easy":

    attempts = 10
    game(attempts, guess_number)
        
elif difficulty == "hard":

    attempts = 5
    game(attempts, guess_number)