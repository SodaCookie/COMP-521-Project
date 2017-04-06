"""Defines the Component class"""

class Component(object):
    """Component class is responsible for executing code for an entity."""

    def __init__(self):
        self.entity = None

    def set_entity(self, entity):
        self.entity = entity

    def get_actions(self, game):
        """Overloadable function that returns the user a list of actions"""
        return None

    def update(self, game):
        """Overloadable function that can act on the entity and the game.

        Only runs once every start of a players turn. Useful for doing something
        at the start of a players turn like gettings resources
        """
        pass
