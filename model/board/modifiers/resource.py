"""Defines the Pathable TileModifier"""

from enum import Enum
from model.board.tilemodifier import TileModifier


class ResourceCategory(Enum):
    MINERAL = 1

class Resource(TileModifier):

    def __init__(self, category, amount):
        super().__init__()
        self.category = category
        self.amount = amount
