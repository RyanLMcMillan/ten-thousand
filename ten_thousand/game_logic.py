import random
from collections import Counter


def is_straight(roll_input):
    if not len(roll_input) == 6:
        return False

    for tup, idx in roll_input:
        if not (tup[1] == 1 and int(tup[0]) == idx):
            return False
        pass
    return True


def has_six_of_a_kind(roll_input):
    if roll_input[0][1] == 6:
        return True
    else:
        return False
    pass


def has_three_pairs(roll_input):
    if not len(roll_input) == 3:
        return False
    for pair in roll_input:
        if not pair[1] == 2:
            return False
    return True
    pass


def has_two_triples(roll_input):
    if not len(roll_input) == 2:
        return False
    for pair in roll_input:
        if not pair[1] == 3:
            return False
    return True
    pass


def one_case(roll_input):
    if roll_input[1] < 3:
        return roll_input[1] * 100
    else:
        return (roll_input[1] - 2) * 1000


def five_case(roll_input):
    if roll_input[1] < 3:
        return roll_input[1] * 50
    else:
        return (roll_input[1] - 2) * 500
    pass


def other_case(roll_input):
    if roll_input[1] < 3:
        return 0
    else:
        return (roll_input[1] - 2) * int(roll_input[0]) * 100
    pass


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
        print(f"tup received: {tup}")
        score = 0

        if len(tup) == 0:
            return score

        roll = Counter(tup).most_common()

        if is_straight(roll):
            # add however many points
            score += 1500
            print("straight")
            pass
        elif has_six_of_a_kind(roll):
            # add however many points
            if roll[0] == "1":
                score += 4000
                print("six of a kind")
            else:
                return other_case(roll)
            pass
        elif has_three_pairs(roll):
            # add however many points
            score += 1500
            print("three pairs")
            pass
        elif has_two_triples(roll):
            # add however many points
            score += 1200
            print("two triples")
            pass
        else:
            for pair in roll:
                if pair[0] == "1":
                    score += one_case(pair)
                elif pair[0] == "5":
                    score += five_case(pair)
                else:
                    score += other_case(pair)
                pass
            pass
        pass

        return score