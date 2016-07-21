from board import Board
import collections

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

	def get_perms(self, board, player):
		limit = len(board)
		for i in range(0, limit):
			if board[i] == 1 or board[i] == 0:
				continue;

			board[i] = player;
			# print str(board) + " " + str(Board(board).value)
			print board
			if player == 1:
				self.get_perms(board, 0)
			elif player == 0:
				self.get_perms(board, 1)

			board[i] = -1

def Main():
	perm_list = list();
	for i in range(0, 3):
		perm_list.append(-1)

	generator = GameGenerator()

	generator.get_perms(perm_list, 1)

if __name__ == "__main__":
	Main()
