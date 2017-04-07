from model.game.components.health import Health
from model.game.components.spawner import Spawner
from model.game.components.blueprint import Blueprint
from assets.units.worker_blueprint import WorkerBlueprint

class KeepBlueprint(Blueprint):
    """Used to create a copy of a Keep (Loyalist main building)"""

    def __init__(self):
        super().__init__("keep", 10, 500)
        self.add_component(Health, 80)
        self.add_component(Spawner, WorkerBlueprint)
