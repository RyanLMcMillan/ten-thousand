class Banker:
    def __init__(self):
        self.score = 0
        self.round_score = 0

    def add_score(self, points):
        self.round_score += points

    def get_round_score(self):
        return self.round_score

    def abort_round_score(self):
        self.round_score = 0

    def commit_round_score(self):
        self.score += self.round_score
        self.round_score = 0

    def get_score(self):
        return self.score