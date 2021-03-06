"""Defines the Player class"""


class Player(object):

    def __init__(self):
        self.units = set()
        self.minerals = 500
        self.faction = None
        self.max_supply = 50
        self.actionable = True
        self.init_pos = ()

    def initialize(self, game, position):
        self.init_pos = position
        self.faction.initialize(game, self, position)

    def set_faction(self, faction):
        self.faction = faction

    def start_turn(self, game):
        for unit in self.units:
            unit.update(game)

    def get_actions(self, game):
        if not self.actionable or len(self.units) >= self.max_supply:
            return actions
        actions = []
        for i in range(game.board.width):
            for j in range(game.board.height):
                if not game.position_occupied((i, j)):
                    for blueprint in self.faction.building_blueprints:
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
            return self.create_reverse_build_action(new_building)
        return callback

    def create_reverse_build_action(self, unit):
        def callback(game):
            self.spawned_building = False
            self.units.remove(unit)
            self.minerals += unit.cost
        return callback

    def add_unit(self, unit):
        unit.set_player(self)
        self.units.add(unit)

    def remove_unit(self, unit):
        self.units.remove(unit)
