from model.game.component import Component


class Collecter(Component):

    def __init__(self, collection_range):
        self.collection_range = collection_range

    def update(self, game):
        """Get all in range resource tiles and add to player enemies."""
        pass
