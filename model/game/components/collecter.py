from model.game.component import Component
from model.board.modifiers.resource import Resource

class Collecter(Component):

    def __init__(self, collection_range, collection_rate, category):
        self.collection_range = collection_range
        self.collection_rate = collection_rate
        self.category = category

    def _get_resource_range(self, x, y, collection_range):
        collection_positions = set()
        for r in range(0, 1 + collection_range):
            for i in range(r):
                j = self.collection_range - i
                collection_positions.add((x + i, y + j))
                collection_positions.add((x + j, y - i))
                collection_positions.add((x - i, y - j))
                collection_positions.add((x - j, y + i))
        return collection_positions

    def update(self, game):
        """Get all in range resource tiles and add to player enemies."""
        harvested = 0
        for pos in _get_resource_range(self.unit.x, self.unit.y, self.collection_range):
            tile = game.board[pos]
            if tile:
                resource = tile.get_modifier(Resource)
                if resource and resource.category == self.category:
                    # Remove from resource from location
                    to_remove = min(resource.amount, self.collection_rate)
                    resource.amount -= to_remove
                    harvested += to_remove
                    if resource.amount == 0:
                        # If expired remove the resource
                        game.board[pos].remove_modifier(Resource)
        self.unit.player.minerals += resource_amount
