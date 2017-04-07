from model.game.component import Component


class Spawner(Component):

    def __init__(self, units):
        self.units = units
        self._cooldown = 0

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
            unit.get_component(Spawner)._cooldown = spawn.cost
        return callback

    def get_actions(self, entities):
        space = _get_available_space(game)
        if self._cooldown == 0 and space:
            return
        else:
            return None

    def update(self, source, amount):
        if self._cooldown > 0:
            self._coo -= 1
