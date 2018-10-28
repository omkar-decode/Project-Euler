import time
start_time = time.clock()


# the approach is essentially brute force
# the code runs in around 110 seconds

primes = []
limit = 200000
sieve = [1 for i in xrange(limit)]
for j in xrange(2, limit):
    if (sieve[j] == 1):
        primes.append(j)
        for k in xrange((2*j), limit, j):
            sieve[k] = 0

          

def prime_fac(n):
    tot = 0
        
    for i in primes:
        if (n%i==0):
            tot += 1
            if tot>4:
                return 5
    return tot        


cond = True; i = 200
while (i<limit):
    
    if (i<limit and sieve[i]==0):
        if prime_fac(i)==4:
            if prime_fac(i+1)==4:
                if prime_fac(i+2)==4:
                    if prime_fac(i+3)==4:
                        print i
                        break
                    else:
                        i += 4
                else:
                    i += 3
            else:
                i += 2

    i += 1            
            


print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"

