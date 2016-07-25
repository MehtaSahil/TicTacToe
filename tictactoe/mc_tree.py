from board import Board
from game_generator import GameGenerator
import collections

class Tree:

	"""
	TODO : function to propogate weights from the leaves
	"""

	def __init__(self, startboard, player):
		self.root = self.build_tree(startboard, player)

	def build_tree(self, startboard, player):
		gen = GameGenerator()
		gs = collections.deque()
		gs.appendleft(Board(startboard))

		first_player = player
		root = gs.pop()
		next_boards = gen.simple_perms(root.board, first_player)

		if len(next_boards) != 0:
			root.children = collections.deque()
			for l in next_boards:
				newboard = Board(l)
				gs.appendleft(newboard)
				root.add_child(newboard)

		first_player = 1 - first_player

		node_process_limit = len(startboard)
		process_level = len(startboard)
		nodes_processed = 0

		while gs:
			current = gs.pop()
			next_boards = gen.simple_perms(current.board, first_player)

			# if there exist children to add, initialize and add
			if len(next_boards) != 0:
				current.children = collections.deque()
				for l in next_boards:
					newboard = Board(l)
					gs.appendleft(newboard)
					current.add_child(newboard)

			nodes_processed += 1
			if nodes_processed == node_process_limit:
				first_player = 1 - first_player

				nodes_processed = 0
				node_process_limit *= process_level - 1
				process_level -= 1

		return root

	def print_tree(self):
		q = collections.deque()
		q.appendleft(self.root)

		while q:
			current = q.pop()
			if current.children == None:
				continue

			for c in current.children:
				print c.board
				q.appendleft(c)

def Main():
	perm_list = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
	mc_tree = Tree(perm_list, 1)

	mc_tree.print_tree();

if __name__ == "__main__":
	Main()
