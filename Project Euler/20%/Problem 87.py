import time
start_time = time.clock()

limit = 50000000
n = int(limit ** 0.5)
sieve = [1 for i in xrange(n+1)]

primes = []
for j in xrange(2, n+1):
    if (sieve[j]==1):

        primes.append(j)
        for k in xrange((2*j), n+1, j):
            sieve[k] = 0

# values is a dictionary which is used to check if a number has been counted previously or not
values = {}

# 908 is the number of primes less than (limit^(1/2))
# 73 is the number of primes less than (limit^(1/3))
# 23 is the number of primes less than (limit^(1/4))

cnt = 0
for two in xrange(908):
    for three in xrange(73):
        for four in xrange(23):

            term = (primes[two] ** 2) + (primes[three] ** 3) + (primes[four] ** 4)

            if term in values:
                continue
            
            if (term < limit):
                cnt += 1
                values[term] = 1

print cnt


print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
  
