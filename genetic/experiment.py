"""Defines the Experiment class and default functions"""

import math
import random
import traceback
import multiprocessing
from copy import deepcopy
import numpy as np

from genetic.generation_operations import *
from model.board.board import Board
from model.game.game import Game
from assets.factions.loyalists_faction import LoyalistFaction
from assets.factions.rebels_faction import RebelsFaction
from ai.ai import Ai

def default_fitness_function(games):
    """Returns a normalized number between 0 and 1, draws are a fail"""
    winners = [abs(game.winner) for game in games]
    above = 0
    below = 0
    for game in games:
        if game.winner > 0:
            above += 1
        else:
            below += 1
    return sum(winners) / len(winners) * min(above, below) / max(above, below)

def create_fitness_stopmethod(fitness):
    """Returns a function that stops when fitness level is reached"""
    def callback(experiment):
        return experiment.current_max_fitness > fitness
    return callback

def create_generation_stopmethod(generation_num):
    """Returns a function that stops when generation number is reached"""
    def callback(experiment):
        return experiment.current_generation == generation_num
    return callback


class Experiment(object):

    DEFAULT = {
        "size"          : 10,                       # Size of each generation
        "gameruns"      : 10,                       # Number of evals per board
        "fitness"       : default_fitness_function, # Fitness function
        "elite"         : 2,                        # Number of elite children
        "mutation"      : 0.1,                      # Mutation rate
        "stopmethod"    : create_fitness_stopmethod(0.8), # Method for stopping
        "ai"            : Ai,                       # AI agent to play
        "mutationnum"   : 3                         # Times to mutate on mutate
    }

    def __init__(self, **kwargs):
        self.options = dict(Experiment.DEFAULT)
        self.options.update(kwargs)
        self.current_population = []
        self.current_max_fitness = 0
        self.current_generation = 0

    def run(self):
        seed = random.randint(0, 4294967295)
        random.seed(seed)
        print("Running experiment with seed: %d" % seed)
        print("Game runs per board: %d" % self.options["gameruns"])
        print("Mutation rate: %0.2f" % self.options["mutation"])
        print("Elite children: %d" % self.options["elite"])
        print("Generating population of size: %d" % self.options["size"])
        print("-"*79 + "\n") # divisor line
        # Initialize first generation
        fitnesses = []
        self.current_population = [Board(10, 10) for i in range(self.options["size"])]
        # Run until fitness stop method is done
        while not self.options["stopmethod"](self):
            if self.current_generation != 0:
                # If not the first population we make the next generation
                self.current_population = self.generate_next_population(fitnesses)
            # Run the games and get the winners
            print("Evaluating population: %d" % self.current_generation)
            result = self.evaluate_population(self.current_population)
            fitnesses = self.evaluate_fitness(result)
            self.current_generation += 1
            print("\n" + "-" * 79 + "\n") # divisor line
        # Return the final generation
        return self.current_population

    def evaluate_population(self, population):
        # For every board generate a game gamerun times
        result = []
        for i, board in enumerate(population):
            run = []
            print("\nEvaluating board: %d" % i)
            for j in range(self.options["gameruns"]):
                # Run every game to completion
                print("\nRunning game %d - " % j, end="")
                new_game = Game(board=deepcopy(board))
                new_game.player1.set_faction(LoyalistFaction())
                new_game.player2.set_faction(RebelsFaction())
                new_game.set_player1_controller(self.options["ai"]())
                new_game.set_player2_controller(self.options["ai"]())
                new_game.initialize()
                new_game.run()
                run.append(new_game)
            result.append((board, run))
        return result

    def generate_next_population(self, fitnesses):
        """Returns a new list of boards based on the fitness"""
        new_population = []
        # Sort the boards by fitness
        sorted_fitnesses = sorted(fitnesses, key=lambda fitness_result : fitness_result[1])
        boards, fitnesses = zip(*sorted_fitnesses)
        new_population.extend(boards[-self.options["elite"]:])

        # Add Mutations
        print("Applying mutations...")
        for board in random.sample(boards, int(math.ceil((self.options["size"] \
                - self.options["elite"]) \
                * self.options["mutation"]))):
            # mutation the board
            new_board = board
            for i in range(self.options["mutationnum"]):
                try:
                    new_board = mutate_board(new_board)
                except:
                    print("Error occured in mutation.")
                    traceback.print_exc()
            new_population.append(new_board)

        # Add merged from parents
        parents = []
        # Add enough to fill out the rest with merges
        # Establish weights
        # Edge case all fitness are 0
        if all(f == 0.0 for f in fitnesses):
            fitnesses = [1 for i in range(len(fitnesses))]
        weights = np.array(fitnesses) / sum(fitnesses)
        for i in range(self.options["size"] - len(new_population)):
            try:
                parents = np.random.choice(boards, 2, False, weights)
                new_board = merge_boards(*parents)
                new_population.append(new_board)
            except:
                print("Error occured in merging.")
                traceback.print_exc()

        return new_population

    def evaluate_fitness(self, gen_result):
        """Evaluates the fitness of every board and returns.

        Also maintains the highest fitness of the generation in the
        current_max_fitness member. Takes the resultant values of the
        evaluated population."""
        self.current_max_fitness = 0
        fitnesses = []
        for board, games in gen_result:
            fitness = self.options["fitness"](games)
            if fitness > self.current_max_fitness:
                self.current_max_fitness = fitness
            fitnesses.append((board, fitness))
        return fitnesses
