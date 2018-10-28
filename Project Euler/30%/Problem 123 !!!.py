import time
start_time = time.clock()

# the main idea is based on the observation that:
# { for all even n, the remainder is 2 }
# { for all odd n, the remainder is (2 * n * p(n)) }

# so, we need to iterate only among the odd indexed primes
# we simply need to find the first n such that (2*n*p(n)) > 10^10

   
# gmpy2 library is used to generate primes
# this library has been used in this problem for generating next primes
import gmpy2


# below function checks if the remainder exceeds 10^10
# since p(n)>(2*n) for all n>7037, the remainder for odd n will always be (2*n*p(n))
def RemainderCheck (n, p):   
    rem = (2*n*p)
    if (rem > minRem):
        return n

    return False


# below function takes a prime number and returns the second prime number after it 
def NextNextPrime (p):
    p = gmpy2.next_prime(p)
    p = gmpy2.next_prime(p)

    return p
        
    
if __name__ == "__main__":

    minRem = (10**10)
    
    givenIndex = 7037
    iterations = (givenIndex // 2)

    n = 1; p = 2

    # find the 7037th prime, since the required prime is definitely greater than p(7037)
    for i in xrange(iterations):
        p = NextNextPrime(p)
        n += 2

    while (True):
        if (RemainderCheck(n, p) != False):
            break
        
        p = NextNextPrime(p)
        n += 2

    print n        
    

print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec" 
        
