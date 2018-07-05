#primes = [2]+[i for i in xrange(3, 1000000, 2) if all(i%j for j in xrange(3, i/2+1, 2))]
#print sum(primes)
tot = 2; count = 1
for i in xrange(3, 1000000, 2):
    if all(i%j for j in xrange(3, i/2+1, 2)):
        tot+=i; count+=1
print tot        
