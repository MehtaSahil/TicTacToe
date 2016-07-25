from mc_tree import Tree
import sys

"""
converting from [row, col] coordinates to explicit spot in list
	spot = row*dim + col

	e.g. accessing the [1,0] spot on a 3x3 board:
		spot = 1*3 + 0 = 3
		list[spot] == the [1,0] spot on a physical board
"""

blank_board = [-1, -1, -1, -1, -1, -1, -1, -1, -1]

class Play:
	def __init__(self):
		print "What position is the computer? (1 for X, 0 for 0)"
		self.computer_player = int(raw_input())
		self.human_player = 1 - self.computer_player

		print "Who is playing first? (1 for X, 0 for O)"
		self.first_player = int(raw_input())

		if self.computer_player == self.first_player:
			computer_plays_first = True
		else:
			computer_plays_first = False

		# set up game
		self.game_tree = Tree(blank_board, self.first_player)
		self.game_tree.prop_vals(self.game_tree.root)

		if computer_plays_first:
			# play a computer move
			pass
		else:
			# begin game loop (while gamestate.value == 0)
			pass

	def loop(self, gamestate, computer_plays_first):
		# True if it's the computer's turn, else False
		comp_turn = computer_plays_first
		while gamestate.value == 0:
			if comp_turn:
				gamestate = self.computer_move(gamestate)
			else:
				gamestate = self.human_move(gamestate)

			comp_turn = !comp_turn

	def computer_move(self, gamestate):
		max_value = -sys.maxint - 1
		for c in gamestate.children:
			if c.value > max_int:
				max_int = c.value

		for c in gamestate.children:
			if c.value == max_int:
				gamestate = c

		print gamestate
		return gamestate

	def human_move(self, gamestate):
		while (True):
			print "where did the human play?"
			user_in = raw_input()
			coords = user_in.split(",")
			if len(coords) != 2:
				print "invalid coords. try again"
			else:
				break

		list_index = self.board_to_list_index(coords)
		gamestate[list_index] = self.human_player

		print gamestate
		return gamestate

	def board_to_list_index(self, b_i):
		dim = 3
		if len(b_i) != 2:
			print "cannot convert coords: " + str(b_i)
			return

		return int(b_i[0])*dim + int(b_i[1])

game = Play()
game.human_move(blank_board)
