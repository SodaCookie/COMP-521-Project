from model.game.components.attack import Attack
from model.game.components.health import Health
from model.game.components.moveable import Moveable
from model.game.components.blueprint import Blueprint

class LongbowmanBlueprint(Blueprint):
    """Used to create a copy of a Longbowman (Loyalist combat unit)"""

    def __init__(self):
        super().__init__("longbowman", 7, 80)
        self.add_component(Health, 8)
        self.add_component(Attack, 4, 2)
        self.add_component(Moveable, 3)