from model.game.components.health import Health
from model.game.components.movable import Movable
from model.game.components.collecter import Collecter
from model.game.blueprint import Blueprint
from model.board.modifiers.resource import ResourceCategory


class WorkerBlueprint(Blueprint):
    """Used to create a copy of a worker (Loyalist collecter unit)"""

    def __init__(self):
        super().__init__("worker", 2, 20)
        self.add_component(Health, 5)
        self.add_component(Movable, 2)
        self.add_component(Collecter, 2, 50, ResourceCategory.MINERAL)
