from board import Board
import collections

combinations = collections.deque()
def get_perms(board, player):
	limit = len(board)
	for i in range(0, limit):
		if board[i] == 1 or board[i] == 0:
			continue;

		board[i] = player;
		combinations.appendleft(board)
		print str(board) + " " + str(Board(board).value)
		if player == 1:
			get_perms(board, 0)
		elif player == 0:
			get_perms(board, 1)

		board[i] = -1

perm_list = list()
list_size = 9
for i in range(0, list_size):
	perm_list.append(-1)

get_perms(perm_list, 1)
print len(combinations)
