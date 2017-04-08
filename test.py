from model.utility.visual_operations import *
from model.utility.board_operations import *
from model.board.board import Board
from assets.factions.loyalists_faction import LoyalistFaction
from assets.factions.rebels_faction import RebelsFaction

import random

# blank_board = Board(10, 10)
# for i in range(blank_board.width):
#     for j in range(blank_board.height):
#         set_pathable(blank_board, i, j, random.randint(0, 1))
#         set_elevation(blank_board, i, j, random.gauss(1, 2))
#
# visualize_board_height(blank_board)
# visualize_board_pathing(blank_board)

from model.game.game import Game

g = Game(10, 10)
g.player1.set_faction(LoyalistFaction())
g.player2.set_faction(RebelsFaction())
g.initialize()
g.run()
visualize_board_height(g.board, True)
