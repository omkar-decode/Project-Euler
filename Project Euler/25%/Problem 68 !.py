import time
import math
import itertools

start_time = time.clock()

# generate all possible valid sequences and find the maximum

n = 10
max_string = '0'

def EqualSumSequences ():

	# five loops for 5 inner numbers
	for p in xrange (1, n+1):
		for q in xrange (1, p):
			for r in xrange (1, q):
				for s in xrange (1, r):
					for t in xrange (1, s):

						check = [False for i in xrange(n+1)]
						
						check[p] = True
						check[q] = True
						check[r] = True
						check[s] = True
						check[t] = True

						remaining = [i for i in xrange(1, n+1) if not check[i]]

						elements = [p, q, r, s, t]

						# generate all permutations of the 5 inner cells
						perms = map(list, list(itertools.permutations(elements)))

						for per in perms:

							sums = []
							for k in xrange(5):

								pair_sum = (per[k]+per[(k+1)%5])
								# include the index k to keep track of the element pair which gave pair_sum
								sums.append([pair_sum, k])


							# since remaining[] is sorted in increasing order, 
							# sums[] should be sorted in decreasing order
							# Reason: we want (remaining[i]+sums[i]) to be equal for all 5 lines
							sums.sort(reverse=True)	

							line_total = sums[0][0]+remaining[0]

							flag = 0
							for i in xrange(1, 5):
								if (sums[i][0]+remaining[i] != line_total):
									flag = 1
									break

							if (flag == 1):
								continue		

							string = ''
							start = sums[0][1]

							# generate the string corresponding to the arrangement
							for i in xrange (start, start+5):
								string += str(line_total - (per[i%5]+per[(i+1)%5]))
								string += str(per[i%5])
								string += str(per[(i+1)%5])

							global max_string
							if (string > max_string):
								max_string = string



if __name__ == '__main__':	

	EqualSumSequences()

	print max_string
	
	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
