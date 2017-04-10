from model.game.components.health import Health
from model.game.components.spawner import Spawner
from model.game.blueprint import Blueprint
from assets.units.thief_blueprint import ThiefBlueprint

class HideoutBlueprint(Blueprint):
    """Used to create a copy of a tavern (Rebels main building)"""

    def __init__(self):
        super().__init__("hideout", 10, 500, True)
        self.add_component(Health, 80)
        self.add_component(Spawner, [ThiefBlueprint()])
