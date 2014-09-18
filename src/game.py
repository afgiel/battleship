import constants
import board
import sys

class Game():

	def __init__(self, player_1, player_2):
		if player_1 == player_2:
			print 'player names must differ!'
			sys.exit()
		self.player_1 = player_1
		self.player_2 = player_2

		self.board_1 = board.Board(player_1)
		self.board_2 = board.Board(player_2)

		self.player_1_shots = set()
		self.player_2_shots = set()


	def play(self):
		self.set_up_boards()
		winner = None
		count = 1
		while winner is None:
			print '\nROUND %d\n' % (count)
	 		self.take_shot(self.player_1, self.board_2, self.player_1_shots)
	 		if not self.board_2.is_alive():
	 			winner = self.player_1
	 			continue
	 		print '\nSWITCH!\n'
	 		self.take_shot(self.player_2, self.board_1, self.player_2_shots)
	 		if not self.board_1.is_alive():
	 			winner = self.player_2
	 			continue
	 		count += 1
	 	loser = self.player_2 if winner == self.player_1 else self.player_1
	 	print 'CONGRATS %s, you have beaten your opponent, %s' % (winner, loser)

	def take_shot(self, player_name, opp_board, player_shots):
		have_shot = False
		shot_index = (-1, -1)
		while not have_shot:
			print '%s, take a shot at your opponent\'s board!' % (player_name)
			shot_x = raw_input('Shot X Index: ')
			shot_y = raw_input('Shot Y Index: ')
			try: 
				shot_x = int(shot_x)
				shot_y = int(shot_y)
			except Exception:
				print 'FUCKING MAYHEM'
				continue
			shot_index = (shot_x, shot_y)
			if not opp_board.in_bounds(shot_index, 'shot index'):
				continue
			if shot_index in player_shots:
				print 'You have already shot at %d, %d! You wouldn\'t want to do that again!' % (shot_index[0], shot_index[1])
				continue
			print 'shot planned for %d, %d !' % (shot_index[0], shot_index[1])
			have_shot = True
			player_shots.add(shot_index)
		if opp_board.take_shot(shot_index):
			print 'SUCCESS! Shot hit at %d, %d!' % (shot_index[0], shot_index[1])
		else:
			print 'Looks like that missed, better luck next time!'
		opp_board.print_opp_view(player_shots)

	def set_up_boards(self):
		self.board_1.fill_board()
		self.board_2.fill_board()