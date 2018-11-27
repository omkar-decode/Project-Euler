import time
start_time = time.clock()

# NOTE: this question can be solved on paper as well
# consider p, q, m, n, a, b, c as given below in the code
# area of the triangle will be -->	2pq(p+q)(p-q)(p^4+q^4-6p^2q^2)
#
# consider the (T =) [2pq(p+q)(p-q)] part:
# for any combination of parity of p and q, T would be divisible by 4
# similarly, for any combination of p and q, T would divide 3
#
# we need to prove the area would be divisible by 7 as well
# take all possible cases on p and q for remainders when divided by 7
# we get that area is divisible by 7

# therefore, the area is always divisible by 6 and 28


# (refer Problem 86 solution for "How to generate all primitive pythagorean triplets")
# use pythagorean parametrization twice 

# iterate over p and q to generate primitive triplets;
# let m = max(p^2-q^2, 2pq) and n = min(p^2-q^2, 2pq)

# now, the sides of the triangle are:
#	a = m^2 - n^2
#	b = 2mn
#	c = m^2 + n^2

# by this method, c will always be a perfect square


def Gcd (m, n):

	if (m < n):
		m, n = n, m

	while (n != 0):
		m, n = n, m%n

	return m		


if __name__ == '__main__':

	c_limit = 10**16
	
	# since c == (m^2+n^2) == (approximately) p^4; p needs to go upto (c_limit ^ (1/4)) 
	generator_limit = int(c_limit ** 0.25)
	perfect_cnt = 0

	for p in xrange (2, generator_limit):
		for q in xrange(1, p):

			if ((p%2) ^ (q%2) == 0):
				continue
			if (Gcd(p, q) > 1):
				continue

			t1 = (p*p - q*q)
			t2 = (2*p*q)

			m = max(t1, t2)	
			n = min(t1, t2)


			c = (m*m + n*n)
			if (c > c_limit):
				continue

			a = (m*m - n*n)
			b = (2*m*n)	

			# print a, b, c

			area = (b/2)*a

			if (area%6 != 0 or area%28 != 0):
				perfect_cnt += 1


	print perfect_cnt		
	
	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"	
