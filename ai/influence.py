""" Defines operation functions to describe a player's influence on the board.

Influence is represented as a grid of int: 
	- Influence value on a tile increases by 1 for each unit with an Attack component in attach range of the cell
"""

from model.game.components.attack import Attack

def get_influence_map(player, board):
	influence_map = [[0 for j in range(board.height)] for i in range(board.width)]

	for unit in player.units:
		if unit.has_component(Attack):
			attack_component = unit.get_component(Attack)
			attack_positions = attack_component._get_attack_ring(unit.x, unit.y, attack_component.attack_range)
			
			for ax, ay in attack_positions:
				influence_map[ax][ay] += 1

	return influence_map