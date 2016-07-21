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

	def get_all_perms(self, board, player):
		limit = len(board)
		for i in range(0, limit):
			if board[i] == 1 or board[i] == 0:
				continue;

			board[i] = player;
			print board
			if player == 1:
				self.get_perms(board, 0)
			elif player == 0:
				self.get_perms(board, 1)

			board[i] = -1

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

	def get_inorder_perms(self, board, player):
		q = collections.deque()
		return_q = collections.deque()

		q.appendleft(board)

		first_player = player
		next_boards = self.simple_perms(q.pop(), first_player)
		for l in next_boards:
			q.appendleft(l)

		if first_player == 1:
			first_player = 0
		else:
			first_player = 1

		node_process_limit = len(board)
		process_level = len(board)
		nodes_processed = 0

		while q:
			current = q.pop()
			# print current
			return_q.appendleft(Board(current))

			next_boards = self.simple_perms(current, first_player)
			for l in next_boards:
				q.appendleft(l)

			# only change player after exploring
			# ALL moves for that player
			nodes_processed += 1
			if nodes_processed == node_process_limit:
				if first_player == 1:
					first_player = 0
				else:
					first_player = 1

				nodes_processed = 0
				node_process_limit *= process_level - 1
				process_level -= 1

		return return_q

def Main():
	q = collections.deque()
	perm_list = list();
	for i in range(0, 9):
		perm_list.append(-1)

	gen = GameGenerator()
	q = gen.get_inorder_perms(perm_list, 1)
	while q:
		print q.pop().board

if __name__ == "__main__":
	Main()
