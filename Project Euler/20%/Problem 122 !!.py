import time
start_time = time.clock()


# the idea is to take three cases for the value of (n % 4) for n-digit numbers
# for each case, generalise the number of n-digit reversible numbers

# if n == 4k+1, ways = 0
# if n == 2k, ways = (20 * (30^(k-1)))
# if n == 4k+3, ways = (100 * (500^k))

def CountReversible (n):

	# n == 4k+3
	if (((n-3) % 4) == 0):
		return (100 * ((500)**((n-3)/4)))

	# n == 2k
	if ((n % 2) == 0):
		return (20 * ((30)**((n-2)/2)))

	# n == 4k+1
	return 0		


if (__name__ == "__main__"):

	# upper limit for number of digits to check
	limit = 9

	# count of reversible numbers
	num_count = 0

	d = 1
	while (d <= limit):
		
		num_count += CountReversible(d)
		d += 1

	print num_count
	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"	