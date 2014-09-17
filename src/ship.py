

class Ship(object):

	@staticmethod
	def get_ship_for_type(ship_type):
		return SHIP_TYPES[ship_type]


class Battleship(Ship):


class Destroyer(Ship):




SHIP_TYPES = {
	'battleship': Battleship()
	'destroyer': Destroyer()
}