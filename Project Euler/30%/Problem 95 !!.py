import time
import math
import itertools

start_time = time.clock()

# use Smallest Prime Factor array to find the sum of factors of a number efficiently


limit = 1000001
spf = [i for i in xrange(limit)]

def SieveAlgorithm ():

	for i in xrange (4, limit, 2):
		spf[i] = 2

	for p in xrange (3, limit, 2):
		
		if (spf[p] == p):
			for j in xrange ((p*p), limit, (2*p)):
				spf[j] = p


# returns sum of factors of n in log(n) time
def SumOfFactors (n):

	if (spf[n] == n):
		return 1

	factor_sum = 1
	temp_n = n
	
	while (spf[temp_n] > 1):
		curr_prime = spf[temp_n]
		curr_expo = 0

		while (spf[temp_n] == curr_prime):
			curr_expo += 1
			temp_n /= spf[temp_n]

		term = (curr_prime ** (curr_expo+1)) - 1
		term /= (curr_prime-1)

		factor_sum *= term

	factor_sum -= n
	return factor_sum	


if __name__ == '__main__':

	SieveAlgorithm()

	threshold = 1000000
	visited = [False for i in xrange(threshold+1)]

	visited[0] = visited[1] = True

	# as given in the problem
	max_chain_len = 5
	longest_chain = []

	for n in xrange (2, threshold+1):
		if (visited[n] or spf[n] == n):
			visited[n] = True
			continue


		curr_num = n
		chain_len = 0
		chain_elems = []

		flag = 0

		# the second condition checks if curr_num is prime or not
		# if curr_num is prime, then a chain is not possible
		while (curr_num <= threshold and spf[curr_num] != curr_num):
			visited[curr_num] = True
			chain_elems.append(curr_num)


			# the following condition checks if a loop has been formed
			# however, the number of elements 'in' the loop may not be equal to chain_len
			# for example, consider [12032 → 12496 → 14288 → 15472 → 14536 → 14264]
			# here, 12032 is NOT a part of the chain, since 14264 is followed by 12496
			curr_num = SumOfFactors(curr_num)
			if (curr_num < threshold and visited[curr_num]):
				
				# find the index of first element of the amicable chain and truncate chain_elems[] accordingly
				chain_len = len(chain_elems)
				for e in chain_elems:
					if (e == curr_num):
						break

					chain_len -= 1

				chain_elems = chain_elems[(len(chain_elems)-chain_len):]
				flag = 1	
				break

		# update max_chain_len and longest_chain[]
		if (flag == 1 and chain_len > max_chain_len):
			max_chain_len = chain_len
			longest_chain = chain_elems


	# print longest_chain
	# print max_chain_len			
	print min(longest_chain)
			
	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"


