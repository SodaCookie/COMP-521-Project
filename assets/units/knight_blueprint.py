from model.game.components.attack import Attack
from model.game.components.health import Health
from model.game.components.movable import Movable
from model.game.blueprint import Blueprint

class KnightBlueprint(Blueprint):
    """Used to create a copy of a knight (Loyalist combat unit)"""

    def __init__(self):
        super().__init__("knight", 5, 50)
        self.add_component(Health, 20)
        self.add_component(Attack, 1, 4)
        self.add_component(Movable, 2)
