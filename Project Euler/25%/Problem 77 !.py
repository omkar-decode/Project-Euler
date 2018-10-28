# use Dynamic Programming to count number of summations
# idea is similar to 'Coin Change Problem', check at 'https://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/'

import time
start_time = time.clock()

# use bottom-up approach to find number of summations

def SievePrimes (n):
    sieve = [True for i in xrange(n+1)]
    primes = []

    for p in xrange(2, n+1):
        if (sieve[p] == True):
            primes.append(p)

            for j in xrange((2*p), n+1, p):
                sieve[j] = False

    return primes


def CountSummations(m, n, primes):

    table = [[0 for i in xrange(m)] for j in xrange(n+1)]

    for i in xrange(m):
        table[0][i] = 1

    # fill up table in a bottom-up manner
    for i in xrange(1, n+1):
        for j in xrange(m):

            x = 0
            # solutions which include primes[j]
            if ((i - primes[j]) >= 0):
                x = table[i-primes[j]][j]

            y = 0
            # solutions which exclude primes[j]
            if (j >= 1):
                y = table[i][j-1]

            table[i][j] = (x+y)

    return table[n][m-1]        
  


if __name__ == "__main__":

    n = 100000
    ways = 5000
    
    primes = SievePrimes(n)
    l = len(primes)

    sumValue = 10
    
    while (True):
        
        sumValue += 1
        
        numWays = CountSummations(l, sumValue, primes)
        if (numWays > ways):
            break

    print sumValue
    

print "Execution time: %.5f" %(time.clock() - start_time) + " sec"
