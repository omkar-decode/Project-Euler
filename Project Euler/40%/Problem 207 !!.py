import time
import math

start_time = time.clock()

# k is of the form [n(n-1)]; keep generating k's till the proportion falls below the given threshold


# this method returns true if (f1<f2)
def CompareFractions (f1, f2):
	
	if ((f1[0]*f2[1] - f1[1]*f2[0]) < 0):
		return True

	return False		
			

if __name__ == '__main__':

	threshold = [1, 12345]

	# put a check_limit to make the while loop finite
	check_limit = 300000
	m = 1

	proportion = [0, 0]
	k = 0

	while (m < (check_limit+1)):

		k = m*(m+1)
		t = math.log((m+1), 2)

		proportion[1] += 1

		if (t == int(t)):
			proportion[0] += 1
	
		if (CompareFractions(proportion, threshold)):
			break

		m += 1	


	print k

	print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"


