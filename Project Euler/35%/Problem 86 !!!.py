import time
start_time = time.clock()

# How to generate all primitive pythagorean triplets: http://mathforum.org/library/drmath/view/55811.html

# We can calculate that the shortest path length is given by the expression
#	d = sqrt[l^2 + (b + h)^2]
# Here, l is the longest dimension of the cuboid

# So the idea is to generate all possible pythagorean triplets upto a limit and consider the two
# shorter sides of the triplet

# one side would represent l and the other would represent (b+h)
# using this, calculate the number of unique cuboids possible

# NOTE: the pythagorean triplets are generated according to the following conditions:
#	given two integers m and n such that-
#		1) m > n
#		2) m and n are coprime
#		3) m and n have different parity
#
#	we will have the two sides as --> s1 = (m^2 - n^2) and s2 = (2mn)
#	
#	This method will generate all primitive triplets, so we will have to consider their multiples separately


# POSSIBLE IMPROVEMENT -->  instead of incrementally searching for all values of M, find a M' such that
#							the number of valid cuboids upto M' is greater (by any amount) than 1,000,000
#							Eg. M = 2000 gives number of cuboids as 1,229,543
#
#							Now, apply binary search on M between 100 (given in the problem) and 2000
#							to find the value of optimal M  							


def Gcd (m, n):

	if (m < n):
		m, n = n, m

	while (n != 0):
	
		rem = m%n
		m = n
		n = rem	

	return m


# count the number of cuboids having l < (b+h)
def Type1Cuboids (l, b_plus_h, lim):
	
	cnt = 0
	factor = 1

	l_next = l
	b_plus_h_next = b_plus_h
	
	# this loop iterates over all the multiples of a primitive triplet
	while (l*factor <= lim):

		# there are multiple scenarios to be considered, when updating count for a particular triplet
		# the conditions can be verified by considering examples of each type
		
		if ((b_plus_h_next) > (2*lim)):
			break

		if ((b_plus_h_next) > (2*l_next)):
			break	

		
		if ((b_plus_h_next/2) > l_next):
			cnt += (((b_plus_h_next)/2) - l_next + 1)
		else:
			if (b_plus_h_next % 2 == 0):
				cnt += (l_next - ((b_plus_h_next)/2) + 1)
			else:
				cnt += (l_next - ((b_plus_h_next)/2))	

		
		if ((b_plus_h_next - l_next) > lim):
			cnt -= (b_plus_h_next - l_next - lim)


		factor += 1

		l_next = (l * factor)
		b_plus_h_next = (b_plus_h * factor)


	return cnt	


# count the number of cuboids having l > (b+h)
def Type2Cuboids (l, b_plus_h, lim):

	cnt = 0
	factor = 1

	while (l*factor <= lim):

		cnt += ((b_plus_h*factor)/2)
		factor += 1

	return cnt	


# given two shorter (coprime) sides of a right triangle, find the number of (unique) possible l, b and h 
# the two given sides (x and y) represent the l and (b+h) of the cuboid
def CountCuboids (x, y, lim):

	cnt = 0

	# case 1: l < (b+h)
	l = min(x, y)
	b_plus_h = max(x, y)

	cnt += Type1Cuboids(l, b_plus_h, lim)
	

	#case 2: l > (b+h)
	l = max(x, y)
	b_plus_h = min(x, y)

	if (l <= lim):
		cnt += Type2Cuboids(l, b_plus_h, lim)

	return cnt	



if __name__ == '__main__':
	
	# generate primitive pythagorean triplets by the m-n-method
	generator_limit = 200

	threshold = 1000000
	routes = 0	

	# start with M=100, since its result is given in the problem
	side_limit = 2000
	while (True):

		routes = 0
		for m in xrange(2, generator_limit+1):
			for n in xrange(1, m):

				if ((m%2) ^ (n%2) == 0):
					continue

				if (Gcd(m, n) > 1):
					continue


				term1 = (2*m)*n
				term2 = ((m*m) - (n*n))

				if (min(term1, term2) > side_limit):
					continue

				routes += CountCuboids(term1, term2, side_limit)

		if (routes > 0):
			break

		side_limit += 1
		

	print side_limit, routes

	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"				


	
	



