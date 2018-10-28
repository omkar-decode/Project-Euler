import time
start_time = time.clock()


# below function returns a list of primes less than or equal to n
def SievePrimes (n):

    sieve = [1 for i in xrange(n+1)]
    primes = []

    for p in xrange(2, n+1):
        if (sieve[p] == 1):
            primes.append(p)

            for j in xrange((2*p), n+1, p):
                sieve[j] = 0

    return primes            


# below function returns the number of multiples of the given prime in the range [start, stop)
def MultiplesInRange (start, stop, prime):

    return (((stop-1)//prime) - ((start-1)/prime))


# below function returns the exponent of the given prime in the product of all numbers in the range [start, stop)
def ExponentInProductOfRange (start, stop, prime):

    exponent = 0
    currFactor = prime

    while (currFactor < stop):
        exponent += MultiplesInRange(start, stop, currFactor)
        currFactor *= prime

    return exponent


# below function returns the sum of terms in prime factorisation for nCr
def FindPrimeFactorSum (n, r):

    sumPrimeFactors = 0
    primes = SievePrimes(n)

    for p in primes:

        # find the difference in the exponent of the prime in numerator & denominator and add the prime those many times
        # this is equivalent to finding the difference in exponent and multiplying the prime with it
        sumPrimeFactors += (ExponentInProductOfRange((n-r+1), n+1, p) - ExponentInProductOfRange(1, r+1, p)) * p

    return sumPrimeFactors


if __name__ == "__main__":

    n = 20000000
    r = 15000000

    print FindPrimeFactorSum(n, r)



print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
    
