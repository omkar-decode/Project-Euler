import numpy

import time
start_time = time.clock()

# the idea is to find the BOP for each degree upto 10 and find the corresponding FIT
# use numpy module to solve linear equations in n variables


# PolynomialEval(x) method returns P(x)
def PolynomialEval (coeffs, n):

	degree = len(coeffs) - 1
	expo_term = (n ** degree)

	val = 0
	for i in xrange(degree+1):
		val += (coeffs[i] * expo_term)
		expo_term /= n

	return val	


if __name__ == '__main__':

	# the given polynomial generating function
	polynomial_GF = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]

	
	# poly_vals stores the values of the given polynomial for n=1 to n=10
	poly_vals = []
	for n in xrange(1, 12):
		poly_vals.append(PolynomialEval(polynomial_GF, n))


	# sum of all First Incorrect Terms
	FIT_sum = 0

	# d is the degree of the current Optimum Polynomial
	for d in xrange(0, 10):
		
		# coeff_arr stores the coefficients of all equations formed by substituting for n
		# in the optimum polynomial of degree d
		coeff_arr = [[] for i in xrange(d+1)]
		for i in xrange(d+1):

			term = (i+1)**d
			for j in xrange(d+1):
				coeff_arr[i].append(term)
				term /= (i+1)
		

		# lhs is the coefficient matrix
		# rhs is the value matrix
		lhs = numpy.array(coeff_arr)
		rhs = numpy.array([poly_vals[i] for i in xrange(d+1)])


		# use numpy to solve the equations
		solution = numpy.linalg.solve(lhs, rhs)

		# round the result to the nearest integer
		solution = map(int, [round(i, 0) for i in solution])

		# calculate the FIT for the current BOP
		# the FIT would occur for n = (d+2)
		curr_fit = PolynomialEval(solution, d+2)

		if (curr_fit != poly_vals[d+1]):
			FIT_sum += curr_fit


	print FIT_sum
	
	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"	