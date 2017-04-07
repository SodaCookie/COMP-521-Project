from mode.game.faction import Faction
from model.game.components.zherg.buildings.spawningbath_blueprint import SpawningBathBlueprint
from model.game.components.zherg.buildings.hatchery_blueprint import HatcheryBlueprint


class ZhergFaction(Faction):
	"""Define the Zherg faction"""

    def __init__(self):
        super().__init__(HatcheryBlueprint, SpawningBathBlueprint);
