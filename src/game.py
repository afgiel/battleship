import constants
import board

class Game():

	def __init__(self, player_1, player_2):
		self.player_1 = player_1
		self.player_2 = player_2

		self.board_1 = board.Board(player_1)
		self.board_2 = board.Board(player_2)


	def play(self):
		self.set_up_boards()
			

	def set_up_boards(self):
		self.board_1.fill_board()
		self.board_2.fill_board()