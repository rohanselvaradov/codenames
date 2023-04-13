import numpy as np

class Codenames:
    def __init__(self, vocab):
        """
        Args:
            vocab (list): list of lower case strings
        """
        self.vocab = vocab
        # self.spymaster_a = Player()
        # self.spymaster_b = Player()
        # self.guesser_a = Player()
        # self.guesser_b = Player()
        self.first_turn = np.random.choice(['R', 'B'])
        self.current_turn = self.first_turn
        self.words = np.random.choice(self.vocab, 25)
        self.revealed = np.zeros(25)
        self.board = 8 * ['R', 'B'] + 7 * ['N'] + ['X'] + [self.first_turn]
        np.random.shuffle(self.board)
        print("{} goes first".format(self.first_turn))

    def get_other_team(self):
        return 'R' if self.current_turn == 'B' else 'B'

    def play(self):
        # current team offers a clue
        # current team guesses
        # check if game is over after each guess
        # if not, switch current team and repeat
        pass

    def get_clue(self):
        # `current_team spymaster`.get_clue() (maybe store Player objects in dict of self.players)
            # print board map for user (colour coded)
            # get clue (str and int)
            # validate clue
                # str must be in words and not revealed
                # int must > 0 and <= 8
        pass

    def make_guesses(self, clue):
        # print board map and clue for user (not colour coded)
        # for i in range(clue[1]):
            # guess = self.get_guess()
            # self.revealed[np.where(self.words == guess)] = 1
            # if self.is_terminal():
                # return self.is_terminal()
            # if self.board[np.where(self.words == guess)] != self.current_turn:
            #    break 
        pass

    def get_guess(self):
        # while True:
            # guess = `current_team guesser`.guess()
                # print board map for user
                # get guess as input (str)
            # validate guess
            # guess in self.words and self.revealed(np.where(self.words == guess)) == 0
        # return guess
        pass

    def is_terminal(self):
        # First check if assassin is revealed
        if self.revealed(np.where(self.board == 'X')) == 1:
            return self.get_other_team()
        # Check if all words of current team are revealed
        if np.all(self.revealed[np.where(self.board == self.current_turn)] == 1):
            return self.current_turn
        # Check if all words of other team are revealed
        if np.all(self.revealed[np.where(self.board == self.get_other_team())] == 1):
            return self.get_other_team()