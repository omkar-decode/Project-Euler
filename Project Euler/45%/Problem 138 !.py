import time
start_time = time.clock()

# the general expression for the valid values of L is [F(6n+3)/2], where F(n) is the n'th
# fibonacci number, with F(1)=1 and F(2)=1

# def Exp1 (n):
	
# 	exp = (5*b*b + 8*b + 4)
# 	root = (exp ** 0.5)

# 	if (int(root) == root):
# 		return root

# 	return -1	


# def Exp2 (n):

# 	exp = (5*b*b - 8*b + 4)
# 	root = (exp ** 0.5)

# 	if (int(root) == root):
# 		return root

# 	return -1


if __name__ == '__main__':
	
	limit = 75
	a = 1; b = 2; c = a+b

	L_sum = 0
	n = 4
	for i in xrange(limit):
		if ((n-3) % 6 == 0):
			L_sum += (c/2)

		a = b
		b = c
		c = a+b

		n += 1

	print L_sum	


	# checking for every even number takes too much time to execute
	# for b in xrange(2, limit, 2):
		
	# 	term1 = Exp1(b)
	# 	if (term1 != -1):
	# 		print "h = b+1, where b=%d and L=%d" %(b, term1/2)

	# 	term2 = Exp2(b)
	# 	if (term2 != -1):
	# 		print "h = b-1, where b=%d and L=%d" %(b, term2/2)

	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"