from model.game.component import Component


class Movable(Component):

    def __init__(self, amount):
        self.amount = amount

    def get_actions(self, game):
        """Return a list of moveable moves."""
        pass
