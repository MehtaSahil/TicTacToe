from board import Board
from game_generator import GameGenerator
import collections

perm_list = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
gen = GameGenerator()
gs = collections.deque()

gs.appendleft(Board(perm_list))
first_player = 1

root = gs.pop()
next_boards = gen.simple_perms(root.board, first_player)
for l in next_boards:
	newboard = Board(l)
	gs.appendleft(newboard)
	root.children.append(newboard)

if first_player == 1:
	first_player = 0
else:
	first_player = 1

node_process_limit = len(perm_list)
process_level = len(perm_list)
nodes_processed = 0

while gs:
	current = gs.pop()
	next_boards = gen.simple_perms(current.board, first_player)
	for l in next_boards:
		newboard = Board(l)
		gs.appendleft(newboard)
		current.children.append(newboard)

	nodes_processed += 1
	if nodes_processed == node_process_limit:
		if first_player == 1:
			first_player = 0
		else:
			first_player = 1

		nodes_processed = 0
		node_process_limit *= process_level - 1
		process_level -= 1

for c in root.children:
	print c.board
