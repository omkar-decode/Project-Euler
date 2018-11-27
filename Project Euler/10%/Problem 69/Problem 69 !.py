
# this problem can be solved using just a pen and paper
# we know, phi(n) = n * (1-(1/p1))*(1-(1/p2))*...*(1-(1/pk)), where p1,p2,...,pk are the k distinct prime factors of n

# therefore, we get (n / phi(n)) = Product [pi/(pi-1)] for i going from 1 to k
# in order to maximise the LHS, we need to maximise the number of prime factors of n (i.e., maximise k), since
# the RHS is product of k numbers all of which are greater than 1

# if we start with 2 and take each prime number exactly once, we see that:
#	2 x 3 x 5 x 7 x 11 x 13 x 17 = 510510

# taking any more primes would make n > 1,000,000
# therefore, the n which maximises the ratio is 510510


# the method below is a very inefficient one

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
