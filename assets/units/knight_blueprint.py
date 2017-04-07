from model.game.components.attack import Attack
from model.game.components.health import Health
from model.game.components.moveable import Moveable
from model.game.components.blueprint import Blueprint

class KnightBlueprint(Blueprint):
    """Used to create a copy of a knight (Loyalist combat unit)"""

    def __init__(self):
        super().__init__("knight", 5, 50)
        self.add_component(Health, 10)
        self.add_component(Attack, 1, 3)
        self.add_component(Moveable, 5)
