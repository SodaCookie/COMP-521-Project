from model.game.component import Component


class Health(Component):

    def __init__(self, amount):
        self.amount = amount

    def on_damage(self, source, amount):
        pass # TODO
