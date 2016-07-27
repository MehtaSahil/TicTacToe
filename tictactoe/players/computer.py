import os
import sys

file_path = os.path.abspath(__file__)
parent_path = os.path.dirname(os.path.dirname(file_path))
sys.path.append(parent_path)

from game_generator import GameGenerator
from board import Board

# =============================================================================

class ComputerPlayer:
	def __init__(self, computer_player):
		self.computer_player = computer_player
		self.human_player = 1 - computer_player
		pass

	def computer_move(self, gamestate):
		# If an immediate win is possible, make that move
		for c in gamestate.children:
			if c.is_win_for(self.computer_player):
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

		print "The computer cannot move without losing"
		raise Exception("the computer has given up")

	def setup_computer_loss(self, gamestate):
		gen = GameGenerator()

		if gamestate.children == None:
			return False

		# explore potential moves from the human player
		for c in gamestate.children:
			if c.children == None:
				continue

			for nc in c.children:
				if nc.is_win_for(self.human_player):
					return True

		return False
