"""Defines the Unit class"""


class Unit(object):

    def __init__(self, name, timecost, cost, pos=(0, 0), components=None):
        self.x = pos[0]
        self.y = pos[1]
        self.player = None
        self.timecost = timecost
        self.cost = cost
        self.name = name
        self.components = set() if components == None else set(components)

    def set_player(self, player):
        """Sets the player who owns this unit"""
        self.player = player

    def kill(self):
        """Kills the unit."""
        self.player.remove_unit(self)

    def get_component(self, cls):
        """Returns the first instance of given the class in Unit"""
        to_remove = None
        for component in self.components:
            if isinstance(component, cls):
                return component

    def get_components(self, cls):
        """Returns all instances of given the class in Unit"""
        return set(filter(lambda comp : isinstance(comp, cls), self.components))

    def add_component(self, component):
        """Adds a component to the Unit."""
        component.set_unit(self)
        self.components.add(component)

    def add_component_type(self, cls, *args, **kwargs):
        """Creates a new component to the Unit and returns it"""
        comp = cls(*args, **kwargs)
        self.add_component(comp)
        return comp

    def remove_component(self, cls):
        """Removes the first instance of given the class in Unit"""
        to_remove = None
        for component in self.components:
            if isinstance(component, cls):
                to_remove = component
                break
        if to_remove:
            self.components.remove(to_remove)

    def remove_components(self, cls):
        """Removes all instances of given the class in Unit"""
        self.components = set(filter(lambda comp : not isinstance(comp, cls),
                                     self.components))

    def has_component(self, cls):
        """Returns a boolean of if Unit contains a class instance"""
        for component in self.components:
            if isinstance(component, cls):
                return True
        return False
