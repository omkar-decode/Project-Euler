import time
start_time = time.clock()

# equating [(b/(b+r)) * ((b-1)/(b+r-1))] to 1/2, we get
#	b = [((1+2r) + sqrt(1+8r^2))/2]

# therefore, we require all those values of r which make (1+8r^2) a perfect square
# by investigating the first few values of r satisfying this, we can obtain the following recurrence relation :
#	
#	r(n) = 6*r(n-1) - r(n-2)

# we use this relation to find valid values of r and b


# this method returns the count of blue discs, given a valid count of red discs
def BlueCount (r):

	term = int((1 + (8*r*r)) ** 0.5)
	term += (1 + (2*r))
	term /= 2

	return term


if __name__ == '__main__':
	
	threshold = 10 ** 12

	# b_n is the number of blue balls for a given number of (valid) red balls
	b_n = -1

	# declare the necessary terms for the recurrence relation
	r_n = -1
	r_n_minus_1 = -1
	r_n_minus_2 = -1

	# base case, for r(1) and r(2)
	r_n_minus_2 = 1
	r_n_minus_1 = 6


	while (True):

		r_n = (6 * r_n_minus_1) - r_n_minus_2
		b_n = BlueCount(r_n)
		
		if (b_n + r_n > threshold):
			break

		r_n_minus_2 = r_n_minus_1
		r_n_minus_1 = r_n


	print b_n
	
	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
	
	