import time
start_time = time.clock()

# for a detailed explanation of the solution, go through readme_158

n_limit = 26
alphabets = 26

def nCr (n, r):
	
	r = min(r, (n-r))	

	if (r == 0):
		return 1

	val = 1
	for j in xrange(1, r+1):
		val *= (n-j+1)
		val /= j

	return val


# this method returns the number of valid permutations for strings of length n
def CountValidPerms (n):
	return ((2 ** n) - n - 1)


if __name__ == '__main__':
	
	max_pn = 0

	for n in xrange(1, n_limit+1):

		valid_perms = CountValidPerms(n)
		valid_perms *= nCr(alphabets, n)

		if (valid_perms > max_pn):
			max_pn = valid_perms


	print max_pn	

	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"		