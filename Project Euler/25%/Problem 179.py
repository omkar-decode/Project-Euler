import time
start_time = time.clock()

# the pre-computations in this problem are similar to those of Problem 173


problem_limit = 10000000
sieve_limit = 10000005

# initialise spf[n] to be n (initial value)
spf = [i for i in xrange(sieve_limit)]


# generate a sieve where spf[n] stores the Smallest Prime Factor of n
def SieveSpf ():

	# update all multiples of 2
	for p in xrange(2, sieve_limit, 2):
		spf[p] = 2

	# update for remaining numbers
	for p in xrange(3, sieve_limit, 2):
		
		if (spf[p] == p):
			for j in xrange((p*p), sieve_limit, p):

				if (spf[j] == j):
					spf[j] = p


# this method returns the number of factors of n
def NumFactors (n):

	factor_cnt = 1

	prev_prime = spf[n]
	curr_prime = spf[n]

	curr_expo = 0
	while (n > 1):
		curr_prime = spf[n]

		if (curr_prime == prev_prime):
			curr_expo += 1

		else:
			prev_prime = curr_prime
			factor_cnt *= (curr_expo + 1)
			curr_expo = 1

		n /= spf[n]
		

	if (curr_prime > 1):
		factor_cnt *= (curr_expo + 1)

	return factor_cnt



if __name__ == '__main__':

	SieveSpf()

	pairs = 0

	prev_factors = NumFactors(2)
	curr_factors = 0

	for n in xrange(3, problem_limit):
		curr_factors = NumFactors(n)

		if (curr_factors == prev_factors):
			pairs += 1

		prev_factors = curr_factors
		

	print pairs		

	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
