import math
import time
start_time = time.clock()

def gcd(a, b):
    rem = b%a
    if(rem==0):
        return a

    return gcd(rem, a)


count = 0
for denom in xrange(1, 12001):
    num_min = int(math.ceil((float(denom))/3))
    num_max = int(math.floor((float(denom))/2))

    for num in xrange(num_min, num_max+1):
        rem = denom % num

        #if rem is 1, then num and denom are definitely coprime
        if(rem==1):
            count += 1
            continue

        #if rem is 0, then it is not a reduced fraction
        if(rem==0):
            continue

        #test for coprime-ness of smaller integers
        if(denom%rem==0 and num%rem==0):
            continue

        if(gcd(num, denom)!=1):
            continue

        count += 1

print count

print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
