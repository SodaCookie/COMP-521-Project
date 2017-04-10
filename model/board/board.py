"""Defines the Board class"""
from model.board.tile import Tile

class Board(object):
    """Board class provides board state and helper functions."""

    def __init__(self, width, height):
        """Initializes a blank board of 0 elevation."""
        self.width = width
        self.height = height
        self.start_locations = set()
        self._board = [[Tile(i, j) for j in range(height)]
            for i in range(width)]

    def __getitem__(self, key):
        if 0 <= key[0] < self.width and 0 <= key[1] < self.height:
            return self._board[key[0]][key[1]]
        return None

    def __setitem__(self, key, value):
        self._board[key[0]][key[1]] = value
