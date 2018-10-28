import time
start_time = time.clock()






if __name__ == "__main__":

    n = 10**8; n /= 2
    n = 10**4
    sieve = [True for i in xrange(n)]
    primes = []
    
    for p in xrange(2, n):
        if (sieve[p] == True):
            primes.append(p)

            for i in xrange((2*p), n, p):
                sieve[i] = False

    print len(primes)


print "Execution time: %.5f" %(time.clock() - start_time) + " sec"
