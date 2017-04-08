from model.board.board import Board
from model.game.player import Player

from itertools import chain
import random

class Game(object):

    def __init__(self, width, height):
        self.board = Board(width, height)
        self.player1 = Player()
        self.player2 = Player()
        self.running = True
        self.player1_controller = None
        self.player2_controller = None
        self.current_player = None

    def set_player1_controller(self, controller):
        self.player1_controller = controller

    def set_player2_controller(self, controller):
        self.player2_controller = controller

    def initialize(self):
        # Get the start position for player 1
        spawn_locations = set(self.board.start_locations)
        if spawn_locations:
            p1_position = random.choice(spawn_locations)
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
            p2_position = random.choice(spawn_locations)
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
        while self.running:
            # Run inputs for ai/player
            if self.current_player == self.player1 and self.player1_controller:
                unit, action = self.player1_controller.run(self.player1, self)
            if self.current_player == self.player2 and self.player2_controller:
                unit, action = self.player2_controller.run(self.player2, self)
            if action:
                self.execute(unit, action)
                unit, action = None, None

            # Check for win condition
            # Player 1 win condition
            for unit in self.player1.units:
                if unit.is_building:
                    break
            else:
                self.running = False
                print("Player2 won!")
                break
            # Player 2 win condition
            for unit in self.player2.units:
                if unit.is_building:
                    break
            else:
                self.running = False
                print("Player1 won!")
                break

    def begin_phase(self):
        for unit in self.current_player.units:
            unit.actionable = True
        self.current_player.actionable = True

    def execute(self, unit, action):
        """Executes an action by the """
        if unit == None:
            # Player action
            if action == "end":
                self.end_phase()
                self.begin_phase()
            else:
                action(self)
                self.current_player.actionable = False
        else:
            if unit.actionable:
                action(self)
                unit.actionable = False

    def end_phase(self):
        # Toggle the current player
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def position_occupied(self, pos):
        """Helper function that returns a unit if that position is taken"""
        for unit in chain(self.player1.units, self.player2.units):
            if pos[0] == unit.x and pos[1] == unit.y:
                return unit
        return None
