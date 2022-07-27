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