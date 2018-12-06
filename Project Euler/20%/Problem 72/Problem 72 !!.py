import time
import math
import itertools

start_time = time.clock()

# the idea is that for a given denominator d, the number of possible
# numerators is Totient(n), giving those many number of fractions

# also, a given fraction cannot be repeated for two different d's since
# all the fractions we are generating are already in their lowest form

# therefore, the total number of fractions is simply
#	Summation(phi(d)) 	for 2 <= d <= 1000000


limit = 1000000

# spf[k] gives the Smallest Prime Factor of k
spf = [i for i in xrange(limit+1)]

def SieveAlgorithm ():
	
	for i in xrange (4, limit+1, 2):
		spf[i] = 2

	for p in xrange (3, limit+1, 2):
		
		if (spf[p] == p):
			for j in xrange ((p*p), limit+1, (2*p)):
				if (spf[j] == j):
					spf[j] = p


# calculate phi(n) using Shortest Prime Factor method
def Totient (n):

	tot = n
	while (spf[n] > 1):

		curr_p = spf[n]
		tot /= curr_p
		tot *= (curr_p-1)

		while (spf[n] == curr_p):
			n /= spf[n]

	return tot		


if __name__ == '__main__':	

	SieveAlgorithm()

	fraction_count = 0
	for d in xrange (2, limit+1):
		fraction_count += Totient(d)

	print fraction_count			

	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
