import math
import time

start_time = time.clock()

# the idea is to create a list (say prime_list[]) of all primes upto (prime_limit =) 5*10^7, 
# since for any number (say k) greater than prime_limit, 2*k would exceed 10^8

# start iterating over primes, starting with 2 
# suppose current prime is p, then check how many primes in prime_list[] which are
# greater than p CANNOT be multiplied with p to produce a semiprime (since it exceeds 10^8)

# the above can be done by maintaining a pointer (say ptr) which initially points to the end of prime_list
# for every prime (say p_curr), bring the pointer back minimum number of times such
# that (prime_list[ptr] * p_curr) < 10^8

# NOTE: for any prime p, check only for all primes GREATER than p (to avoid repititions)


problem_limit = 100000000
sieve_limit = 100000000

sieve_limit /= 2


# initialise spf[n] to be n (initial value)
is_prime = [True for i in xrange(sieve_limit)]

# primes stores the list of primes (sorted) upto sieve_limit
primes = [-1]

# number of primes less than sieve_limit
prime_count = 0


# generate a sieve where spf[n] stores the Smallest Prime Factor of n
def SieveAlgorithm ():

	is_prime[0] = False
	is_prime[1] = False

	global prime_count
		
	# update for remaining numbers
	for p in xrange(2, sieve_limit):
		
		if (is_prime[p]):

			primes.append(p)
			prime_count += 1
						
			for j in xrange((p*p), sieve_limit, p):

				is_prime[j] = False


def CountSemiprimes (problem_limit):

	semiprimes = 0

	# prime_index points to the largest prime that can be multiplied with the current prime
	prime_index = prime_count

	# for semiprimes with one factor as 2
	semiprimes += prime_count

	# limit till which there is need to check is sqrt(problem_limit)
	check_limit = int(math.ceil(problem_limit ** 0.5))

	n = 2
	curr_count = (prime_count - 1)

	while (primes[n] < check_limit):

		curr_prime = primes[n]
		while (curr_prime * primes[prime_index] >= problem_limit):
			prime_index -= 1
			curr_count -= 1	

		semiprimes += curr_count
		curr_count -= 1
		n += 1

	return semiprimes		



if __name__ == '__main__':

	SieveAlgorithm()

	semiprimes = CountSemiprimes(problem_limit)
	print semiprimes		

	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
