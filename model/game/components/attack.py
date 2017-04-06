from model.game.component import Component
from model.game.components.movable import Movable

class Attack(Component):

    def __init__(self, attack_range, damage, ranged=False):
        self.attack_range = attack_range
        self.damage = damage
        self.ranged = ranged
        self._actions = None

    def get_actions(self, game):
        return self._get_attacks(board)

    def _get_attacks(self, game):
        """Determine a list of attackable enemies."""
        # If entity contains a movable component then we should add that
        # to the range of possible locations to attack and create a composite
        # move attack function
        if self.entity.has_component(Movable):
            pass
        else:
            # Check every tile in range on the board
            pass
