from board import Board
import collections
import copy

class GameGenerator():

	"""
	For tree generation, define a perms method that returns
		a list of lists of different IN ORDER permuations
		e.g. perms([-1, -1, -1], 1) returns:
			[1, -1, -1]
			[-1, 1, -1]
			[-1, -1, 1]
		keep track of whose turn it is in the main loop
			the player will switch when the list of lists
			has no more states left to process
	"""

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

def Main():
	print "game generator main method"

if __name__ == "__main__":
	Main()
