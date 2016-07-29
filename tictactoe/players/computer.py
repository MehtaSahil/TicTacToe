import os
import sys
import collections
import copy

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

	def computer_move(self, gamestate):
		"""
		Decision Order:
			1) Immediate Win
			2) Immediate Loss
			3) 2-Move Loss
		"""

		# If an immediate win is possible, make that move
		for c in gamestate.children:
			if c.is_win_for(self.computer_player):
				gamestate = c
				return gamestate

		# If the comp is trapped, the game is over
		non_immediate_losses = self.get_nonlosing_moves(gamestate)
		if len(non_immediate_losses) == 0:
			print "The computer cannot move without losing"
			raise Exception("the computer has given up")

		# Prevents looking beyond the 9th turn for two_step_setup
		final_two_moves = False
		for move in non_immediate_losses:
			if len(move.children) == 1:
				final_two_moves = True
				break

		# No possibility for two_step_setup anymore (not enough turns)
		# Simply choose the best path forward
		if final_two_moves:
			max_value = self.max_value(non_immediate_losses)
			return self.max_move(non_immediate_losses, max_value)

		# Choose the best path that is not a setup
		valid_moves = [x for x in non_immediate_losses
			       if not self.two_step_setup(x)]

		max_value = self.max_value(valid_moves)
		return self.max_value_move(valid_moves, max_value)

	def max_move(self, tosearch, max_value):
		for m in tosearch:
			if m.value == max_value:
				return m

		raise Exception("no max value match found")

	def max_value(self, tosearch):
		return max(x.value for x in tosearch)

	def get_nonlosing_moves(self, gamestate):
		nonlosing_moves = set()
		for c in gamestate.children:
			potential_loss = self.setup_computer_loss(c)

			# if there is a non-losing move to make
			if not potential_loss:
				nonlosing_moves.add(c)

		return nonlosing_moves

	def two_step_setup(self, compmove):
		for hc in compmove.children:
			# if there are no moves the computer can make
			non_immediate_losses = self.get_nonlosing_moves(hc)
			if len(non_immediate_losses) == 0:
				return True

		return False

	def setup_computer_loss(self, compmove):
		gen = GameGenerator()

		if compmove.children == None:
			return False

		# explore potential moves from the human player
		for c in compmove.children:
			if c.children == None:
				continue

			for nc in c.children:
				if nc.is_win_for(self.human_player):
					return True

		return False
