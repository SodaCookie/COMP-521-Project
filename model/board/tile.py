"""Defines the Tile class"""
import inspect


class Tile(object):
    """ Simple container class holding unique information on the board
    """

    def __init__(self, x, y, elevation=0, mods=None):
        self.x = x
        self.y = y
        self.elevation = elevation
        self.pathable = True
        # If no mod list is given then create a empty tile by default
        self.mods = set() if mods == None else set(mods)

    def add_modifier(self, modifier):
        """Adds a given modifer to the Tile"""
        self.mods.add(modifier)

    def remove_modifier(self, mod_or_modtype):
        """Removes the first instance of mod_type in Tile or mod"""
        if inspect.isclass(mod_or_modtype):
            to_remove = None
            for mod in self.mods:
                if isinstance(mod, mod_or_modtype):
                    to_remove = mod
                    break
            if to_remove:
                self.mods.remove(to_remove)
        else:
            self.mods.remove(mod_or_modtype)

    def remove_modifiers(self, mod_type):
        """Removes all instances of mod_type in Tile"""
        self.mods = set(filter(lambda mod : not isinstance(mod, mod_type),
                               self.mods))

    def has_modifier(self, mod_type):
        """Returns a boolean of if Tile contains a TileModifier instance"""
        for mod in self.mods:
            if isinstance(mod, mod_type):
                return True
        return False

    def get_modifier(self, mod_type):
        """Returns a boolean of if Tile contains a TileModifier instance"""
        for mod in self.mods:
            if isinstance(mod, mod_type):
                return mod
        return None
