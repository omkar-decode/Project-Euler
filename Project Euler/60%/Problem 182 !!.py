import time
start_time = time.clock()

# use the result that the number of unconcealed messages for a given e and n is:
#	unconcealed_msgs = (gcd(p-1, e-1) * gcd(q-1, e-1))
# where p and q are primes such that n=pq

def Gcd (m, n):

    if (m > n):
            m, n = n, m

    while (n != 0):
            temp = n
            n = m%n
            m = temp

    return m
                    

if __name__ == "__main__":

    p = 1009
    q = 3643

    n = p*q
    phi_n = (p-1)*(q-1)

    unconcealed_freq = {}

    for e in xrange (2, phi_n):
            
            if (Gcd(e, phi_n) != 1):
                    continue

            unconcealed_msgs = (Gcd(e-1, p-1)+1)*(Gcd(e-1, q-1)+1)

            if (unconcealed_msgs not in unconcealed_freq):
            	unconcealed_freq[unconcealed_msgs] = [0]
            else:	
            	unconcealed_freq[unconcealed_msgs][0] += 1

            unconcealed_freq[unconcealed_msgs].append(e)


    min_m = 10**10

    for m in unconcealed_freq:
    	if (m < min_m):
    		min_m = m

    sum_e = 0
    e_cnt = len(unconcealed_freq[min_m])
    for i in xrange (1, e_cnt):
            sum_e += unconcealed_freq[min_m][i]

    print sum_e	


print "Execution time: %.5f" %(time.clock() - start_time) + " sec"
