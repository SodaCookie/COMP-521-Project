from mode.game.faction import Faction
from assets.units.tavern_blueprint import TavernBlueprint
from assets.units.hideout_blueprint import HideoutBlueprint


class RebelsFaction(Faction):
	"""Define the Rebels faction"""

    def __init__(self):
        super().__init__(HideoutBlueprint, TavernBlueprint);
