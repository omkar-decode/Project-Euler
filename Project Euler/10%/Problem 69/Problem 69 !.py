def totient(P_fac):
    prod = 1.0
    for i in P_fac:
        prod *= (float(i))/(i-1)

    return prod    
        
    
primes = [num for num in xrange(3, 500000, 2) if all(num%j!=0 for j in xrange(3, int(num**(0.5))+1, 2))]
primes.insert(0, 2)
#print primes

max_ratio = 0.0; curr_ratio = 0.0
max_n = 0

for n in xrange(1000000, 1, -2):
    P_factors = []
    temp = n
    for p in primes:
        if temp==1:
            curr_ratio = totient(P_factors)
            if curr_ratio>max_ratio:
                max_ratio = curr_ratio
                max_n = n
            break
        if not n%p==0:
            continue
        P_factors.append(p)
        while temp%p==0:
            temp /= p
        

print max_n        
