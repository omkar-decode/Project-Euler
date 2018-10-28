import time
start_time = time.clock()


# find the radical of all the numbers and then sort them according to rad
numbers = [i for i in xrange(100001)]
rads = [-1 for i in xrange(100001)]
rads[1] = 1
primes = [2]

# create a list of all primes upto 100000 and use the fact that rad(p) = p for all prime p
for i in xrange(3, 100000, 2):
    if all(i%j!=0 for j in xrange(3, i, 2)):
        primes.append(i)
        rads[i] = i
        
for i in xrange(4, 100001):
    if(rads[i] != (-1)):
        continue

    num = i; rad = 1
    for p in primes:
        if(num==1):
            break

        if(num%p==0):
            rad *= p
            while(num%p==0):
                num /= p

    rads[i] = rad

pairs = zip(rads, numbers)
pairs.sort(key = lambda t: t[0])

print pairs[10000]

print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"

    
