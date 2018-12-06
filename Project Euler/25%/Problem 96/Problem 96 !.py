import time
import math

start_time = time.clock()

# use backtracking to check for every possible valid solution

n = 9
numbers_sum = 0
count = 1

# check whether the 3x3 square to which (r, c) belongs 
# can contain elem at (r, c) or not
def IsSafeSubgrid (grid, r, c, elem):

	lower_r = r - (r%3)
	lower_c = c - (c%3)	

	for row in xrange (lower_r, lower_r+3):
		for col in xrange (lower_c, lower_c+3):

			if (row == r and col == c):
				continue

			if (grid[row][col] == elem):
				return False

	return True				


# check if a given arrangement is valid safe or not
def IsSafeState (grid, r, c, elem):

	# check along the row
	for col in xrange(n):
		if (col == c):
			continue

		if (grid[r][col] == elem):
			return False


	# check along the column
	for row in xrange(n):
		if (row == r):
			continue

		if (grid[row][c] == elem):
			return False	


	# check in the sub-grid
	return IsSafeSubgrid(grid, r, c, elem)	


# starting from top-left cell and iterating row-by-row, find the first unassigned cell
def FindUnassigned (grid):

	for r in xrange(n):
		for c in xrange(n):
			if (grid[r][c] == 0):
				return [r, c]

	return [-1, -1]


def SolveSudoku (grid):

	cell = FindUnassigned(grid)
	if (cell[0] == -1):
		return True

	r, c = cell

	for elem in xrange (1, n+1):

		# check if putting elem at (r, c) is safe
		if (not IsSafeState(grid, r, c, elem)):
			continue

		grid[r][c] = elem	

		# check if this placement can solve the Sudoku
		if (SolveSudoku(grid)):
			return True

		# since the above placement cannot solve the Sudoku, reset (r, c)
		grid[r][c] = 0	

	return False	


# add the top three digits to a global variable
def AddThreeDigitNumber (grid):
	
	SolveSudoku(grid)

	curr_sum = 0
	curr_sum += (100 * grid[0][0])
	curr_sum += (10 * grid[0][1])
	curr_sum += (grid[0][2])

	# global count
	# print count, curr_sum
	# count += 1

	global numbers_sum
	numbers_sum += curr_sum


def PrintGrid (grid):

	for row in grid:
		print row	



if __name__ == '__main__':

	filename = "p096_sudoku.txt"
	fp = open(filename, "r")		

	grid = []
	flag = 0

	# in the loop, whenever we reach a 'Grid $$' line,
	# we solve the Sudoku above that line (which is currently in grid[][])
	# then we reset grid[][] to an empty list 
	for line in fp:

		# takes care of 'Grid 01', since grid[][] is empty
		if (flag == 0):
			flag = 1
			continue

		# if the current line is 'Grid $$', solve the grid
		if (str(line)[0] == 'G'):
			AddThreeDigitNumber(grid)
			grid = []
			continue

		# else, add the current line to the list of rows
		row = list(str(line))
		if (len(row) > n):
			# pop the '\n' character
			row.pop()

		row = map(int, row)
		grid.append(row)


	# since the 'if' condition broke the loop after 49 Sudoku's
	AddThreeDigitNumber(grid)
	
	print numbers_sum
	
	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
	