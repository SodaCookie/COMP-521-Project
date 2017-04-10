"""Defines useful change methods on the board for the experiment"""
from model.utility.board_operations import *
from model.board.modifiers.resource import *
from copy import deepcopy
import random
import numpy as np

def merge_boards(left, right):
    # copy one fragment from left board to the right board
    dest = deepcopy(right)
    min_width = min(left.width, right.width)
    min_height = max(left.height, right.height)
    copy_width = random.randint(2, min_width)
    copy_height = random.randint(2, min_height)
    copy_x = random.randint(0, left.width - copy_width)
    copy_y = random.randint(0, left.height - copy_height)

    dest_x = random.randint(0, right.width - copy_width)
    dest_y = random.randint(0, right.height - copy_height)
    copy_board(dest, left, (copy_x, copy_y, copy_width, copy_height),
               (dest_x, dest_y))
    return dest

_mutation_distribution = {
    "increase_width"    :   10 / 100,
    "decrease_width"    :   10 / 100,
    "increase_height"   :   10 / 100,
    "decrease_height"   :   10 / 100,
    "add_resource"      :   10 / 100,
    "remove_resource"   :   10 / 100,
    "change_pathable"   :   10 / 100,
    "change_elevation"  :   10 / 100,
    "add_spawn"         :   10 / 100,
    "remove_spawn"      :   10 / 100
}

def mutate_board(board):
    distribution = dict(_mutation_distribution)
    if board.width <= 5:
        del distribution["decrease_width"]
    if board.height <= 5:
        del distribution["decrease_height"]
    if board.width <= 5:
        del distribution["increase_width"]
    if board.width <= 5:
        del distribution["increase_width"]
    if not board.start_locations:
        del distribution["remove_spawn"]

    p = np.array(distribution.values()) / sum(distribution.values())
    mutation = np.random.choice(distribution.keys(), p=p)

    # Execute the mutation
    new_board = deepcopy(board)
    if mutation == "increase_width":
        new_board = increase_width(new_board)
    elif mutation == "decrease_width":
        new_board = decrease_width(new_board)
    elif mutation == "increase_height":
        new_board = increase_height(new_board)
    elif mutation == "decrease_height":
        new_board = decrease_width(new_board)
    elif mutation == "add_resource":
        for i in range(1):
            add_resource(new_board, random.randint(0, new_board.width - 1),
                         random.randint(0, new_board.height - 1),
                         ResourceCategory.MINERAL, 500)
    elif mutation == "remove_resource":
        for i in range(1):
            remove_resource(new_board, random.randint(0, new_board.width - 1),
                         random.randint(0, new_board.height - 1),
                         ResourceCategory.MINERAL, 500)
    elif mutation == "change_pathable":
        for i in range(1):
            pos = (random.randint(0, new_board.width - 1),
                   random.randint(0, new_board.height - 1))
            set_pathable(new_board, pos[0], pos[1], not new_board[pos].pathable)
    elif mutation == "change_elevation":
        for i in range(1):
            pos = (random.randint(0, new_board.width - 1),
                   random.randint(0, new_board.height - 1))
            set_elevation(new_board, pos[0], pos[1], not new_board[pos].pathable)
    elif mutation == "add_spawn":
        for i in range(1):
            pos = (random.randint(0, new_board.width - 1),
                   random.randint(0, new_board.height - 1))
            add_spawn(new_board, pos)
    elif mutation == "remove_spawn":
        for i in range(1):
            remove_spawn(new_board, random.choice(new_board.start_locations))
    return new_board
