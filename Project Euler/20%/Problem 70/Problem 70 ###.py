import time
start_time = time.clock()


def totient(P_fac, n):
    prod = n
    for i in P_fac:
        prod /= i
        prod *= (i-1)

    return prod    
        
    
primes = [num for num in xrange(3, 500000, 2) if all(num%j!=0 for j in xrange(3, int(num**(0.5))+1, 2))]
primes.insert(0, 2)
#print primes

totient_sum = 2
for n in xrange(2, 1000001):
    P_factors = []
    temp = n
    for p in primes:

        if temp==1:
            tot = totient(P_factors, n)
            totient_sum += tot
            break

        if not n%p==0:
            continue

        P_factors.append(p)
        while temp%p==0:
            temp /= p
        

print totient_sum

print "Execution time: %.4f" %(time.clock() - start_time) + " sec"
