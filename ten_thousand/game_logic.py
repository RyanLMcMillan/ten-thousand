import random
from collections import Counter

class GameLogic:
    def __init__(self):
        pass

    @staticmethod
    def roll_dice(num):
        rolls = []
        while len(rolls) < num:
            rolls.append(random.randint(1, 6))
        return tuple(rolls)

    @staticmethod
    def calculate_score(tup):
        roll = Counter(tup).most_common()



        return int







