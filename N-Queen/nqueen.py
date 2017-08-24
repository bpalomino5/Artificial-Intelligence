import random
import time
import math

# Author: Brandon Palomino
# Date: 8/23/17
# Description: N-Queen solver for n=22, using two implementations of local search algorithms

def SimulatedAnnealing(board):
	T = len(board)**2
	anneal_rate = 0.95
	h = getHcost(board)

	i=0
	while h > 0:
		board = getAnnealingSuccessor(board,h,T)
		h = getHcost(board)
		T = max(T * anneal_rate,0.01)
		i+=1
		if i >= 50000: 
			break
	return board

def getAnnealingSuccessor(board,maxH,T):
  bcopy = list(board)
  found = False
 
  while not found:
    bcopy = list(board)
    row = random.randint(0,len(board)-1)
    col = random.randint(0,len(board)-1)
    bcopy[col] = row
    h = getHcost(bcopy)
    if h < maxH:
      found = True
    else:
      dE = maxH - h
      probability = min(1,math.exp(dE/T))
      found = random.random() <= probability
  return bcopy

def HillClimbing(board):
	current = board
	while True:
		neighbor = getHillSuccessor(current)
		if getHcost(neighbor) >= getHcost(current) or getHcost(current) == 0:
			return current
		current = neighbor

def getHillSuccessor(board):
	moves = {}
	for i in range(len(board)):
		for j in range(len(board)):
			if board[i] == j:
				continue
			bcopy = list(board)
			bcopy[i] = j
			moves[(i,j)] = getHcost(bcopy)

	best_moves = []
	maxH= getHcost(board)
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
	    bcopy = list(board)
	    bcopy[col] = row
	return bcopy

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
	print "N-Queen Solver"
	n = 8
	size=100
	print "n:",n,"\n"

	# testing steepest ascent hill climbing
	print "Hill Climbing"
	print "*************"
	avgTime = 0
	numSolutions = 0
	for i in range(size):
		board = random.sample(range(n),n)
		t1 = time.time()
		q = HillClimbing(board)
		t2 = time.time()
		elaspedTime = t2-t1
		h = getHcost(q)
		if h==0:
			numSolutions+=1
		print i+1,q
		print "h:" ,h
		print "t:",elaspedTime
		avgTime +=elaspedTime
		print "----------------------------------------------------------------------------------"
	avgTime /= 100
	print "Average Time:",avgTime
	print "Percentage of solutions:",numSolutions,"%"
	print ""

	# testing simulated annealing
	print "Simulated Annealing"
	print "*******************"
	avgTime = 0
	numSolutions = 0
	for i in range(size):
		board = random.sample(range(n),n)
		t1 = time.time()
		q = SimulatedAnnealing(board)
		t2 = time.time()
		elaspedTime = t2-t1
		h = getHcost(q)
		if h==0:
			numSolutions+=1
		print i+1,q
		print "h:",h
		print "t:",elaspedTime
		avgTime+=elaspedTime
		print "----------------------------------------------------------------------------------"
	avgTime /=100
	print "Average Time:",avgTime
	print "Percentage of solutions:",numSolutions,"%"

