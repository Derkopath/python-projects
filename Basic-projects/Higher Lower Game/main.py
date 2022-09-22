from functions import *
from game_data import data
from art import logo, vs

print(logo)

points = 0
while True:
    random1 = randomNum()
    random2 = randomNum()

    print(f"Compare A: {data[random1]['name']}, {data[random1]['description']}, from {data[random1]['country']}")

    print(vs)

    print(f"Against B: {data[random2]['name']}, {data[random2]['description']}, from {data[random2]['country']}")

    choose = input("'A' or 'B':")

    if choose == 'A' and data[random1]['follower_count'] > data[random2]['follower_count']:
        
        points += 1

    elif choose == 'B' and data[random2]['follower_count'] > data[random1]['follower_count']:
        points += 1

    else:
        print(f"Sorry, that's wrong. Final score: {points}")
        break
