from mc_tree import Tree

"""
converting from [row, col] coordinates to explicit spot in list
	spot = row*dim + col

	e.g. accessing the [1,0] spot on a 3x3 board:
		spot = 1*3 + 0 = 3
		list[spot] == the [1,0] spot on a physical board
"""

print "What position is the computer playing? (1 for X, 0 for 0)"
computer_player = int(raw_input())

print "Who is playing first? (1 for X, 0 for O)"
first_player = int(raw_input())

if computer_player == first_player:
	computer_plays_first = True
else:
	computer_plays_first = False

# set up game
blank_board = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
game_tree = Tree(blank_board, first_player)
game_tree.prop_vals(game_tree.root)

# play computer's move
gamestate = game_tree.root
if computer_plays_first:
	max_value = 0
	for c in gamestate.children:
		if c.value > max_value:
			max_value = c.value

	print max_value
	for c in gamestate.children:
		if c.value == max_value:
			print c.board
			gamestate = c

	print gamestate.value
