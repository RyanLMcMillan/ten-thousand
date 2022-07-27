import random
from collections import Counter
from banker import Banker

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