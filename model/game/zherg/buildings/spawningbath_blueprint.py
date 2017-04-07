from model.game.components.health import Health
from model.game.components.spawner import Spawner
from model.game.components.blueprint import Blueprint
from model.game.components.zherg.units.zhergling_blueprint import ZherglingBlueprint
from model.game.components.zherg.units.ericalisk_blueprint import EricalickBlueprint

class SpawningBathBlueprint(Blueprint):
    """Used to create a copy of a spawning bath (Zherg production building)"""

    def __init__(self):
        super().__init__("spawningbath", 10, 300)
        self.add_component(Health, 50)
        self.add_component(Spawner, ZherglingBlueprint, EricalistBlueprint)
