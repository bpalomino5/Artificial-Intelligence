# Author: Brandon Palomino
# Date: 8/23/17
# Description: N-Queen solver for n=22, using two implementations of local search algorithms
import random
def HillClimbing(board):
	current = Node(board)
	while True:
		neighbor = getSuccessor(current)

		# For debugging purposes
		# print "c:",current.getValue()
		# print "n:",neighbor.getValue()
		# print "-------------------"
		if neighbor <= current:
			return current
		current = neighbor


def getSuccessor(n):
	moves = {}
	for i in range(len(n.board)):
		for j in range(len(n.board)):
			if n.board[i] == j:
				continue
			copy = Node(list(n.board))
			copy.board[i] = j
			moves[(i,j)] = copy.getValue()

	best_moves = []
	maxH= n.getValue()
	for k,v in moves.iteritems():
		if v < maxH:
			maxH = v
	for k,v in moves.iteritems():
		if v==maxH:
			best_moves.append(k)

	if len(best_moves) > 0:
	    pick = random.randint(0,len(best_moves) - 1)
	    col = best_moves[pick][0]
	    row = best_moves[pick][1]
	    copy.board = list(n.board)
	    copy.board[col] = row

	return copy

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
	def __cmp__(self,other):
		if self.getValue() >= other.getValue() or other.getValue() == 0:
			return -1
		elif self.getValue() < other.getValue():
			return 1
		else: return 0
		
if __name__ == '__main__':
	# testing steepest ascent hill climbing
	# board = [3,2,1,4,3,2,1,2]
	for i in range(100):
		board = random.sample(range(8),8)
		n = HillClimbing(board)
		print n.board," val:" ,n.getValue()
