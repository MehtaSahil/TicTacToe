import copy

class HumanPlayer:
	def __init__(self, human_player):
		self.human_player = human_player
		self.computer_player = 1 - human_player

	def human_move(self, gamestate):
		local_gamestate_board = copy.deepcopy(gamestate.board)

		# ask for moves until a valid move is given
		while (True):
			print "where did the human play?"
			user_in = raw_input()
			coords = user_in.split(",")
			if len(coords) != 2:
				print "invalid coords. try again"
			else:
				break

		list_index = self.board_to_list_index(coords)
		local_gamestate_board[list_index] = self.human_player

		for c in gamestate.children:
			if local_gamestate_board == c.board:
				gamestate = c
				return gamestate

		print "human move failed"
		return gamestate

	def board_to_list_index(self, b_i):
		dim = 3
		if len(b_i) != 2:
			print "cannot convert coords: " + str(b_i)
			return

		return int(b_i[0])*dim + int(b_i[1])
