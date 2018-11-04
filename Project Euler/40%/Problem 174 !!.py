import time
start_time = time.clock()

# the solution to this problem is almost the same as that of Problem 173
# see readme_173 for explanation

problem_limit = 1000000
sieve_limit = 1000005

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


def CountLaminae (T):
	
	# use the expression (4*k*(N-k)) = T
	T /= 4

	factors = NumFactors(T)
	factors += 1
	
	laminae = (factors // 2)

	# exclude the case where the lamina has no hole
	if (int(T**0.5) == (T**0.5)):
		laminae -= 1

	return laminae


if __name__ == '__main__':

	SieveSpf()

	n = 10
	type_count = [0 for i in xrange(n+1)]

	laminae_count = 0
	summation = 0

	# we need to iterate only over multiples of 4
	for T in xrange(4, problem_limit+1, 4):
		laminae_count = CountLaminae(T)


		if (laminae_count>=1 and laminae_count <= n):
			type_count[laminae_count] += 1
			summation += 1

	
	print summation

	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
