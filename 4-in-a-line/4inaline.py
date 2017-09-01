# Author: Brandon Palomino
# Date: 8/31/17
# Description: Program where user plays 4 in a line game against CPU that uses alpha-beta pruning to calculate best moves

def setup():
	board = [["-"]*8 for i in range(8)]
	return board

def printboard(board):
	print "  1 2 3 4 5 6 7 8"
	letters = ["A","B","C","D","E","F","G","H"]
	for i in range(8):
		print letters[i],
		for j in range(8):
			print board[i][j],
		print ""




if __name__ == '__main__':
	board = setup()
	printboard(board)
	# while True:
	# 	getMove()
	# 	checkGameOver()
	# 	makeMove()
	# 	checkGameOver()