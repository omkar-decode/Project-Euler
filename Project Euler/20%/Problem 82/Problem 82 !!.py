import time
import math
import itertools

start_time = time.clock()

# use Dynamic Programming by iterating over all the columns
# Refer to the readme file of this problem for a detailed explanation


if __name__ == '__main__':

	dimension = -1

	# grid = [[131, 673, 234, 103, 18],
	# 		[201, 96, 342, 965, 150],
	# 		[630, 803, 746, 422, 111],
	# 		[537, 699, 497, 121, 956],
	# 		[805, 732, 524, 37, 331]]

	fp = open("p082_matrix.txt", "r")
	grid = []

	for line in fp:
		row = line.split(",")

		dimension = len(row)
		row[dimension-1] = row[dimension-1][:(len(row[dimension-1])-1)]
		grid.append(map(int, row))


	# use Dynamic Programming to find optimal path
	up_to_down = [-1 for i in xrange(dimension)]
	down_to_up = [-1 for i in xrange(dimension)]

	for col in xrange (dimension-2, -1, -1):

		# traverse through the column from top to bottom
		up_to_down[0] = grid[0][col] + grid[0][col+1]
		for row in xrange (1, dimension):
			right_cost = grid[row][col+1]
			up_cost = up_to_down[row-1]

			up_to_down[row] = grid[row][col] + min(right_cost, up_cost)


		# traverse through the column from bottom to top	
		down_to_up[dimension-1] = grid[dimension-1][col] + grid[dimension-1][col+1]	
		for row in xrange (dimension-2, -1, -1):
			right_cost = grid[row][col+1]
			down_cost = down_to_up[row+1]

			down_to_up[row] = grid[row][col] + min(right_cost, down_cost)


		# update the corresponding column in the grid
		for row in xrange(dimension):
			grid[row][col] = min(up_to_down[row], down_to_up[row])


	# find the smallest element in the first column of the updated grid
	min_cost = grid[0][0]
	for row in xrange (1, dimension):			
		if (grid[row][0] < min_cost):
			min_cost = grid[row][0]


	print min_cost		

	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"