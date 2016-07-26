from board import Board
from game_generator import GameGenerator
import collections

class Tree:
	def __init__(self, startboard, player):
		self.root = self.build_tree(startboard, player)

	def build_tree(self, startboard, player):
		gen = GameGenerator()
		gs = collections.deque()

		# Process root node
		gs.appendleft(Board(startboard))
		first_player = player
		root = gs.pop()
		next_boards = gen.simple_perms(root.board, first_player)

		# If the root has children (it should), init and add
		if len(next_boards) != 0:
			root.children = collections.deque()
			for l in next_boards:
				newboard = Board(l)
				gs.appendleft(newboard)
				root.add_child(newboard)

		# switch player after one move (blank board --> first turn)
		first_player = 1 - first_player

		# Variables to control when the player should switch
		node_process_limit = len(startboard)
		process_level = len(startboard)
		nodes_processed = 0

		# while gamestates queue is not empty
		while gs:
			current = gs.pop()

			# Stop exploring children after one player wins
			# if current.value != 0:
				# continue

			next_boards = gen.simple_perms(current.board, first_player)

			# if there exist children to add, initialize and add
			if len(next_boards) != 0:
				current.children = collections.deque()
				for l in next_boards:
					newboard = Board(l)
					gs.appendleft(newboard)
					current.add_child(newboard)

			# increment the number of nodes processed on this level
			nodes_processed += 1

			# if it's time to move down a layer
			if nodes_processed == node_process_limit:
				# switch player
				first_player = 1 - first_player

				# reset variables
				nodes_processed = 0
				node_process_limit *= process_level - 1
				process_level -= 1

		return root

	# sums values from leaves to reveal the best paths to victory
	def prop_vals(self, root):
		sum = 0

		if root.children == None:
			sum = root.value
		else:
			for c in root.children:
				sum += self.prop_vals(c)

		root.value = sum
		return sum

	def print_tree(self):
		q = collections.deque()
		q.appendleft(self.root)

		# while queue is not empty
		while q:
			current = q.pop()

			# if at a leaf node, print and move on
			# exception caused by null pointer w/o this
			if current.children == None:
				continue

			for c in current.children:
				self.print_node(c)
				q.appendleft(c)

	def print_node(self, node):
		print str(node.board) + " : " + str(node.value)

def Main():
	blank_board = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
	mc_tree = Tree(blank_board, 1)

	mc_tree.prop_vals(mc_tree.root)
	# mc_tree.print_tree()

if __name__ == "__main__":
	Main()
