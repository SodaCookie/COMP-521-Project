from model.utility.visual_operations import *
from model.utility.board_operations import *
from model.board.board import Board

import random

blank_board = Board(10, 10)
for i in range(blank_board.width):
    for j in range(blank_board.height):
        set_pathable(blank_board, i, j, random.randint(0, 1))
        set_elevation(blank_board, i, j, random.gauss(1, 2))

visualize_board_height(blank_board)
visualize_board_pathing(blank_board)
