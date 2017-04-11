"""Defines operation functions that can be put on the board"""

from model.board.board import Board
from model.board.modifiers.resource import Resource


def copy_board(dest, src, rect=None, pos=None):
    """Copies tiles from src board to destinations.

    If rect is given than a rect, starting from the x,, y corner from the src
    will be copied to dest at it's topleft corner. If pos is also specified
    than the copied rect will start at dest at the given position."""
    if rect:
        x, y, width, height = rect
        if not pos:
            pos = (0, 0) # default top left
        for i in range(width):
            for j in range(height):
                dest[i + pos[0], j + pos[1]] = src[i + x, j + y]
    else:
        min_width = min(src.width, dest.width)
        min_height = min(src.height, dest.height)
        for i in range(min_width):
            for j in range(min_height):
                dest[i, j] = src[i, j]

def increase_width(board):
    new_board = Board(board.width + 1, board.height)
    copy_board(new_board, board)
    return new_board

def decrease_width(board):
    new_board = Board(board.width - 1, board.height)
    copy_board(new_board, board)
    return new_board

def increase_height(board):
    new_board = Board(board.width, board.height + 1)
    copy_board(new_board, board)
    return new_board

def decrease_height(board):
    new_board = Board(board.width, board.height - 1)
    copy_board(new_board, board)
    return new_board

def add_resource(board, x, y, category, amount):
    if board[x, y].has_modifier(Resource):
        mod = board[x, y].get_modifier(Resource)
        if mod.category == category:
            mod.amount += amount
            return
    board[x, y].add_modifier(Resource(category, amount))

def remove_resource(board, x, y, category, amount):
    if board[x, y].has_modifier(Resource):
        mod = board[x, y].get_modifier(Resource)
        if mod.category == category:
            mod.amount -= amount
            if mod.amount <= 0:
                board[x, y].remove_modifier(mod)

def set_pathable(board, x, y, pathable):
    board[x, y].pathable = pathable

def set_elevation(board, x, y, new_height):
    board[x, y].elevation = new_height

def add_spawn(board, position):
    board.start_locations.add(position)

def remove_spawn(board, position):
    board.start_locations.remove(position)
