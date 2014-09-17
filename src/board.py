import constants

class Board():

	def __init__(self):
		self.grid = []
		for i in xrange(constants.BOARD_SIZE):
			row = []
			for j in xrange(constants.BOARD_SIZE):
				row.append(0)
			self.grid.append(row)
		self.ships = []
		self.status = constants.ALIVE

	