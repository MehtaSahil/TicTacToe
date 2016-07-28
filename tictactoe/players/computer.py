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
		pass

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

		# max_value assuming computer plays 1 (X), otherwise min_value
		non_immediate_losses = self.get_nonlosing_moves(gamestate)
		if len(non_immediate_losses) == 0:
			print "The computer cannot move without losing"
			raise Exception("the computer has given up")

		max_value = -sys.maxint - 1
		for move in non_immediate_losses:
			if move.value > max_value:
				max_value = move.value

		# max_value_moves = set([x for x in non_immediate_losses if x.value == max_value])

		# find the best of the non-losing moves
		max_value_moves = collections.deque()
		for move in non_immediate_losses:
			# print "%s : %s" % (str(move.board), str(move.value))
			if move.value == max_value:
				max_value_moves.append(move)

		"""
		set for moves in non_immediate_losses that match max_value
		for each move in the max_value set, discard if a two-move setup
		if there are no moves that are not two-move setups, choose
			either move from the max_value set and HOPE
		"""

		"""
		TODO : Step identifying two_step_setups fails
		non_two_step_setup = set()
		temp_max_value_moves = set(copy.deepcopy(max_value_moves))
		for move in temp_max_value_moves:
			if not self.two_step_setup(move):
				non_two_step_setup.add(move)

		print non_two_step_setup
		"""

		# FIXME: Why does this change if the above block is uncommented?
		gamestate = max_value_moves.pop()
		return gamestate

	def get_nonlosing_moves(self, gamestate):
		nonlosing_moves = set()

		for c in gamestate.children:
			potential_loss = self.setup_computer_loss(c)

			# if there is a non-losing move to make
			if not potential_loss:
				nonlosing_moves.add(c)

		return nonlosing_moves

	def two_step_setup(self, compmove):
		"""
		This happens AFTER the immediate loss detection, so skip that
			*Eventual consolidation*
		Will be given a potential computer move to validate
			explore the children (human moves) of that move
				find the move the comp WOULD make in this sit
					if setup_computer_loss == True
						return True

		return False
		"""

		for hc in compmove.children:
			# TODO: This loop is too broad, want only logical move
			# TODO: this is redundant. Pull trap detection out
			non_immediate_losses = self.get_nonlosing_moves(hc)
			if len(non_immediate_losses) == 0:
				return True

			max_value_moves = collections.deque()
			max_value = -sys.maxint - 1
			for move in non_immediate_losses:
				if move.value > max_value:
					max_value_moves.append(move)

			intended_move = max_value_moves.pop()
			if self.setup_computer_loss(intended_move):
				print "future hum move: %s" % str(hc.board)
				print "future comp move: %s" % str(intended_move.board)
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
