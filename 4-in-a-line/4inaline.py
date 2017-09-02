# Author: Brandon Palomino
# Date: 9/1/17
# Description: Program where user plays 4 in a line game against CPU that uses alpha-beta pruning to calculate best moves

from copy import deepcopy
import time

letters = ["A","B","C","D","E","F","G","H"]
negInfinity = -99999999
posInfinity =  99999999
timeLimit = 30

def setup():
	global timeLimit
	board = [["-"]*8 for i in range(8)]
	print "4 in a Line Game!"
	print "Would you like to go first (y/n)? : ",
	first = raw_input()
	print "How much time will the AI run for? (in seconds) : ",
	time = raw_input()
	if time.isdigit():
		timeLimit = int(time)
	return [board,first]

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
	t1 = time.time()
	result = minimax(board,4,negInfinity,posInfinity,False,t1,timeLimit)
	return result[1]

def makeMove(board):
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
		for i in range(8):
			if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:
				return True

	# vertical check
	for i in range(8-3):
		for j in range(8):
			if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == player and board[i+3][j] == player:
				return True

def minimax(board, depth, alpha, beta, maximizingPlayer,t1,timeLimit):
	bestPosition = board
	t2 = time.time()
	if depth == 0 or (int(round(t2-t1))) >= timeLimit:
		score = evaluation(board)
		return [score,bestPosition]
	else:
		for succ in successors(board,maximizingPlayer):
			if maximizingPlayer:
				score = minimax(succ, depth-1, alpha, beta,False,t1,timeLimit)[0]
				if score > alpha:
					alpha = score
					bestPosition = succ
			else:
				score = minimax(succ, depth-1, alpha, beta,True,t1,timeLimit)[0]
				if score < beta:
					beta = score
					bestPosition = succ
			if alpha >= beta:
				break
	return [score,bestPosition]

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
	for player in ["O","X"]:
		# horizontal check
		for j in range(8-3):
				for i in range(8):
					if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:
						score += 1000 if player=="O" else -1000
					if 	   board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == "-" \
						or board[i][j] == "-" and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:						
						score += 100 if player=="O" else -100
					if 	   board[i][j] == player and board[i][j+1] == player and board[i][j+2] == "-" and board[i][j+3] == "-" \
						or board[i][j] == "-" and board[i][j+1] == "-" and board[i][j+2] == player and board[i][j+3] == player:
						score += 10 if player=="O" else -10
					if 	   board[i][j] == player and board[i][j+1] == "-" and board[i][j+2] == "-" and board[i][j+3] == "-" \
						or board[i][j] == "-" and board[i][j+1] == "-" and board[i][j+2] == "-" and board[i][j+3] == player:
						score += 1 if player=="O" else -1
		# # vertical check
		for i in range(8-3):
			for j in range(8):
					#vertical check
					if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == player and board[i+3][j] == player:
						score += 1000 if player=="O" else -1000
					if 	   board[i][j] == player and board[i+1][j] == player and board[i+2][j] == player and board[i+3][j] == "-" \
						or board[i][j] == "-" and board[i+1][j] == player and board[i+2][j] == player and board[i+3][j] == player:
						score += 100 if player=="O" else -100
					if 	   board[i][j] == player and board[i+1][j] == player and board[i+2][j] == "-" and board[i+3][j] == "-" \
						or board[i][j] == "-" and board[i+1][j] == "-" and board[i+2][j] == player and board[i+3][j] == player:
						score += 10 if player=="O" else -10
					if 	   board[i][j] == player and board[i+1][j] == "-" and board[i+2][j] == "-" and board[i+3][j] == "-" \
						or board[i][j] == "-" and board[i+1][j] == "-" and board[i+2][j] == "-" and board[i+3][j] == player:
						score += 1 if player=="O" else -1
	return score

if __name__ == '__main__':
	settings = setup()
	board = settings[0]
	if settings[1].upper() == 'N':
		board = makeMoveAI(board)

	printboard(board)
	while True:
		getMove(board)
		if checkGameOver(board,"O"):
			print "Player 1 wins!"
			break
		board = makeMoveAI(board)
		if checkGameOver(board,"X"):
			print "AI wins!"
			break
