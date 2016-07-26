from mc_tree import Tree
from game_generator import GameGenerator
from board import Board
import sys
import copy

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
		self.computer_player =  1
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

		self.loop(self.game_tree.root, computer_plays_first)

	def loop(self, gamestate, computer_plays_first):
		print "start board: " + str(gamestate.board)

		# True if it's the computer's turn, else False
		comp_turn = computer_plays_first
		while True:
			if comp_turn:
				gamestate = self.computer_move(gamestate)
				print "computer move: " + str(gamestate.board)
			else:
				gamestate = self.human_move(gamestate)
				print "human move: " + str(gamestate.board)
				print

			comp_turn = not comp_turn

			# if at endgame
			if (gamestate.calc_value() == 1
			    or gamestate.calc_value() == -1):
				break

			# if tie game AND no more moves
			if (gamestate.calc_value() == 0
			    and not(-1 in gamestate.board)):
				break

		print "game over"
		gamestate.value = gamestate.calc_value()
		if gamestate.value == 1:
			print "X's Win"
		elif gamestate.value == 0:
			print "draw"
		elif gamestate.value == -1:
			print "O's Win"

		print "final gamestate: " + str(gamestate.board)

	def computer_move(self, gamestate):
		# If an immediate win is possible, make that move
		for c in gamestate.children:
			if c.calc_value() == 1:
				gamestate = c
				return gamestate

		# if not defending, choose path of most likely victory
		# max_value assuming computer plays 1 (X), otherwise min_value
		max_value = -sys.maxint - 1
		for c in gamestate.children:
			potential_loss = self.setup_computer_loss(c)

			# only consider moves that don't lose the game
			if not potential_loss:
				if c.value > max_value:
					max_value = c.value
			elif potential_loss:
				print str(c.board) + " : impending loss"

		# find the best of the non-losing moves
		for c in gamestate.children:
			potential_loss = self.setup_computer_loss(c)
			if c.value == max_value and (not potential_loss):
				gamestate = c
				return gamestate

		print "the computer cannot move without losing"
		return gamestate

	def setup_computer_loss(self, gamestate):
		gen = GameGenerator()

		if gamestate.children == None:
			return False

		for c in gamestate.children:
			next_boards = gen.simple_perms(gamestate.board,
						       self.human_player)
			if len(next_boards) == 0:
				continue

			for b in next_boards:
				temp_board = Board(b)
				if temp_board.calc_value() == -1:
					return True

		return False

	def human_move(self, gamestate):
		local_gamestate_board = copy.deepcopy(gamestate.board)

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

	def board_to_list_index(self, b_i):
		dim = 3
		if len(b_i) != 2:
			print "cannot convert coords: " + str(b_i)
			return

		return int(b_i[0])*dim + int(b_i[1])

def Main():
	game = Play()

if __name__ == "__main__":
	Main()
