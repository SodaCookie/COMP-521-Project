from model.game.component import Component


class Spawner(Component):

    def __init__(self, unit_blueprints):
        self.unit_blueprints = unit_blueprints
        self.cooldown = 0

    def _get_available_space(self, game):
        positions = set()
        x, y = self.unit.x, self.unit.y
        i, j = 0, 1
        positions.add(x + i, y + j)
        positions.add(x + j, y - i)
        positions.add(x - i, y - j)
        positions.add(x - j, y + i)

        available = set()
        for px, py in positions:
            # Check if in bounds
            if 0 <= px < game.board.width and 0 <= py < game.board.height:
                unit = game.position_occupied(ax, ay)
                if not unit:
                    return (px, py)
        return Nones

    @staticmethod
    def create_spawn_action(unit, pos, spawn):
        def callback(game):
            # Put on cooldown
            unit.get_component(Spawner).cooldown = spawn.timecost
            # Initate at position
            new_unit = spawn.instantiate(pos)
            # Set player owner
            new_unit.set_player(unit.player)
            # Remove minerals
            unit.player.minerals -= spawn.cost
        return callback

    def get_actions(self, game):
        space = _get_available_space(game)
        if self.cooldown == 0 and space and len(self.unit.player.units) \
                < self.unit.player.max_supply:
            actions = []
            for blueprint in self.unit_blueprints:
                if blueprint.cost <= self.unit.player.minerals:
                    actions.append(self.create_spawn_action(
                        self.unit, space, blueprint))
            return actions
        else:
            return None

    def update(self, source, amount):
        if self.cooldown > 0:
            self.cooldown -= 1
