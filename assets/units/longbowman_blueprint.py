from model.game.components.attack import Attack
from model.game.components.health import Health
from model.game.components.movable import Movable
from model.game.blueprint import Blueprint

class LongbowmanBlueprint(Blueprint):
    """Used to create a copy of a Longbowman (Loyalist combat unit)"""

    def __init__(self):
        super().__init__("longbowman", 7, 80)
        self.add_component(Health, 5)
        self.add_component(Attack, 3, 4)
        self.add_component(Movable, 3)
