from model.game.components.health import Health
from model.game.components.spawner import Spawner
from model.game.components.blueprint import Blueprint
from assets.units.knight_blueprint import KnightBlueprint
from assets.units.longbowman_blueprint import LongbowmanBlueprint

class BarracksBlueprint(Blueprint):
    """Used to create a copy of a Barracks (Loyalist production building)"""

    def __init__(self):
        super().__init__("barracks", 10, 300)
        self.add_component(Health, 50)
        self.add_component(Spawner, KnightBlueprint, LongbowmanBlueprint)
