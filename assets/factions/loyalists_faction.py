from model.game.faction import Faction
from assets.units import KeepBlueprint
from assets.units import BarracksBlueprint


class LoyalistFaction(Faction):
	"""Define the Loyalist faction"""

	def __init__(self):
	    super().__init__([KeepBlueprint, BarracksBlueprint])
	    
	def instantiate(self, game, player, position):
		start_building = self.building_blueprints[0].instantiate(position)
		start_building.set_player(player)