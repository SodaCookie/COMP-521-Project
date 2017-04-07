from model.game.components.attack import Attack
from model.game.components.health import Health
from model.game.components.moveable import Moveable
from model.game.components.blueprint import Blueprint

class ZherglingBlueprint(Blueprint):
    """Used to create a copy of a zhergling (Zherg combat unit)"""

    def __init__(self):
        super().__init__("zhergling", 5, 50)
        self.add_component(Health, 10)
        self.add_component(Attack, 1, 3)
        self.add_component(Moveable, 5)
