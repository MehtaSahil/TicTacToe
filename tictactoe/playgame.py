from mc_tree import Tree
from players.computer import ComputerPlayer
from players.human import HumanPlayer

class Game:
	def __init__(self, starting_board):
		self.starting_board = starting_board

		print "What position is the computer? (1 for X, 0 for O)"
		self.computer_player =  1
		self.human_player = 1 - self.computer_player

		print "Who is playing first? (1 for X, 0 for O)"
		self.first_player = int(raw_input())

		self.computer_plays_first = False
		if self.computer_player == self.first_player:
			self.computer_plays_first = True

		# set up game
		self.game_tree = Tree(self.starting_board, self.first_player)
		self.game_tree.prop_vals(self.game_tree.root)

		# start game loop
		self.loop(self.game_tree.root)

	def loop(self, gamestate):
		comp = ComputerPlayer(self.computer_player)
		human = HumanPlayer(self.human_player)

		print "start board: " + str(gamestate.board)

		# True if it's the computer's turn, else False
		comp_turn = self.computer_plays_first
		while True:
			print "==============================================="

			if comp_turn:
				gamestate = comp.computer_move(gamestate)
				print "computer move: " + str(gamestate.board)
			else:
				gamestate = human.human_move(gamestate)
				print "human move: " + str(gamestate.board)

			comp_turn = not comp_turn

			if gamestate.is_end_game():
				break

		print "game over"
		self.get_winner(gamestate)
		print "final gamestate: " + str(gamestate.board)

	def get_winner(self, gamestate):
		if gamestate.is_win_for(1):
			print "X Wins"
		elif gamestate.is_win_for(0):
			print "O wins"
		else:
			print "Draw"
