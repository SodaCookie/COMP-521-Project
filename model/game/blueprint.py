"""Defines the Blueprint class"""
from model.game.unit import Unit

class Blueprint(object):
    """Used to create new copies of a unit class."""

    def __init__(self, name, timecost, cost, is_building=False):
        self.name = name
        self.timecost = timecost
        self.cost = cost
        self.components = []
        self.is_building = is_building

    def add_component(self, cls, *args, **kwargs):
        """Adds a component to the blueprint to be used during instantiate"""
        self.components.append((cls, args, kwargs))

    def instantiate(self, pos=(0, 0)):
        """Creates and returns a new copy of the given unit"""
        components = []
        for cls, args, kwargs in self.components:
            components.append(cls(*args, **kwargs))
        new_unit = Unit(self.name, self.timecost, self.cost, pos, components)
        new_unit.is_building = self.is_building
        return new_unit
