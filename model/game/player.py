"""Defines the Player class"""


class Player(object):

    def __init__(self):
        self.units = set()
        self.minerals = 0
        self.faction = None
        self.max_supply = 50
        self.actionable = True

    def set_faction(self, faction):
        self.faction = faction

    def get_actions(self, game):
        if not self.actionable:
            return actions
        actions = []
        for i in range(game.board.width):
            for j in range(game.board.height):
                if not game.position_occupied((i, j)):
                    for blueprint in self.faction:
                        if blueprint.cost <= self.minerals:
                            actions.append(
                                self.create_build_action(blueprint, (i, j)))
        return actions

    def create_build_action(self, blueprint, pos):
        def callback(game):
            self.spawned_building = True
            new_building = blueprint.instantiate(pos)
            new_building.set_player(self)
            self.minerals -= blueprint.cost
        return callback

    def

    def add_unit(self, unit):
        unit.set_player(self)
        self.units.add(unit)

    def remove_unit(self, unit):
        self.units.remove(unit)
