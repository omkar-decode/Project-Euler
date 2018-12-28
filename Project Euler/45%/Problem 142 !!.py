import time
import math
import itertools

start_time = time.clock()

# It can be verified (by taking x-y=a^2 and x+y=(a+k)^2) that x is of the form (a^2 + b^2) and y is
# of the form (2ab).
# Similarly, y is of the form (c^2 + d^2) and z is of the form (2cd)

# For x and z, x is of the form (e^2 + f^2) and z is of the form (2ef), such that 2ef==2cd and 2ab>(2cd==2ef)

# Therefore, we get
#	x = (a^2 + b^2) == (c^2 + d^2)
#	y = 2ab == (c^2 + d^2)
#	z = 2cd == 2ef

# In my solution, I have generated sum of two integer squares upto 1,000,000 (which correspond to values of x) 
# and then checked for possible values of y and z


if __name__ == '__main__':
	
	# limit has been set randomly
	limit = 1000

	min_sum = 10**10
	hypot_freq = {}

	for a in xrange (1, limit):
		for b in xrange (1, a):

			sqr = (a*a + b*b)

			if (sqr in hypot_freq):
				hypot_freq[sqr][0] += 1
			else:
				hypot_freq[sqr] = [1]
			
			hypot_freq[sqr].append([a, b])


	# iterate over possible values of x
	for key in hypot_freq:
		
		# we need x to be expressible as a sum of two squares in at least 2 distinct ways
		if (hypot_freq[key][0] == 1):
			continue

		x = key				
		legs = hypot_freq[key][1:]
		pair_cnt = len(legs)

		for i in xrange (pair_cnt):
			for j in xrange (i):

				first_pair = legs[i]
				second_pair = legs[j]

				y = 2 * max(first_pair[0]*first_pair[1], second_pair[0]*second_pair[1])

				# since y must be of the form (c^2 + d^2)
				if (y not in hypot_freq):
					continue

				z = 2 * min(first_pair[0]*first_pair[1], second_pair[0]*second_pair[1])
				y_vals = hypot_freq[y][1:]

				for val in y_vals:

					if ((2*val[0]*val[1]) == z):	
						# print x, y, z
						if (min_sum > (x+y+z)):
							min_sum = x+y+z
							

	print min_sum

	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
							