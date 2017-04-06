"""Defines the Board class"""
from model.tile import Tile

class Board(object):
    """Board class provides board state and helper functions."""

    def __init__(self, width, height):
        """Initializes a blank board of 0 elevation."""
        self.width = width
        self.height = height
        self._board = [[Tile(i, j) for j in range(height)]
            for i in range(width)]

    def __getitem__(self, key):
        return self._board[key[0]][key[1]]
