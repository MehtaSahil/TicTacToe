import collections

def Main():
	tempboard = [0, 1, 1, 0, -1, 1, 0, 1, 0]
	gamestate = Board(tempboard)

	gamestate.print_board()
	print gamestate.value

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
		self.children = collections.deque()

	def set_board(self, board):
		if len(board) != 9:
			raise ValueError("invalid board: " + str(len(board)))
		self.board = board

	def add_child(self, child):
		self.children.add(child)

	def print_board(self):
		temp = self.board
		print str(temp[0]) + " " + str(temp[1]) + " " + str(temp[2])
		print str(temp[3]) + " " + str(temp[4]) + " " + str(temp[5])
		print str(temp[6]) + " " + str(temp[7]) + " " + str(temp[8])

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

if __name__ == "__main__":
	Main()
