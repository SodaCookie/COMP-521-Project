from model.game.components.attack import Attack
from model.game.components.health import Health
from model.game.components.movable import Movable
from model.game.blueprint import Blueprint

class BrigandBlueprint(Blueprint):
    """Used to create a copy of a brigand (Rebels combat unit)"""

    def __init__(self):
        super().__init__("brigand", 5, 60)
        self.add_component(Health, 40)
        self.add_component(Attack, 1, 5)
        self.add_component(Movable, 1)
