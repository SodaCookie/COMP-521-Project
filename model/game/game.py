from model.board.board import Board
from model.game.player import Player

from itertools import chain

class Game(object):

    def __init__(self, width, height):
        self.board = Board(width, height)
        self.player1 = Player()
        self.player2 = Player()

    def position_occupied(self, pos):
        for unit in chain(self.player1.units, self.player2.units):
            if pos[0] == unit.x and pos[1] == unit.y:
                return unit
        return None
