import time
start_time = time.clock()


# the idea is to use binomial expansions to find coefficient of x^r
# Note: see readme of this problem for detailed explanation

# nCr_fill_r() method fills up the passed table with nCr for given (fixed) value of r
# table[k] gives the value of (k+r)Cr
def nCr_fill_r (r, n, table):

	table[0] = 1
	# here, we have used pCr = (p-1)Cr * (p / (p-r))
	for p in xrange(r+1, n+r+1):
		table[p-r] = (table[p-r-1] * p) / (p-r)


# nCr_fill_n() method fills up the passed table with nCr for given (fixed) value of n
# table[k] gives the value of nCk
def nCr_fill_n (n, table):

	table[0] = 1
	for r in xrange(1, (n+1)):
		table[r] = (table[r-1] * (n+1-r)) / r


if __name__ == "__main__":

	# a and b denote the number of faces on the two types of dies
	a = 4; b = 6

	# n and m are the number of dies of each type (n --> a; m --> b)
	n = 9; m = 6

	# following are the tables for nCr and mCr, such that table[r] gives the value of nCr
	nCr_table_n = [0 for i in xrange(n+1)]
	mCr_table_n = [0 for i in xrange(m+1)]

	# following are the tables for nCr and mCr, such that table[n] gives the value of (n+r)Cr, where n starts from 0
	nCr_table_r = [0 for i in xrange((a*n)+1)]
	mCr_table_r = [0 for i in xrange((b*m)+1)]

	# following 4 commands fill up the 4 tables
	nCr_fill_n(n, nCr_table_n)
	nCr_fill_r((n-1), (a*n), nCr_table_r)

	nCr_fill_n(m, mCr_table_n)
	nCr_fill_r((m-1), (b*m), mCr_table_r)


	# a_freq[k] gives the number of ways of obtaining a sum k on rolling n dies of type 'a'
	# Note: since the minimum roll sum is n, a_freq[0] through a_freq[n-1] is 0
	a_freq = [0 for i in xrange((a*n)+1)]

	# iterate over all possible roll sums
	# observe that x^n has been taken common from the expansion
	# (x + x^2 + x^3 + ... + x^a)^n = x^n * (1 + x + x^2 + ... + x^(a-1))^n
	for roll in xrange(n, (a*n)+1):

		# r is the coefficient after taking the common exponent out
		r = (roll - n)

		# x^r1 comes from (1 - x^a)^n
		# x^r2 comes from (1 - x)^(-n)
		for j in xrange(r+1):
			r1 = j
			r2 = (r-j)

			# coeff_1 --> coefficient of x^r1
			# coeff_2 --> coefficient of x^r2
			coeff_1 = 0
			if (r1 % a == 0):
				temp = r1 / a
				coeff_1 = nCr_table_n[temp]
				if (temp % 2 == 1):
					coeff_1 = (coeff_1 * -1)

			coeff_2 = nCr_table_r[r2]

			a_freq[roll] += (coeff_1 * coeff_2)


	# do the same as above for 'b'
	b_freq = [0 for i in xrange((b*m)+1)]

	for roll in xrange(m, (b*m)+1):

		r = (roll - m)

		for j in xrange(r+1):
			r1 = j
			r2 = (r-j)

			coeff_1 = 0
			if (r1 % b == 0):
				temp = r1 / b
				coeff_1 = mCr_table_n[temp]
				if (temp % 2 == 1):
					coeff_1 = (coeff_1 * -1)
				# print roll, coeff_1

			coeff_2 = mCr_table_r[r2]

			b_freq[roll] += (coeff_1 * coeff_2)
	

	# total number of dice configurations possible for each type
	sample_space_a = (a ** n)
	sample_space_b = (b ** m)

	# number of cases where 'a' wins
	a_wins = 0

 	# use a_freq[] and b_freq[] to compute number of cases where 'a' wins
	for sum_a in xrange(n, (a*n)+1):
		for sum_b in xrange(m, (b*m)+1):

			if (sum_a <= sum_b):
				continue

			a_wins += (a_freq[sum_a] * b_freq[sum_b])


	# calculate the probability of 'a' winning
	prob_win_a = float(a_wins)/float(sample_space_a * sample_space_b)
	print prob_win_a		

	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
