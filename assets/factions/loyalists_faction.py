from model.game.faction import Faction
from assets.units import KeepBlueprint
from assets.units import BarracksBlueprint


class LoyalistFaction(Faction):
	"""Define the Loyalist faction"""

	def __init__(self):
	    super().__init__([KeepBlueprint, BarracksBlueprint])
