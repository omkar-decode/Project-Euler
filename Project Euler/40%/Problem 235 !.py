import time
import math

start_time = time.clock()

# we can see that the function is monotonically decreasing
# hence, we can do a binary search and reach the required value in very few steps


if __name__ == '__main__':
	
	n = 5000
	s_n = -600000000000

	s = 0
	r = 0

	# the initial values of lo and hi are decided by checking the value of the series for some values of r
	# we get that the solution lies between 1 and 1.1
	lo = 1.0
	hi = 1.1

	# keep iterating till the value of the series becomes less than 1 unit away from s_n
	while (abs(s-s_n) > 1):

		r = (lo + hi)/2.0

		# evaluate series sum
		s = sum([(900 - 3*k) * (r**(k-1)) for k in xrange(1, n+1)])
	
		if (s > s_n):
			lo = r
		else:
			hi = r	


	print format(r, '.13g')

	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
