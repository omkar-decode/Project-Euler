import time
start_time = time.clock()

# the idea is to generate pythagorean triples upto a limit and use a python dictionary to check if
# a triangle with that perimeter has been obtained earlier

# the triplets are generated using the method explained in this article:
#	http://mathforum.org/library/drmath/view/55811.html

# since perimeter of the triangle will be 2m(m+n), take highest perimeter as 1,500,000 to get 
# highest value of m to be a bit less than 870 (assuming n is 1)
# therefore, generator_limit is set to 870


def Gcd (m, n):

	if (m < n):
		m, n = n, m

	while (n != 0):
	
		rem = m%n
		m = n
		n = rem	

	return m


if __name__ == '__main__':
	
	# generate all primitive pythagorean triples using the m-n-method
	generator_limit = 870

	perimeter_limit = 1500000
	triangle_freq = {}

	L_cnt = 0

	for m in xrange(2, generator_limit+1):
		for n in xrange(1, m):

			if ((m%2) ^ (n%2) == 0):
				continue

			if (Gcd(m, n) > 1):
				continue

			# perimeter will be [(m^2 + n^2) + (m^2 - n^2) + (2mn)]
			perimeter = (2 * m * (m+n))

			if (perimeter > perimeter_limit):
				continue

			# since the method generates only primitive triplets, iterate through all multiples of the triplet
			for p in xrange(perimeter, perimeter_limit, perimeter):

				if p in triangle_freq:
					if (triangle_freq[p] == 1):
						L_cnt -= 1
						triangle_freq[p] = -1	

				else:
					triangle_freq[p] = 1
					L_cnt += 1	


	print L_cnt				

	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"


			
