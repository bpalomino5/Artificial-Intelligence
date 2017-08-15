# Author: Brandon Palomino
# Date: 8/11/17

from Queue import heapq as hq
from copy import deepcopy
import random
import time

def astar(start,h,d=None):
	explored=set()
	open = []
	hq.heappush(open,Node(start))

	while open:
		current = hq.heappop(open)
		if d >= 2:
			if current.g == d:
				if isGoal(current):
					return [current.g,len(open) + len(explored)+1]
				else:
					return None

		if isGoal(current):
			return [current.g,len(open) + len(explored)+1]
		explored.add(str(current))

		for succ in successors(current):
			if str(succ) not in explored:
				succ.g = current.g + 1
				succ.f = succ.g + h(succ)
				hq.heappush(open,succ)
	return None

# Number of misplaced tiles
def h1(node):
	return sum(x!=y for x,y in zip(node.state,"012345678"))

# Manhattan distance
def h2(node):
	sum =0
	for c in "12345678":
		sum += manhattandistance(node.state.index(c), "012345678".index(c))
	return sum

def manhattandistance(n,m):
	return abs((n - m) / 3) + abs( ((n / 3) % 3) - ((m / 3) % 3))

# function which gets successors of the current node and returns a list of successors
def successors(node):
	k=3
	N=9
	succ = []
	if node.pos0 >= k:
		createSucc(node,node.pos0-k,succ)
	if node.pos0 < N-k:
		createSucc(node,node.pos0+k,succ)
	if (node.pos0 % k) > 0:
		createSucc(node,node.pos0-1,succ)
	if (node.pos0 % k) < k-1:
		createSucc(node,node.pos0+1,succ)
	return succ

def createSucc(node,i,succ):
	n = deepcopy(node)
	swap(n,i,node.pos0)
	n.pos0 = i
	succ.append(n)

def isGoal(Node):
	return Node.state == "012345678"

def swap(node,a,b):
	values = list(node.state)
	
	temp = values[a]
	values[a] = values[b]
	values[b] = temp

	node.state = ''.join(values)

def isSolvable(state):
	count=0
	for i in range(8):
		for j in range(i+1,9):
			if int(state[j]) and int(state[i]) and int(state[i]) > int(state[j]):
				count+=1
	return count%2==0

# Node object to handle 
class Node(object):
	f=0
	g=0
	pos0=None
	parent=None
	def __init__(self, state=""):
		self.state = state
		if self.state != "":
			self.pos0 = state.find("0")
	def __cmp__(self, other):
		return cmp(self.f, other.f)
	def __eq__(self,other):
		return self.state == other.state 
	def __str__(self):
		return self.state
	def __repr__(self):
		return str(self)

def createPuzzle():
	print '\nEnter puzzle values (Enter 3 values at a time):'
	r1 = raw_input()
	r2 = raw_input()
	r3 = raw_input()
	return str(r1+r2+r3)

def printPuzzle(puzzle):
	print "\n8-Puzzle:"
	for i in range(9):
		print puzzle[i],
		if i == 2 or i == 5:
			print ""
	print ""


if __name__ == '__main__':
	# Prompt
	"""
	print "8-Puzzle Project Analysis"
	while True:
		print "[1] Generate Random 8-Puzzle"
		print "[2] Input 8-Puzzle"
		print "[3] Exit\n"
		print "Command: ",
		command = input()
	
		if command == 1:
			puzzle = "".join(random.sample("012345678", len("012345678")))
		elif command == 2:
			puzzle = createPuzzle()
		elif command == 3:
			print "Done"
			break

		if isSolvable(puzzle):
			printPuzzle(puzzle) 
			print "\nh1:"
			c = astar(puzzle,h1)
			print "Search Cost: ", c[1]
			print "Solution Depth:",c[0]
			print ""
			print ""

			print "h2:"
			c = astar(puzzle,h2)
			print "Search Cost: ", c[1]
			print "Solution Depth:",c[0]
			print ""
		else:
			print "Puzzle inputed is not solvable. Try Again!\n"
			continue
	"""
	# Get Solution Depths
	depth = 2
	print "depth = ",depth
	i=0
	while i < 100:
		puzzle = "".join(random.sample("012345678", len("012345678")))
		if isSolvable(puzzle):
			c = astar(puzzle,h2,depth)
			if c:
				if c[0] == depth:
					print "i:",i,puzzle
					i+=1

	
	# t1 = time.time()
	# t2 = time.time()
	# str((t2-t1) * 1000) = ms of time