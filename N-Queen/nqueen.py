# Author: Brandon Palomino
# Date: 8/23/17
# Description: N-Queen solver for n=22, using two implementations of local search algorithms
import random
def HillClimbing(board):
	current = Node(board)

	while True:
		neighbor = getSuccessor(current)
		if neighbor.getValue() >= current.getValue():
			return current
		current = neighbor


def getSuccessor(n):
	moves = {}
	for i in range(len(n.board)):
		for j in range(len(n.board)):
			if n.board[i] == j:
				continue
			board_copy = list(n.board)
			board_copy[i] = j
			moves[(i,j)] = getHcost(board_copy)
	
	best_moves = []
	hbeat= getHcost(n.board)
	for k,v in moves.iteritems():
		if v < hbeat:
			hbeat = v
	for k,v in moves.iteritems():
		if v==hbeat:
			best_moves.append(k)

	if len(best_moves) > 0:
	    pick = random.randint(0,len(best_moves) - 1)
	    col = best_moves[pick][0]
	    row = best_moves[pick][1]
	    n.board[col] = row
	return Node(n.board)

class Node(object):
	def __init__(self, board=None):
		self.board = board
	def getValue(self):
		h=0
		for i in range(len(self.board)):
			for j in range(i + 1, len(self.board)):
				if self.board[i] == self.board[j]:
					h+=1
				offset = j-i
				if self.board[i] == self.board[j] - offset or self.board[i] == self.board[j] + offset:
					h+=1
		return h

def getHcost(board):
	h=0
	for i in range(len(board)):
		for j in range(i + 1, len(board)):
			if board[i] == board[j]:
				h+=1
			offset = j-i
			if board[i] == board[j] - offset or board[i] == board[j] + offset:
				h+=1
	return h
		
if __name__ == '__main__':
	# testing node
	# n = Node([0,0,1,2,4])
	# m = Node([2,7,3,6,0,5,1,4])
	# print n.getValue()
	# print m.getValue()
	n = HillClimbing([0,0,1,2,4])
	m = HillClimbing([3,2,1,4,3,2,1,2])
	print getHcost([3,2,1,4,3,2,1,2])
	print m.getValue()

	# moves = {}
	# for i in range(len(n.board)):
	# 	for j in range(len(n.board)):
	# 		if n.board[i] == j:
	# 			continue
	# 		board_copy = list(n.board)
	# 		board_copy[i] = j
	# 		moves[(i,j)] = getHcost(board_copy)
	
	# best_moves = []
	# hbeat= getHcost(n.board)
	# for k,v in moves.iteritems():
	# 	print k,v
	# 	if v < hbeat:
	# 		hbeat = v
	# print hbeat
	# for k,v in moves.iteritems():
	# 	if v==hbeat:
	# 		best_moves.append(k)

	# if len(best_moves) > 0:
	#     pick = random.randint(0,len(best_moves) - 1)
	#     col = best_moves[pick][0]
	#     row = best_moves[pick][1]
	#     n.board[col] = row
   
