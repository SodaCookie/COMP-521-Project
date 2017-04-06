"""Defines the Player class"""


class Player(object):

    def __init__(self):
        self.units = set()
        self.minerals = 0

    def add_unit(self, unit):
        unit.set_player(self)
        self.units.add(unit)

    def remove_unit(self, unit):
        self.units.remove(unit)
