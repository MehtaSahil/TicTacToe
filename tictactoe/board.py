def Main():
	tempboard = [1, 0, -1, -1, 1, 1, 0, 1, 0]
	gamestate = Board(tempboard)

	print str(gamestate.board) + " : " + str(gamestate.value)

class Board():
	"""
	board representation (string)
		-1's are blank
		1's are X
		0's are O
	value (win = 1, loss = -1; else = 0)
	Set of children
	"""

	def __init__(self, board):
		self.set_board(board)
		self.value = self.calc_value()
		self.children = None

	def set_board(self, board):
		if len(board) != 9:
			raise ValueError("invalid board: " + str(len(board)))
		self.board = board

	def add_child(self, child):
		if self.children == None:
			raise Exception("must initialize children before adding")
		self.children.append(child)

	def is_vertical_win(self, player):
		temp = self.board

		col1 = (temp[0] == player
			and temp[3] == player
			and temp[6] == player)

		col2 = (temp[1] == player
			and temp[4] == player
			and temp[7] == player)

		col3 = (temp[2] == player
			and temp[5] == player
			and temp[8] == player)

		return bool(col1 or col2 or col3)

	def is_horizontal_win(self, player):
		temp = self.board

		row1 = (temp[0] == player
			and temp[1] == player
			and temp[2] == player)

		row2 = (temp[3] == player
			and temp[4] == player
			and temp[5] == player)

		row3 = (temp[6] == player
			and temp[7] == player
			and temp[8] == player)

		return bool(row1 or row2 or row3)

	def is_diagonal_win(self, player):
		temp = self.board

		diag1 = (temp[0] == player
			and temp[4] == player
			and temp[8] == player)

		diag2 = (temp[6] == player
			and temp[4] == player
			and temp[2] == player)

		return bool(diag1 or diag2)

	def is_win_for(self, player):
		vert	= self.is_vertical_win(player)
		horiz	= self.is_horizontal_win(player)
		diag	= self.is_diagonal_win(player)

		return bool(vert or horiz or diag)

	# assumes computer is X (1)
	def calc_value(self):
		if self.is_win_for(1):
			return 1
		elif self.is_win_for(0):
			return -1
		else:
			return 0

	def is_end_game(self):
		# if at endgame
		if (self.is_win_for(1) or self.is_win_for(0)):
			return True

		# if tie game AND no more moves
		if (self.calc_value() == 0
		    and not(-1 in self.board)):
			return True

		return False

if __name__ == "__main__":
	Main()
