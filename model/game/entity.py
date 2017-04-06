"""Defines the Entity class"""

class Entity(object):

    def __init__(self, pos=(0, 0), components=None):
        self.x = pos[0]
        self.y = pos[1]
        self.player = None
        self.components = set() if components == None else set(components)

    def set_player(self, player):
        """Sets the player who owns this entity"""
        self.player = player

    def kill(self, game):
        """Kills the entity."""
        # TODO

    def add_component(self, component):
        """Adds a component to the Entity."""
        self.components.add(component)

    def add_component_type(self, cls, *args, **kwargs):
        """Creates a new component to the Entity and returns it"""
        comp = cls(*args, **kwargs)
        self.add_component(comp)
        return comp

    def remove_component(self, cls):
        """Removes the first instance of given the class in Entity"""
        to_remove = None
        for component in self.components:
            if isinstance(component, cls):
                to_remove = component
                break
        if to_remove:
            self.components.remove(to_remove)

    def remove_components(self, cls):
        """Removes all instances of given the class in Entity"""
        self.components = set(filter(lambda comp : not isinstance(comp, cls),
                                     self.components))

    def has_component(self, cls):
        """Returns a boolean of if Entity contains a class instance"""
        for component in self.components:
            if isinstance(component, cls):
                return True
        return False
