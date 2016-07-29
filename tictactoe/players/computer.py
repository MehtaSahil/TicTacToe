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
		if self.can_immediately_win(gamestate):
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

		# No possibility for two_step_setup (not enough turns)
		# Simply choose the best path forward
		if final_two_moves:
			max_value = self.max_value(non_immediate_losses)
			return self.max_move(non_immediate_losses, max_value)

		for m in non_immediate_losses:
			print "nim : %s" % str(m.board)

		# Choose the best path that is not a setup
		"""
		TODO : two_step_setup needs to check for immediate wins!
			right now it returns True if there is ANY possibility
			of a trap, but does not know that in the process of
			setting up a trap the human may have set up a win for
			the comp (separate is_immediate_win method)
			Make this decision less extreme in avoiding loss
		"""
		valid_moves = [x for x in non_immediate_losses
			       if not self.two_step_setup(x)]

		for m in valid_moves:
			print "vm : %s" % str(m.board)

		max_value = self.max_value(valid_moves)
		return self.max_move(valid_moves, max_value)

	def can_immediately_win(self, gamestate):
		for c in gamestate.children:
			if c.is_win_for(self.computer_player):
				return True

		return False

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
		win_trap_balance = 0

		# value loss avoidance over following a win
		win_bias = 1
		loss_bias = 5

		for hc in compmove.children:
			if self.can_immediately_win(hc):
				win_trap_balance += win_bias
				continue

			# if there are no moves the computer can make
			non_immediate_losses = self.get_nonlosing_moves(hc)
			if len(non_immediate_losses) == 0:
				win_trap_balance -= loss_bias

		if win_trap_balance < 0:
			return True

		return False

	def setup_computer_loss(self, compmove):
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
