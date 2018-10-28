import time
start_time = time.clock()

#print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"    


n = 10000      
sieve = [1 for i in xrange(n+1)]

primes = []
for i in xrange(2, n):

    if sieve[i] == 1:
        primes.append(i)

        for j in xrange((2*i), n+1, i):
            sieve[j] = 0

d = len(primes)
print d

total = 0
index = 0
while (index<d and total < n):
    total += primes[index]
    index += 1

##total -= primes[index-1]
##print index+1
##print primes[index-1]
##print total
##print 
