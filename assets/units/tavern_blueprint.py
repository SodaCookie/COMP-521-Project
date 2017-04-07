from model.game.components.health import Health
from model.game.components.spawner import Spawner
from model.game.components.blueprint import Blueprint
from assets.units.brigand_blueprint import BrigandBlueprint
from assets.units.ranger_blueprint import RangerBlueprint

class TavernBlueprint(Blueprint):
    """Used to create a copy of a tavern (Rebels production building)"""

    def __init__(self):
        super().__init__("tavern", 10, 300)
        self.add_component(Health, 50)
        self.add_component(Spawner, BrigandBlueprint, RangerBlueprint)
