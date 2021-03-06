from model.game.components.health import Health
from model.game.components.spawner import Spawner
from model.game.blueprint import Blueprint
from assets.units.brigand_blueprint import BrigandBlueprint
from assets.units.ranger_blueprint import RangerBlueprint

class TavernBlueprint(Blueprint):
    """Used to create a copy of a tavern (Rebels production building)"""

    def __init__(self):
        super().__init__("tavern", 10, 300, True)
        self.add_component(Health, 30)
        self.add_component(Spawner, [BrigandBlueprint(), RangerBlueprint()])
