# Author: Brandon Palomino
# Date: 8/23/17
# Description: N-Queen solver for n=22, using two implementations of local search algorithms
import random
import time
import math


class Node(object):
	def __init__(self, board=None):
		self.board = board

def annealing(board):
	temp = len(board)**2
	anneal_rate = 0.95
	new_h_cost = getHcost(board)

	steps=0
	while new_h_cost > 0:
		board = make_annealing_move(board,new_h_cost,temp)
		new_h_cost = getHcost(board)
		#Make sure temp doesn't get impossibly low
		new_temp = max(temp * anneal_rate,0.01)
		temp = new_temp
		steps+=1
		if steps >= 50000: 
			break
	return board

def make_annealing_move(board,h_to_beat,temp):
  board_copy = list(board)
  found_move = False
 
  while not found_move:
    board_copy = list(board)
    new_row = random.randint(0,len(board)-1)
    new_col = random.randint(0,len(board)-1)
    board_copy[new_col] = new_row
    new_h_cost = getHcost(board_copy)
    if new_h_cost < h_to_beat:
      found_move = True
    else:
      #How bad was the choice?
      delta_e = h_to_beat - new_h_cost
      #Probability can never exceed 1
      accept_probability = min(1,math.exp(delta_e/temp))
      found_move = random.random() <= accept_probability
  return board_copy


def SimulatedAnnealing(board, schedule):
	current = Node(board)
	t = 1
	while True:
		T = schedule[t]
		if T==0:
			return current
		next = Node(randomSuccessor(current))
		E = getHcost(next) - getHcost(current)
		if E > 0:
			current = next
		else:
			current=next
		t+=1


def HillClimbing(board):
	current = Node(board)
	while True:
		neighbor = Node(getSuccessor(current))

		# For debugging purposes
		# print "c:",current.getValue()
		# print "n:",neighbor.getValue()
		# print "-------------------"
		if getHcost(neighbor.board) >= getHcost(current.board) or getHcost(current.board) == 0:
			return current
		current = neighbor


def getSuccessor(n):
	moves = {}
	for i in range(len(n.board)):
		for j in range(len(n.board)):
			if n.board[i] == j:
				continue
			bcopy = list(n.board)
			bcopy[i] = j
			moves[(i,j)] = getHcost(bcopy)

	best_moves = []
	maxH= getHcost(n.board)
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
	    bcopy = list(n.board)
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
	n = 22
	# testing steepest ascent hill climbing
	print "Hill Climbing"
	avgTime = 0
	numSolutions = 0
	for i in range(100):
		board = random.sample(range(n),n)
		t1 = time.time()
		q = HillClimbing(board)
		t2 = time.time()
		elaspedTime = t2-t1
		h = getHcost(q.board)
		if h==0:
			numSolutions+=1
		print i+1,q.board
		print "h:" ,h
		print "t:",elaspedTime
		avgTime +=elaspedTime
		print "---------------------------"
	avgTime /= 100
	print "Average Time:",avgTime
	print "Percentage of solutions:",numSolutions,"%"
	print ""

	# testing simulated annealing
	print "Simulated Annealing"
	avgTime = 0
	for i in range(100):
		board = random.sample(range(n),n)
		t1 = time.time()
		q = annealing(board)
		t2 = time.time()
		elaspedTime = t2-t1
		print i+1,q
		print "h:",getHcost(q)
		print "t:",elaspedTime
		avgTime+=elaspedTime
		print "----------------------------"
	avgTime /=100
	print "Average Time:",avgTime
