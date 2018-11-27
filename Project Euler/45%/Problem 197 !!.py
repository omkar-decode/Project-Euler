import time
import math

start_time = time.clock()

# the value of f(x) alternates between two small intervals as the value of x increases
# at x=516, x becomes equal to f(f(x)), meaning the function oscillates between two values

# therefore, for any n >= 516, all u(even_n) are equal and all u(odd_n) are equal 


k = 30.403243784

def f (x):

	# the following step is not required, since x is never in this range in the problem
	# root = (k ** 0.5)

	# # check if the floor function makes it 0
	# if (x > root or x < (-1 * root)):
	# 	return 0

	term = k - (x*x)
	term = 2 ** term
	term = math.floor(term)
	term = term / float(10**9)

	return term


if __name__ == '__main__':
	
	u_prev = -1
	u_curr = 0

	# an upper limit to n, to make the while loop finite
	check_limit = 1000000

	n = 1
	while (True):
		
		u_curr = f(u_prev)

		# check if the convergence point has been reached
		if (f(u_curr) == u_prev):
			# print n
			break

		u_prev = u_curr
		n += 1

		# print "u(%d) = %.9f" %(n, u_curr)

		
	# print u_prev, u_curr
	print (u_prev + u_curr)	
			

	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"	
