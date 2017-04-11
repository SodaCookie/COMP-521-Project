from model.board.board import Board
from model.game.player import Player
from model.game.components.health import Health

from itertools import chain
import traceback
import random
import sys

class Game(object):

    def __init__(self, width=10, height=10, board=None):
        if board:
            self.board = board
        else:
            self.board = Board(width, height)
        self.player1 = Player()
        self.player2 = Player()
        self.running = True
        self.player1_controller = None
        self.player2_controller = None
        self.current_player = None
        self.winner = None
        self.deadlock_count = 0

    def set_player1_controller(self, controller):
        self.player1_controller = controller

    def set_player2_controller(self, controller):
        self.player2_controller = controller

    def initialize(self):
        # Get the start position for player 1
        spawn_locations = set(self.board.start_locations)
        if spawn_locations:
            p1_position = random.choice(list(spawn_locations))
            spawn_locations.remove(p1_position)
        else:
            # If there are no more spawn locations than just find a random location
            p1_position = (random.randint(0, self.board.width - 1),
                           random.randint(0, self.board.height - 1))
            while not self.board[p1_position].pathable:
                p1_position = (random.randint(0, self.board.width - 1),
                               random.randint(0, self.board.height - 1))
        self.player1.initialize(self, p1_position)

        # Get the start position for player 2
        if spawn_locations:
            p2_position = random.choice(list(spawn_locations))
        else:
            # If there are no more spawn locations than just find a random location
            p2_position = (random.randint(0, self.board.width - 1),
                           random.randint(0, self.board.height - 1))
            while not self.board[p2_position].pathable or p2_position == p1_position:
                p2_position = (random.randint(0, self.board.width - 1),
                               random.randint(0, self.board.height - 1))
        self.player2.initialize(self, p2_position)

    def run(self):
        self.current_player = self.player1
        unit, action = None, None
        count = 1
        sys.stdout.write("Playing turn: %d" % count)
        sys.stdout.flush()
        while self.running and count <= 30:
            sys.stdout.write('\b'*len(str(count-1))+str(count))
            sys.stdout.flush()
            # Run inputs for ai/player
            try:
                if self.current_player == self.player1 and self.player1_controller:
                    self.player1_controller.run(self.player1, self)
                if self.current_player == self.player2 and self.player2_controller:
                    self.player2_controller.run(self.player2, self)
            except:
                print("ERROR - ALERT! ALERT! ALERT!")
                traceback.print_exc()
            self.end_phase()
            self.begin_phase()
            # Check for win condition
            # Player 1 win condition
            for unit in self.player1.units:
                if unit.is_building:
                    break
            else:
                self.running = False
                self.winner = 1
                break
            # Player 2 win condition
            for unit in self.player2.units:
                if unit.is_building:
                    break
            else:
                self.running = False
                self.winner = -1
                break

            if self.deadlock_count > 6: # passed turns for 3 rounds
                # Draw condition
                break
            count += 1
        if not self.winner:
            self.winner = self.evaluate_winner(self)

    def begin_phase(self):
        for unit in self.current_player.units:
            unit.actionable = True
        self.current_player.actionable = True

    def end_phase(self):
        # Toggle the current player
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def evaluate_winner(self, game):
    	base = 0.2    # finetune this if needed
    	player1_value = self.calc_player_value(base, game.player1.units)
    	player2_value = self.calc_player_value(base, game.player2.units)
    	return self.calc_relative_value(player1_value, player2_value)

    def calc_player_value(self, base, units):
    	value = 0
    	for unit in units:
    		unit_value = unit.cost * (base + (1 - base) * unit.get_component(Health).current_hp_percent())
    		value += unit_value
    	return value

    def calc_relative_value(self, value1, value2):
    	max_val = max(value1, value2)
    	min_val = min(value1, value2)

    	ratio = min(2, max_val / min_val) / 2
    	return -ratio if value1 > value2 else ratio

    def position_occupied(self, pos):
        """Helper function that returns a unit if that position is taken"""
        for unit in chain(self.player1.units, self.player2.units):
            if pos[0] == unit.x and pos[1] == unit.y:
                return unit
        return None
