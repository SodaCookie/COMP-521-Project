from model.game.component import Component


class Health(Component):

    def __init__(self, amount):
        self.amount = amount

    def damage(self, amount):
        self.amount -= amount
        if self.amount <= 0:
            self.unit.kill()
