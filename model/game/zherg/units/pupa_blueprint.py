from model.game.components.health import Health
from model.game.components.moveable import Moveable
from model.game.components.collecter import Collecter
from model.game.components.blueprint import Blueprint

class PupaBlueprint(Blueprint):
    """Used to create a copy of a pupa (Zherg collecter unit)"""

    def __init__(self):
        super().__init__("pupa", 2, 20)
        self.add_component(Health, 5)
        self.add_component(Moveable, 2)
        self.add_component(Collecter, 2, 25, MINERAL)
