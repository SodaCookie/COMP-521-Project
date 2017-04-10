from ai.influence import *
from model.board.modifiers.resource import *
from model.game.components.health import Health
from model.game.components.collecter import Collecter
from model.game.components.spawner import Spawner
from model.utility.distance import *

class Evaluator(object):

	def __init__(self):
		self.score = 0
		self.workers = set()
		self.soldiers = set()
		self.resources = set()
		self.spawners = set()

	def eval_board(self, player, game):
		""" Evaluate the board from a player's perspective and return the score """
		enemy = game.player2 if (player == game.player1) else game.player1

		for unit in player.units:
			if unit.has_component(Collecter):
				workers.add(unit)
			if unit.has_component(Attack):
				soldiers.add(unit)
			if unit.has_component(Spawner):
				spawners.add(unit)

		for tile in game.board:
			if tile.has_modifier(Resource):
				resources.add(tile)

		influence_map = get_influence_map(player, game.board)
		threat_map = get_influence_map(enemy, game.board)

		eval_units(player, influence_map, threat_map)
		eval_enemy_units(enemy)
		eval_soldiers(enemy, game)
		eval_spawner_pos(player, enemy, game)
		eval_workers(threat_map, game, ResourceCategory.MINERAL)

		return self.score


	# Prefer more expensive units. Avoid building too many workers
	def eval_units(self, player, influence_map, threat_map):
		need_workers = need_build_workers(influence_map, threat_map)
		for unit in player.units:
			if unit.has_component(Health):
				if unit.has_component(Collecter) and not need_workers:
					continue
				else:
					self.score += unit.cost

	# Attacking will prioritize units that are easier to kill
	def eval_enemy_units(self, enemy):
		for unit in enemy.units:
			if unit.has_component(Health):
				self.score += 100 * unit.get_component(Health).current_hp_percent()

	# Attack units out of attack range will prefer positions that bring them closer to the enemy
	def eval_soldiers(self, enemy, game):
		enemy_distances = set()
		for soldier in self.soldiers:
			if not solder.get_component(Attack)._get_attacks(game):
				for enemy_unit in enemy.units:
					enemy_distances.add(dist_squared(soldier.x, soldier.y, enemy_unit.x, enemy_unit.y))
				self.score -= min(enemy_distances)

	# Prefer to place spawners close to other buidings
	# As a measure to avoid wall-offs, tiles around spawner must not be occupied by buildings
	def eval_spawner_pos(self, player, enemy, game):
		temp_score = 0
		for spawner in self.spawners:
			# check if tiles surrounding the spawner have buildings
			for i in range(-1, 1):
				for j in range(-1, 1):
					if i == 0 and j == 0:
						continue
					adj_x = spawner.x + i
					adj_y = spawner.y + j

					if (0 <= adj_x < game.board.width) and (0 <= adj_y < game.board.height):
						for unit in chain(player.units, enemy.units):
							if unit.x == adj_x and unit.y == adj_y and unit.is_building:
								temp_score += 1
		if (temp_score):
			self.score -= temp_score
		else:
			sum_dist_squared = 0
			for spawner in self.spawners:
				sum_dist_squared += dist_squared(spawner.x, spawner.y, player.init_pos[0], player.init_pos[1])
			self.score -= sum_dist_squared


	def eval_workers(self, threat_map, game, resource_category):
		for worker in self.workers:
			threat_level = threat_map[worker.x][worker.y]
			if threat_level:
				self.score -= threat_level
			else:
				collection_range = worker.get_component(Collecter).collection_range
				resource_range = worker.get_component(Collecter)._get_resource_range(worker.x, worker.y, collection_range)
				temp_score = 0;

				for pos in resource_range:
					resource = game.board[pos].get_modifier(Resource)
					if resource and resource.category == category:
						temp_score += 1

				if temp_score != 0:    # nothing to collect
					self.score += temp_score
				elif self.resources:    # look to get closer to resources to collect
					goal = None
					for tile in self.resources:
						if threat_map[tile.x][tile.y] == 0:
							if (goal == None):
								goal = tile
							elif (tile.get_modifier(Resource).amount > goal.get_modifier(Resource).amount):
								goal = tile
					self.score -= dist_squared(worker.x, worker.y, goal.x, goal.y)

	def need_build_workers(self, influence_map, threat_map):
		""" helper function to determine if we need more workers """
		if len(self.workers) == 0:
			return True

		for worker in self.workers:
			range = worker.get_component(Collecter).collection_range
			break

		num_controlled_tiles = 0
		for tile in self.resources:
			if influence_map[tile.x][tile.y] - threat_map[tile.x][tile.y] > 0:
				num_controlled_tiles += 1
		return len(self.workers) < num_controlled_tiles * range + 1













