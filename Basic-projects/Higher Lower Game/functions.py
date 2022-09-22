import random
from game_data import data

def randomNum():
    return random.randint(0, len(data) - 1)
