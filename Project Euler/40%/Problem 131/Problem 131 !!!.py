import time
start_time = time.clock()

# the idea is to find a relationship between the prime p and the number n
# Note: refer the problem's readme for a detailed explanation

sieve_size = 1000005
limit = 1000000

# create a sieve for prime checking
def SieveOfEratosthenes (checkPrime):

	checkPrime[0] = False
	checkPrime[1] = False

	for p in xrange(2, sieve_size):
		if (not checkPrime[p]):
			continue

		for i in xrange((2*p), sieve_size, p):
			checkPrime[i] = False	


# generate a number which, if prime, is a special prime according to the problem
def GenerateCubePrime (x):
	return ((3*x*x) + (3*x) + 1)			


if __name__ == '__main__':
	
	checkPrime = [True for i in xrange(sieve_size)]
	SieveOfEratosthenes(checkPrime)
	
	prime_count = 0

	x = 1
	while(True):

		num = GenerateCubePrime(x)
		if (num > limit):
			break

		if (checkPrime[num]):
			prime_count += 1

		x += 1	


	print prime_count

	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"	

