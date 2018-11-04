import time
start_time = time.clock()

import math

e = math.exp(1)

# given a N, we need to find a k such that f(k) = [(N/k)^k] is maximum
# differentiate f(k) and equate to 0
# the simplified result we get is [k = (N/e)]
# round off the value of k to the nearest integer for this problem


# returns the gcd of m and n
def Gcd (m, n):

	if (m > n):
		m, n = n, m

	if (m == 1):
		return m

	rem = n % m
	while (rem != 0):

		temp = m
		m = (n%m)
		n = temp

		rem = (n % m)	

	return m


# check if (p/q) is a terminating rational number or not
# use the fact that (p/q) is terminating iff [q = (2^a)*(5^b) where a,b >= 0]
def IsTerminating (p, q):
	
	# divide p and q by their gcd to make them coprime
	gcd = Gcd(p, q)

	q /= gcd

	while (q % 2 == 0):
		q /= 2

	while (q % 5 == 0):
		q /= 5

	if (q > 1):
		return False

	return True			


def MaxSplitPower (N):

	k = int(round((float(N)/e), 0))

	if (IsTerminating(N, k)):
		return (-1 * N)

	return N	


if __name__ == '__main__':			

	lower_bound = 5
	upper_bound = 10000

	summation = 0

	for N in xrange(lower_bound, upper_bound+1):
		summation += MaxSplitPower(N)

	print summation	

	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"	