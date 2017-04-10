from copy import deepcopy

from ai.influence import *
from ai.evaluator import Evaluator
from model.game.components.health import Health
from model.game.components.collecter import Collecter
from model.game.components.spawner import Spawner
from model.game.game import Game

class Ai(object):

	def __init__(self):
		self.evaluator = Evaluator()
		self.init_score = 0

	def run(self, player, game):
		self.init_score = self.evaluator.eval_board(player, game)

		workers = set()
		soldiers = set()
		spawners = set()

		# divide units into subgroups
		for unit in player.units:
			if unit.has_component(Collecter):
				workers.add(unit)
			if unit.has_component(Attack):
				soldiers.add(unit)
			if unit.has_component(Spawner):
				spawners.add(unit)

		self.run_group(soldiers, game)
		self.run_group(workers, game)
		self.run_build_actions(player, game)
		self.run_group(spawners, game)

	def run_group(self, group, game):
		""" Run optimal action for each unit in given set """
		for unit in group:
			action_list = unit.get_actions(game)
			action_scores = []
			for i in range(0, len(action_list)):
				action_scores.append(self.eval_action(unit.x, unit.y, i, game))
			if action_scores:
				max_score = max(action_scores)
				if max_score >= self.init_score:
					self.init_score = max_score
					optimal_action_index = action_scores.index(max_score)
					optimal_action = action_list[optimal_action_index]
					optimal_action(game)
				else:
					continue

	def run_build_actions(self, player, game):
		""" Create optimal building """
		build_actions = player.get_actions(game)
		build_scores = []
		for i in range(0, len(build_actions)):
			build_scores.append(self.eval_build(i, game))
		if build_scores:
			max_score = max(build_scores)
			if max_score >= self.init_score:
				self.init_score = max_score
				optimal_build_index = build_scores.index(max_score)
				optimal_build = build_actions[optimal_build_index]
				optimal_build(game)

	def eval_action(self, x, y, act_index, game):
		""" Evaluates board state of a potential action """
		player = game.current_player
		for unit in player.units:    # find the unit in game copy
			if unit.x == x and unit.y == y:
				active_unit = unit
				break
		actions = active_unit.get_actions(game)
		reverse_action = actions[act_index](game)
		result = self.evaluator.eval_board(player, game)
		reverse_action(game)
		return result

	def eval_build(self, index, game):
		"""Evaluate board state of a potential building creation"""
		player = game.current_player
		build = player.get_actions(game)[index]
		reverse_build = build(game)
		result = self.evaluator.eval_board(player, game)
		reverse_build(game)
		return result
