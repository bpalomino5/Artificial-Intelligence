# Author: Brandon Palomino
# Date: 8/31/17
# Description: Program where user plays 4 in a line game against CPU that uses alpha-beta pruning to calculate best moves

def setup():
	board = [["-"]*8 for i in range(8)]
	print "Would you like to go first (y/n)? : ",
	first = raw_input()
	print "How much time would you like (in seconds) : ",
	timelimit = raw_input()
	return [board,first,timelimit]

def printboard(board):
	print "\n  1 2 3 4 5 6 7 8"
	letters = ["A","B","C","D","E","F","G","H"]
	for i in range(8):
		print letters[i],
		for j in range(8):
			print board[i][j],
		print ""
	print "\n"

def getMove(board):
	letters = ["A","B","C","D","E","F","G","H"]
	print "Enter your move p1: ",
	try:
		move = raw_input()
		if len(move) != 2:
			raise ValueError()

		i = move[0].upper()
		i = letters.index(i)

		j = int(move[1])-1
		if not j >= 0 and j <= 7:
			raise ValueError() 

		#check if free space
		if board[i][j] != "-":
			raise ValueError()
		board[i][j]="O"
	except (ValueError,IndexError):
		print "Invalid move, Try Again!"
		getMove(board)


def makeMove(board):
	letters = ["A","B","C","D","E","F","G","H"]
	print "Enter your move p2: ",
	try:
		move = raw_input()
		if len(move) != 2:
			raise ValueError()

		i = move[0].upper()
		i = letters.index(i)

		j = int(move[1])-1
		if not j >= 0 and j <= 7:
			raise ValueError()

		#check if free space
		if board[i][j] != "-":
			raise ValueError()
		board[i][j]="X"
	except (ValueError,IndexError):
		print "Invalid move, Try Again!"
		makeMove(board)

def checkGameOver(board,player):
	printboard(board)
	# horizontal check
	for j in range(8-3):
		for i in range(8-3):
			if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:
				return True

	# vertical check
	for i in range(8-3):
		for j in range(8-3):
			if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == player and board[i+3][j] == player:
				return True



if __name__ == '__main__':
	settings = setup()
	board = settings[0]
	printboard(board)
	while True:
		getMove(board)
		if checkGameOver(board,"O"):
			print "Player 1 wins!"
			break
		makeMove(board)
		if checkGameOver(board,"X"):
			print "Player 2 wins!"
			break

	# testing checkgameover
	# board = [["-"]*8 for i in range(8)]
	# board[0][0]="O"
	# board[1][0]="O"
	# board[2][0]="O"
	# board[3][1]="X"
	# board[3][2]="X"
	# board[3][3]="X"
	# board[3][4]="X"
	# printboard(board)
	# print checkGameOver(board,"X")

	# testing getMove
	# board = [["-"]*8 for i in range(8)]
	# getMove(board)
	# printboard(board)