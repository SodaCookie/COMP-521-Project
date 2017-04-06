from model.game.component import Component
from model.game.components.movable import Movable
from model.game.components.health import Health

class Attack(Component):

    def __init__(self, attack_range, damage):
        self.attack_range = attack_range
        self.damage = damage
        self._actions = None

    def get_actions(self, game):
        return [self.create_attack_action(self, pos, target) \
            for pos, target in self._get_attacks(game)]

    @staticmethod
    def create_attack_action(unit, pos, target):
        def callback(game):
            Movable.create_move_action(unit, pos[0], pos[1])(game)
            target.get_component(Health).damage(unit.damage)
        return callback

    def _get_attack_ring(self, x, y, attack_range):
        attack_positions = set()
        for i in range(attack_range):
            j = attack_range - i
            attack_positions.add(x + i, y + j)
            attack_positions.add(x + j, y - i)
            attack_positions.add(x - i, y - j)
            attack_positions.add(x - j, y + i)
        return attack_positions

    def _get_attacks(self, game):
        """Determine a list of attackable enemies."""
        # If unit contains a movable component then we should add that
        # to the range of possible locations to attack and create a composite
        # move attack function
        attackable = []
        if self.unit.has_component(Movable):
            availble_moves = self.unit.get_component(Movable).get_moves(game)
            for x, y in availble_moves:
                for ax, ay in self._get_attack_ring(x, y, self.attack_range):
                    unit = game.position_occupied(ax, ay)
                    # If we find a unit and it is owned by a different player
                    if unit and unit.player != self.unit.player and
                            unit.has_component(Health):
                        attackable.append(((x, y), unit))
        else:
            # Check every tile in range on the board
            # Above, left, right, below
            x, y = self.unit.x, self.unit.y
            for ax, ay in self._get_attack_ring(x, y, self.attack_range):
                unit = game.position_occupied(ax, ay)
                # If we find a unit and it is owned by a different player
                if unit and unit.player != self.unit.player and
                        unit.has_component(Health)::
                    attackable.append(((x, y), unit))
        return attackable
