import random
from collections import Counter


class Banker:
    def __init__(self):
        self.score = 0
        self.round_score = 0

    def add_score(self, points):
        self.round_score += points

    def abort_round_score(self):
        self.round_score = 0

    def commit_round_score(self):
        self.score = 0
        self.score += self.round_score

    def get_score(self):
        return self.score


class GameTracker:
    def __init__(self):
        self.run_game = True
        self.round_number = 1
        self.die_count = 6
        self.round_score = 0
        self.total_score = 0
        self.banker = Banker()

    def continue_playing(self):
        return self.run_game

    def quit(self):
        self.run_game = False

    def add_round(self):
        self.round_number += 1
        self.die_count = 6

    def get_round(self):
        return self.round_number

    def set_die(self, die_count):
        self.die_count = die_count

    def get_die_count(self):
        return self.die_count

    def get_banker(self):
        return self.banker


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
        roll = Counter(tup).most_common()

        if len(tup) == 0:
            return score

        print(f"print roll: {roll}")

        # straight
        if len(roll) == 6:
            score += 1500

        #6 of a kind
        if roll[0][1] == 6:

            if roll[0][0] == 1:
                score += 4000
                return score
            score += int(roll[0][0]) * 400
            return score

        #5 of a kind
        elif roll[0][1] == 5:
            if roll[0][0] == 1:
                score += 3000

            elif len(roll) > 1:
                if roll[1][0] == 5:
                    score += 50

                elif roll[1][0] == 1:
                    score += 100

            else:
                score += int(roll[0][0]) * 300
                return score

        # 4 of a kind
        elif roll[0][1] == 4:
            if roll[0][0] == "1":
                score += 2000

            else:
                score += int(roll[0][0]) * 200
                pass

            if len(roll) == 2:
                if roll[1][0] == "5":
                    score += 50 * roll[1][1]

                elif roll[1][0] == "1":
                    score += 100 * roll[1][1]

                elif roll[2][0] == "5":
                    score += 50 * roll[2][1]

                elif roll[2][0] == "1":
                    score += 100 * roll[2][1]

            elif len(roll) > 1:
                if roll[1][0] == "5":
                    score += 50 * roll[1][1]

                elif roll[1][0] == "1":
                    score += 100 * roll[1][1]

            else:
                score += int(roll[0][0]) * 200

            return score


        # double 3 of a kind
        elif len(roll) == 2 and roll[0][1] == 3 and roll[1][1] == 3:
            if roll[0][1] == 3 and roll[1][1] == 3:
                if roll[0][0] == 1:
                    score += 1000
                    return score + int(roll[1][0]) * 100

                if roll[1][0] == 1:
                    score += 1000
                    return score + roll[0][0] * 100

                return roll[0][0] * 100 + roll[1][0] * 100

        # 3 of a kind
        elif roll[0][1] == 3:
            if roll[0][0] == 1:
                score += 1000

            elif len(roll) > 1:
                if roll[1][0] == "5":
                    score += 50 * roll[1][1]

                elif roll[1][0] == "1":
                    score += 100 * roll[1][1]

                elif roll[2][0] == "5":
                    score += 50 * roll[2][1]

                elif roll[2][0] == "1":
                    score += 100 * roll[2][1]

                elif roll[3][0] == "5":
                    score += 50 * roll[3][1]

                elif roll[3][0] == "1":
                    score += 100 * roll[3][1]

            else:
                score += int(roll[0][0]) * 100
                return score

        # 3 pairs
        elif len(roll) > 2 and roll[0][1] == 2 and roll[1][1] == 2 and roll[2][1] == 2:
            score += 1500
            return score

        # pair 1's
        elif roll[0][1] == 2 and roll[0][0] == "1":
            score += 200

        # pair 5's
        elif roll[0][1] == 2 and roll[0][0] == "5":
            score += 100

        elif len(roll) > 1:
            if roll[1][1] == 2 and roll[1][0] == "5":
                score += 100

        # single 1's
        elif roll[0][0] == "1":
            score += 100

        # single 5's
        elif roll[0][0] == "5":
            score += 50

        print(f"resultant score: {score}")

        return score


def game_round(game_tracker):
    banker = game_tracker.get_banker()

    print(f"starting round {game_tracker.get_round()}")
    print(f"Rolling {game_tracker.get_die_count()} dice...")
    #test = [2, 1, 2, 2, 2, 4]
    roll = GameLogic.roll_dice(game_tracker.get_die_count())
    print(f"*** {tuple(roll)} ***")
    print("Enter dice to keep or (q)uit")
    cont = input("> ")
    if cont == "q":
        banker.commit_round_score()
        print(f"Thanks for playing. You earned {banker.get_score()} points.")
        game_tracker.quit()
        return

    die_count = game_tracker.get_die_count() - len(cont)
    game_tracker.set_die(die_count)
    round_score = GameLogic.calculate_score(tuple(cont))

    if round_score == 0:
        banker.abort_round_score()

    print(f"You have {round_score} unbanked points and {die_count} dice remaining")

    print("(r)oll again, (b)ank your points or (q)uit:")
    action = input("> ")
    if action == "q":
        print(f"Thanks for playing. You earned {banker.get_score()} points.")
        game_tracker.quit()
        return
    elif action == "r":
        game_round(game_tracker)
        pass
    elif action == "b":
        banker.add_score(round_score)
        pass

    banker.commit_round_score()


def play_game():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    start = input("> ")

    if start == "n":
        print("OK. Maybe another time")
        return

    game_tracker = GameTracker()

    game_round(game_tracker)

    while game_tracker.continue_playing():
        game_tracker.add_round()
        game_round(game_tracker)

        if game_tracker.get_round() == 20:
            print(f"Thank you for playing; you earned {game_tracker.get_score()} points.")
            pass
        pass


if __name__ == "__main__":
    play_game()