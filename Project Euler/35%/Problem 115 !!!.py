import time
import math
import itertools

start_time = time.clock()

# identical logic as Problem 114
# for detailed explanation, refer to 'readme_114.txt'

def nCr (n, r):

	if (r == 0):
		return 1

	val = 1
	for i in xrange (1, r+1):
		val *= (n-i+1)
		val /= i

	return val		


# n is the length of the row
# m is the minimum length of 1 tile
def CountArrangements (m, n):
	
	# initialised to 1, corresponding to the case where 0 tiles are arranged
	arrangements = 1

	# max_tiles is the overall maximum number of tiles that can 
	# be arranged in the row given the constraints
	max_tiles = (n+1)/(m+1)

	# k is the total number of tiles in the current iteration
	for k in xrange (1, max_tiles+1):
		
		expo = (2*k)+1

		req_coeff = n - ((m*k)+k-1)
		upper = (expo + req_coeff - 1)

		arrangements += nCr(upper, req_coeff)


	return arrangements		



if __name__ == '__main__':
	
	m = 50
	threshold = 1000000

	# start checking from n=(m+1)
	n = 51
	while (True):
		if (CountArrangements(m, n) > threshold):
			break

		n += 1
		
		
	print n		

	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
