from model.game.components.health import Health
from model.game.components.spawner import Spawner
from model.game.components.blueprint import Blueprint
from model.game.components.zherg.units.pupa_blueprint import Pupa

class HatcheryBlueprint(Blueprint):
    """Used to create a copy of a hatchery (Zherg main building)"""

    def __init__(self):
        super().__init__("hatchery", 10, 500)
        self.add_component(Health, 80)
        self.add_component(Spawner, PupaBlueprint)
