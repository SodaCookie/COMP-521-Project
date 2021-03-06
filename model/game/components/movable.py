from model.game.component import Component


class Movable(Component):

    def __init__(self, movement):
        self.movement = movement

    def get_moves(self, game):
        return self._find_moves(self.unit.x, self.unit.y, set(), game, 0)

    def get_actions(self, game):
        """Return a list of Movable moves."""
        return [self.create_move_action(self.unit, x, y) for x, y in self._find_moves(
            self.unit.x, self.unit.y, set(), game, 0)]

    @staticmethod
    def create_move_action(unit, x, y):
        """Creates a move function that moves this component's unit to x, y"""
        def callback(game):
            prev_x, prev_y = unit.x, unit.y
            unit.x = x
            unit.y = y
            return Movable.create_reverse_move_action(unit, prev_x, prev_y)
        return callback

    @staticmethod
    def create_reverse_move_action(unit, x, y):
        """Creates a move function that moves this component's unit to x, y"""
        def callback(game):
            unit.x = x
            unit.y = y
        return callback

    def _find_moves(self, x, y, visited, game, depth):
        """Finds all available move via DFS."""
        neighbours = []
        visited.add((x, y))
        if (depth > self.movement):
            return []
        if (depth == self.movement):
            return [(x, y)]

        if x >= 0 and x < game.board.width:
            if x != 0: neighbours.append((x - 1, y))
            if x != game.board.width - 1: neighbours.append((x + 1, y))
        if y >= 0 and y < game.board.width:
            if y != 0: neighbours.append((x, y - 1))
            if y != game.board.height - 1: neighbours.append((x, y + 1))

        cur = game.board[x, y]
        actual_moves = [(x, y)]
        for pos in neighbours:
            # Check for height difference, check for occupy by another unit
            if cur.elevation - game.board[pos].elevation <= 1 and \
                    not game.position_occupied(pos) and \
                    game.board[pos].pathable and \
                    pos not in visited:
                visited.add(pos)
                actual_moves.extend(self._find_moves(pos[0], pos[1], visited,
                                                     game, depth + 1))
        return actual_moves
