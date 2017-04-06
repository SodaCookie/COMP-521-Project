"""Defines the TileModifier class"""


class TileModifier(object):
    """Base class for tile modifiers
    Useful intermediary class in case more advance data relaying needed
    via callbacks from the Tile class. For now is only a tag"""

    def __init__(self):
        self.tag = None # Used to set special tiles
