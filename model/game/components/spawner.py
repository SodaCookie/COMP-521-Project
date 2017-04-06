from model.game.component import Component


class Spawner(Component):

    def __init__(self, entities):
        self.entities = entities

    def update(self, source, amount):
        pass # TODO
