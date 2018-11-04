import time
start_time = time.clock()

# consider N to be the side length of the lamina &
# k is the 'thickness' of the lamina
# Eg: in the first instance given in the problem, N=6 & k=2
# in the second instance, N=9 & k=1

# if we have to make a lamina with T tiles, we can derive the expression
# 	(4 * k * (N-k)) = T

# Therefore, T must be a multiple of 4 and the number of laminae for a given T 
# will be the number of factors of (T/4) which are less than or equal to sqrt(T/4)

# This can be written as:
# 	number of laminae = ((Total number of factors of T/4) + 1) // 2
# the above expression takes care for both odd and even T/4

# Note: since we are considering laminae with a hole, all the cases where the lamina has no hole must be ignored
# the number to be subtracted is simply the number of perfect squares from 1 to 250,000 (inclusive)


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

	# exclude the case where the lamina has no hole (done in the 'main' method)
	# if (int(T**0.5) == (T**0.5)):
	# 	laminae -= 1

	return laminae


if __name__ == '__main__':

	SieveSpf()

	laminae_count = 0

	# we need to iterate only over multiples of 4
	for T in xrange(4, problem_limit+1, 4):
		laminae_count += CountLaminae(T)

	# subtract the cases where the lamina has no hole (perfect square cases)
	laminae_count -= int((problem_limit/4) ** 0.5)	

	print laminae_count	

	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
