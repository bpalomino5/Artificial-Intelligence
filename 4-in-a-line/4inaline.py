# Author: Brandon Palomino
# Date: 8/31/17
# Description: Program where user plays 4 in a line game against CPU that uses alpha-beta pruning to calculate best moves

from copy import deepcopy
letters = ["A","B","C","D","E","F","G","H"]

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
	# letters = ["A","B","C","D","E","F","G","H"]
	print "Enter your move: ",
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

def makeMoveAI(board):
	result = minimax(board,2,negInfinity,posInfinity,False)
	return result[1]

def makeMove(board):
	# letters = ["A","B","C","D","E","F","G","H"]
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

negInfinity = -99999999
posInfinity =  99999999
def minimax(board,depth,alpha,beta, maximizingPlayer):
	if depth == 0:
		return evaluation(board)

	if maximizingPlayer:
		v = negInfinity
		for succ in successors(board,maximizingPlayer):
			v = max(v, minimax(succ, depth -1, alpha, beta, False))
			if v > alpha:
				alpha = v
				best=succ
			if beta <= alpha:
				break
		return [v,best]

	else:
		v = posInfinity
		for succ in successors(board,maximizingPlayer):
			v = min(v, minimax(succ, depth-1, alpha, beta, True))
			if v < beta:
				beta = v
				best=succ
			if beta <= alpha:
				break
		return [v,best]

def successors(board,max):
	next = []
	for i in range(8):
		for j in range(8):
			if board[i][j]=="-":
				b = deepcopy(board)
				if max:
					b[i][j]="O"
				else:
					b[i][j]="X"
				next.append(b)
	return next

def evaluation(board):
	score = 0
	player = "O"
	# horizontal check 4-in-a-row
	for j in range(8-3):
		for i in range(8-3):
			if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:
				score+=1000

	# vertical check 4-in-a-row
	for i in range(8-3):
		for j in range(8-3):
			if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == player and board[i+3][j] == player:
				score+=1000

	# horizontal check 3-in-a-row
	for j in range(8-3):
		for i in range(8-3):
			if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == "-" or board[i][j] == "-" and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:
				score+=100

	# vertical check 3-in-a-row
	for i in range(8-2):
		for j in range(8-2):
			if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == player and board[i][j+3] == "-" or board[i][j] == "-" and board[i+1][j] == player and board[i+2][j] == player and board[i][j+3] == player:
				score+=100

	# horizontal check 2-in-a-row
	for j in range(8-3):
		for i in range(8-3):
			if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == "-" and board[i][j+3] == "-" or board[i][j] == "-" and board[i][j+1] == "-" and board[i][j+2] == player and board[i][j+3] == player:
				score+=10

	# vertical check 2-in-a-row
	for i in range(8-3):
		for j in range(8-3):
			if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == "-" and board[i+3][j] == "-" or board[i][j] == "-" and board[i+1][j] == "-" and board[i+2][j] == player and board[i+3][j] == player:
				score+=10

	# horizontal check 1-in-a-row
	for j in range(8-3):
		for i in range(8-3):
			if board[i][j] == player and board[i][j+1] == "-" and board[i][j+2] == "-" and board[i][j+3] == "-" or board[i][j] == "-" and board[i][j+1] == "-" and board[i][j+2] == "-" and board[i][j+3] == player:
				score+=1

	# vertical check 1-in-a-row
	for i in range(8-3):
		for j in range(8-3):
			if board[i][j] == player and board[i+1][j] == "-" and board[i+2][j] == "-" and board[i+3][j] == "-" or board[i][j] == "-" and board[i+1][j] == "-" and board[i+2][j] == "-" and board[i+3][j] == player:
				score+=1

	player = "X"
	# horizontal check 4-in-a-row
	for j in range(8-3):
		for i in range(8-3):
			if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:
				score-=1000

	# vertical check 4-in-a-row
	for i in range(8-3):
		for j in range(8-3):
			if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == player and board[i+3][j] == player:
				score-=1000

	# horizontal check 3-in-a-row
	for j in range(8-3):
		for i in range(8-3):
			if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == "-" or board[i][j] == "-" and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:
				score-=100

	# vertical check 3-in-a-row
	for i in range(8-3):
		for j in range(8-3):
			if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == player and board[i][j+3] == "-" or board[i][j] == "-" and board[i+1][j] == player and board[i+2][j] == player and board[i][j+3] == player:
				score-=100

	# horizontal check 2-in-a-row
	for j in range(8-3):
		for i in range(8-3):
			if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == "-" and board[i][j+3] == "-" or board[i][j] == "-" and board[i][j+1] == "-" and board[i][j+2] == player and board[i][j+3] == player:
				score-=10

	# vertical check 2-in-a-row
	for i in range(8-3):
		for j in range(8-3):
			if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == "-" and board[i+3][j] == "-" or board[i][j] == "-" and board[i+1][j] == "-" and board[i+2][j] == player and board[i+3][j] == player:
				score-=10

	# horizontal check 1-in-a-row
	for j in range(8-3):
		for i in range(8-3):
			if board[i][j] == player and board[i][j+1] == "-" and board[i][j+2] == "-" and board[i][j+3] == "-" or board[i][j] == "-" and board[i][j+1] == "-" and board[i][j+2] == "-" and board[i][j+3] == player:
				score-=1

	# vertical check 1-in-a-row
	for i in range(8-3):
		for j in range(8-3):
			if board[i][j] == player and board[i+1][j] == "-" and board[i+2][j] == "-" and board[i+3][j] == "-" or board[i][j] == "-" and board[i+1][j] == "-" and board[i+2][j] == "-" and board[i+3][j] == player:
				score-=1
	return score

if __name__ == '__main__':
	# settings = setup()
	# board = settings[0]
	# printboard(board)
	# while True:
	# 	getMove(board)
	# 	if checkGameOver(board,"O"):
	# 		print "Player 1 wins!"
	# 		break
	# 	board = makeMoveAI(board)
	# 	if checkGameOver(board,"X"):
	# 		print "AI wins!"
	# 		break

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

	# testing successors()
	# board = [["-"]*8 for i in range(8)]
	# board[0][0]="O"
	# board[1][0]="O"
	# board[2][0]="O"
	# board[3][1]="X"
	# board[3][2]="X"
	# board[3][3]="X"
	# board[3][4]="X"
	# printboard(board)
	# print "succs"
	# for succ in successors(board,False):
	# 	printboard(succ)

	#testing minimax
	board = [["-"]*8 for i in range(8)]
	board[0][0]="O"
	board[1][0]="O"
	board[2][0]="O"
	board[3][1]="X"
	board[3][2]="X"
	board[3][3]="X"

	printboard(board)
	result = minimax(board,2,negInfinity,posInfinity,False)
	print result
	printboard(result[1])

	# board = result[1]
	# result = minimax(board,2,negInfinity,posInfinity,True)
	# printboard(result[1])