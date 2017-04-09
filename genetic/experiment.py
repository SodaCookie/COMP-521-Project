"""Defines the Experiment class and default functions"""

import math
import random
import multiprocessing
from copy import deepcopy
import numpy as np

from genetic.generation_operations import *
from model.board.board import Board
from model.game.game import Game
from assets.factions.loyalists_faction import LoyalistFaction
from assets.factions.rebels_faction import RebelsFaction

def default_fitness_function(games):
    """Returns a normalized number between 0 and 1, draws are a fail"""
    winners = [game.winner for game in games]
    p1_wins = winners.count(1)
    p2_wins = winners.count(2)
    draws = winners.count(None)
    return min(p1_wins, p2_wins) / len(winners) / 0.5

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
        "stopmethod"    : create_fitness_stopmethod(0.8) # Method for stopping
    }

    def __init__(self, **kwargs):
        self.options = dict(Experiment.DEFAULT)
        self.options.update(kwargs)
        self.current_population = []
        self.
        self.current_max_fitness = 0
        self.current_generation = 0

    def run(self):
        seed = random.randint(0, 4294967295)
        random.seed(seed)
        print("Running experiment with seed: %d" % seed)
        print("Game runs per board: %d" % self.options["gameruns"])
        print("Mutation rate: %d" % self.options["mutation"])
        print("Elite children: %d" % self.options["elite"])
        print("Generating population of size: %d" % self.options["size"])
        print("-"*79 + "\n") # divisor line
        # Initialize first generation
        self.current_population = [Board() for i in range(self.options["size"])]
        # Run until fitness stop method is done
        while not self.options["fitness"](self):
            if self.current_generation != 0:
                # If not the first population we make the next generation
                self.current_population = self.generate_next_population(self.current_population)
            # Run the games and get the winners
            print("Evaluating population: %d" % self.current_generation)
            result = self.evaluate_population(self.current_population)
            self.evaluate_fitness(result)
            self.current_generation += 1
            print("-"*79 + "\n") # divisor line
        # Return the final generation
        return self.current_population

    def evaluate_population(self, population):
        # For every board generate a game gamerun times
        result = []
        for board in population:
            run = []
            for i in range(self.options["gameruns"])
                # Run every game to completion
                new_game = Game(deepcopy(board))
                g.player1.set_faction(LoyalistFaction())
                g.player2.set_faction(RebelsFaction())
                game.initialize()
                game.run()
                run.append(game)
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
        for board in random.sample(boards, int(math.ceil((self.options["size"] \
                - self.options["elite"]) \
                * self.options["mutation"]))):
            # mutation the board
            new_board = mutate_board(board)
            new_population.append(new_board)

        # Add merged from parents
        parents = []
        # Add enough to fill out the rest with merges
        # Establish weights
        weights = np.array(fitnesses) / sum(fitnesses)
        for i in range(self.options["size"] - len(new_population)):
            parents = np.random.choice(boards, 2, False, weights)
            new_board = merge_boards(*parents)
            new_population.append(new_board)

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
