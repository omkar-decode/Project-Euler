import time
import math
import itertools

start_time = time.clock()


# My solution:
# the idea is to realise that:
#	(n/phi(n)) = Product(p(i)/(p(i)-1)) for each p(i) | n, i.e., for each p(i) that divides n

# Observation 1: Number of primes in the prime factorisation of n must be less
# Observation 2: (p/(p-1)) gives a smaller value for a larger p, implying 
#					we need our prime factors to be as large as possible

# combining the two observations, we guess that the number n should have 
# 	only 2 prime factors (occuring only once) which are both as large as possible

# Therefore, we start from r = sqr_root(10000000), and choose some p1 and p2 (p1>r and p2<p1), 
# 	while checking all other given conditions too (p1*p2 < 10000000)


# From the discussion forum (very similar to my idea): 
# the ratio would be minimum for prime n (ratio = n/(n-1))
# but for prime n, (n-1) can never be a permutation of n
# Therefore, the next step is to assume a semiprime n


# since we expect our primes to lie around sqr_root(10000000) == 3200 (approx), we generate primes only upto 10000
limit = 10000
sieve = [True for i in xrange(limit)]

primes = []
prime_count = 0

def SieveAlgorithm ():
	sieve[0] = sieve[1] = False
	
	global prime_count
	global primes

	primes.append(2)
	prime_count += 1
	for i in xrange (4, limit, 2):
		sieve[i] = False

	for p in xrange (3, limit, 2):
		if (sieve[p]):
			primes.append(p)
			prime_count += 1

			for j in xrange ((3*p), limit, (2*p)):
				sieve[j] = False


# p1 and p2 are the only two prime factors of n, i.e., n = (p1*p2)
def Totient (p1, p2):

	return ((p1-1)*(p2-1))


def IsPermutation (n1, n2):

	l1 = list(str(n1))
	l2 = list(str(n2))

	l1.sort()
	l2.sort()

	return (l1 == l2)


# returns true if f1 < f2
def IsFractionLess (f1, f2):

	return ((f1[0]*f2[1]) < (f1[1]*f2[0]))



if __name__ == '__main__':	

	SieveAlgorithm()

	threshold = 10000000

	# index denotes the index of prime closest (approx) to sqr_root(threshold)
	index = -1
	sqr_root = int(threshold ** 0.5)
	for p in xrange(prime_count):
		if (primes[p] > (sqr_root)):
			index = p
			break

	# the instance given in the problem
	min_ratio = [87109, 79180]
	min_n = -1
	
	for i in xrange(index, prime_count):
		for j in xrange(i):

			p1 = primes[i]; p2 = primes[j]

			if (p1*p2 >= threshold):
				continue

			num = (p1*p2)
			tot = Totient(p1, p2)
	
			if (IsPermutation(num, tot)):
				if (IsFractionLess([num, tot], min_ratio)):
					min_ratio = [num, tot]
					min_n = num
					# print p1, p2, min_ratio


	print min_n
	# print min_n, min_ratio			
				

	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
