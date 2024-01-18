import numpy as np

class Player:
    def __init__(self, team, role, words):
        self.role = role
        self.words = words
        self.guesses = np.zeros(25)

    def get_clue(self):
        