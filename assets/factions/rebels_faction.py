from model.game.faction import Faction
from assets.units.tavern_blueprint import TavernBlueprint
from assets.units.hideout_blueprint import HideoutBlueprint


class RebelsFaction(Faction):
	"""Define the Rebels faction"""

	def __init__(self):
	    super().__init__([HideoutBlueprint(), TavernBlueprint()])

	def initialize(self, game, player, position):
		start_building = self.building_blueprints[0].instantiate(position)
		start_building.set_player(player)
