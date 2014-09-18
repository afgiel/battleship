import constants
import ship
import copy

class Board():

	def __init__(self, player_name):
		self.player_name = player_name
		self.grid = []
		for i in xrange(constants.BOARD_SIZE):
			row = []
			for j in xrange(constants.BOARD_SIZE):
				row.append(0)
			self.grid.append(row)
		self.ships = []
		self.status = constants.ALIVE

	def to_std_out(self):
		print '%s, your board currently looks like this:' % (self.player_name)
		for row in self.grid:
			str_row = ['\t']
			for elem in row:
				str_row.append(str(elem))
			print ' '.join(str_row)

	def fill_board(self):
		for ship_type in ship.SHIP_TYPES:
			ship_placed = False
			while not ship_placed:
				start_index = self.get_start_index(ship_type)
				end_index = self.get_end_index(ship_type, start_index)
				if not self.correct_dist(start_index, end_index, ship_type):
					print '%s, your start and end indices must share one common component and be properly distanced!' % (self.player_name)
					print '%s, the euclidean distance of your two indices must be %d!' % (self.player_name, constants.SHIP_LENS[ship_type] - 1)
					constants.try_again()
					continue
				if not self.space_available(start_index, end_index):
					print '%s, your %s was overlapping with another ship previously placed!' % (self.player_name, ship_type)
					self.to_std_out()
					constants.try_again()
					continue
				self.place_ship(start_index, end_index)
				print '%s, your %s was successfully placed on the board' % (self.player_name, ship_type)
				self.to_std_out()
				ship_placed = True
		print '%s, all your ships have been placed! Use cmd + k to clear the terminal so your opponent can\'t see'

	def place_ship(self, start_index, end_index):
		xs = [start_index[0] - 1, end_index[0] - 1]
		ys = [start_index[1] - 1, end_index[1] - 1]
		if abs(ys[0] - ys[1]) == 0:
			row = ys[0]
			for i in range(xs[0], xs[1] + 1):
				self.grid[row][i] += 1
		else:
			col = xs[0]
			for i in range(ys[0], ys[1] + 1):
				self.grid[i][col] += 1

	def space_available(self, start_index, end_index):
		new_grid = copy.deepcopy(self.grid)
		xs = [start_index[0] - 1, end_index[0] - 1]
		ys = [start_index[1] - 1, end_index[1] - 1]
		if abs(ys[0] - ys[1]) == 0:
			row = ys[0]
			for i in range(xs[0], xs[1] + 1):
				new_grid[row][i] += 1
		else:
			col = xs[0]
			for i in range(ys[0], ys[1] + 1):
				new_grid[i][col] += 1
		for row in new_grid:
			for elem in row:
				if elem != 0 and elem != 1:
					return False
		return True

	def correct_dist(self, start_index, end_index, ship_type):
		ship_len = constants.SHIP_LENS[ship_type] - 1
		xs = [start_index[0], end_index[0]]
		ys = [start_index[1], end_index[1]]
		if abs(xs[0] - xs[1]) == ship_len and abs(ys[0] - ys[1]) == 0:
			return True
		elif abs(ys[0] - ys[1]) == ship_len and abs(xs[0] - xs[1]) == 0:
			return True
		else:
			return False

	def in_bounds(self, index, check_name):
		ind = list(index)
		for elem in ind:
			if not elem > 0: 
				print '%s, all elements of the %s must be greater than 0' % (self.player_name, check_name)
				constants.try_again()
				return False
			elif not elem <= constants.BOARD_SIZE:
				print '%s, all elements of the %s must be less than or equal to %d' % (self.player_name, check_name, constants.BOARD_SIZE)
				constants.try_again()
				return False
		return True

	def get_start_index(self, ship_type):
		have_start = False
		start_index = (-1, -1)
		while not have_start:
				print '%s, pick the start index of your %s' % (self.player_name, ship_type)
				print 'This ship is %d units long' % (constants.SHIP_LENS[ship_type])
				start_x = raw_input('Start X Index: ')
				start_y = raw_input('Start Y Index: ')
				try: 
					start_x = int(start_x)
					start_y = int(start_y)
				except Exception:
					print 'FUCKING MAYHEM'
				start_index = (start_x, start_y)
				if self.in_bounds(start_index, 'start index'):
					print 'start index successfully saved'
					have_start = True
		return start_index

	def get_end_index(self, ship_type, start_index):
		have_end = False
		end_index = -1
		while not have_end:
			print '%s, pick the end index of your %s' % (self.player_name, ship_type)
			print 'This ship is %d units long and your start index was at %d, %d' % (constants.SHIP_LENS[ship_type], start_index[0], start_index[1])
			end_x = raw_input('End X Index: ')
			end_y = raw_input('End Y Index: ')
			try: 
				end_x = int(end_x)
				end_y = int(end_y)
			except Exception:
				print 'FUCKING MAYHEM'
			end_index = (end_x, end_y)
			if self.in_bounds(end_index, 'end index'):
				print 'end index successfully saved'
				have_end = True
		return end_index

