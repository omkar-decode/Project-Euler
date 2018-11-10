import time
import math

start_time = time.clock()

# we use the m-n-method to generate primitive pythagorean triples
# to avoid non-primitive triples, we impose the parity and gcd conditions

# if a given primitive triplet (a, b, c) forms a valid pythagorean tile, then all multiples of 
# this triplet will form a valid pythagorean tile

# similarly, if a given primitive triplet (a, b, c) does NOT form a valid pythagorean tile, then no multiple of 
# this triplet will form a valid pythagorean tile


def Gcd (m, n):

	if (m < n):
		m, n = n, m

	rem = -1
	while (rem != 0):
		rem = m%n
		m = n
		n = rem

	return m		


if __name__ == '__main__':
	
	# generator_limit is calculated using the fact that the perimeter is given by 2m(m+n)
	# therefore, for n=1, we get highest value of m to be around 7100
	generator_limit = 7100
	perimeter_limit = 100000000

	tile_count = 0

	for m in xrange (2, generator_limit):
		for n in xrange (1, m):

			if ((m%2) ^ (n%2) == 0):
				continue

			if (Gcd(m, n) > 1):
				continue


			a = (m*m) - (n*n)
			b = (2*m)*n
			c = (m*m) + (n*n)

			perimeter = (a+b+c)
			if (perimeter > perimeter_limit):
				break

			if (c % abs(a-b) == 0):
				
				# type_count is the count of number of triples which are a multiple
				# of the primitive triple (a, b, c), having perimeter < perimeter_limit
				type_count = int(math.ceil(float(perimeter_limit)/perimeter)) - 1
				tile_count += type_count


	print tile_count				

	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
