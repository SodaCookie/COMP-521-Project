"""Defines operation functions that can be put on the board"""

from model.board.modifiers.pathable import Pathable
from model.board.modifiers.resource import Resource


def add_resource(board, x, y, category, amount):
    board[x, y].add_modifier(Resource(category, amount))

def set_pathable(board, x, y, pathable):
    board[x, y].pathable = pathable

def set_elevation(board, x, y, new_height):
    board[x, y].elevation = new_height
