"""Defines the Faction class"""


class Faction(object):

    def __init__(self, building_blueprints):
        self.building_blueprints = building_blueprints

    def initialize(self, game, player, position):
        """Overloadable function to be called when the faction starts"""
        pass
