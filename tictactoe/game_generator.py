import copy

class GameGenerator():
	def __init__(self):
		pass

	# Generates all possible moves for <player> given the <board>
	def simple_perms(self, board, player):
		# list of lists
		boards = list()
		limit = len(board)
		for i in range(0, limit):
			if board[i] == 1 or board[i] == 0:
				continue

			board[i] = player
			boards.append(copy.deepcopy(board))
			board[i] = -1

		return boards
