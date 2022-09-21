from functions import *
from game_data import data
from art import logo, vs

print(logo)

random1 = randomNum()
random2 = randomNum()

print(f"Compare A: {data[random1]['name']}, {data[random1]['description']}, from {data[random1]['country']}")

print(vs)

print(f"Compare A: {data[random2]['name']}, {data[random2]['description']}, from {data[random2]['country']}")