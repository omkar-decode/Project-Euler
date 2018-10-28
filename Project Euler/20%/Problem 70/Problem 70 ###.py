import time
start_time = time.clock()

  
def SievePrimes (n):        
    sieve = [1 for i in xrange(n+1)]
    primes = []
    for p in xrange(2, n):
        if sieve[p] == 1:
            primes.append(p)

            for j in xrange((2*p), n+1, p):
                sieve[j] = 0

    return [sieve, primes]


def Totient (n):
    result = n
    check = int(n**0.5)

    for p in primes:
        if (p > check):
            break

        while (n%p == 0):
            n /= p
            result -= (result // p)

    if (n > 1):
        result -= (result // n)

    return result


def CheckPerm (a, b):
    strA = list(str(a))
    strB = list(str(b))

    strA.sort()
    strB.sort()

    if (strA == strB):
        return True

    return False


if __name__ == "__main__":

    n = (10**7)
    sieve, primes = SievePrimes(n)

    minRatio = 100000
    nVal = -1

    for k in xrange(2, n):
        if (sieve[k] == 1):
            continue

        t = Totient(k)
        if (CheckPerm(k, t)):
            ratio = float(k)/float(t)

            if (minRatio > ratio):
                minRatio = ratio
                nVal = k

    print nVal            


print "Execution time: %.4f" %(time.clock() - start_time) + " sec"


