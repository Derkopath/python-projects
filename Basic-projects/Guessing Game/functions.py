import random

def randomNumber():
    return random.randint(1, 100)

def attemptsRemaining(attempts):
        return f"You have {attempts} attempts remaining to guess the number."

def game(attempts, guess_number):
    right_number = True

    print(attemptsRemaining(attempts))

    while right_number:
        if attempts == 0:
                print('You loose!')
                break
            
        player_guess = int(input("Make a guess: "))

        if player_guess == guess_number:
            print("You Win!")
            break

        elif player_guess < guess_number:
            print("Too low. \nGuess again.")
            attempts -= 1
            print(attemptsRemaining(attempts))

        elif player_guess > guess_number:
            print("Too high. \nGuess again.")
            attempts -= 1
            print(attemptsRemaining(attempts))
